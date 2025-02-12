import requests
import datetime
import json
import logging
import time
import clickhouse_connect
from config import host,username,password

url  = "http://api.open-notify.org/astros.json"


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(".venv/bin/app.log"), logging.StreamHandler()],
)


def get_json(url : str = url, max_retries : int = 5, timeout : int = 2) -> dict[str,any]:
    """Function gets data by url and returns dictionary"""
    for attempt in range(1,max_retries + 1):
        try:
            response = requests.get(url)
            time.sleep(timeout)
            response.raise_for_status()
            logging.info("STATUS CODE == 200")
            return response.json()
        except requests.exceptions.RequestException as e:
             logging.warning(f"ATTEMPT {attempt}/{max_retries} REQUEST ERROR: {e}")
             timeout += 1
             if attempt == max_retries:
                logging.error(f"ERROR: {e}")
        except json.JSONDecodeError as e:
             logging.warning(f"ATTEMPT: {attempt}/{max_retries} REQUEST ERROR: {e}")
             timeout += 1
             if attempt == max_retries:
                logging.error(f"DECODE ERROR: {e}")


def json_data() :
    """This function write json into file : for_raw_data/file_json.txt """
    data = get_json()
    if isinstance(data, dict):
        res_data = data['people']
        result = '\n'.join(map(lambda x : json.dumps(x), res_data))
        with open('for_raw_data/file_json.txt', 'w') as file:
            file.write(result)
        logging.info("DATA WAS LOADED TO FILE SUCCESSFULLY")
    else:
        raise  TypeError("object should be dictionary")


class Datebase:
    """Class for connection to clickhouse and realizing all the logic"""
    def __init__(self, host : str = host, username : str = username, password: str = password):
        try:
            self.connection = clickhouse_connect.get_client(host = host,username = username,password = password)
            logging.info("SUCCESSFUL CONNECTION")
        except Exception as e:
            logging.error(f"ERROR {e}")


    def raw_table_creation(self):
        table_creation = """
        CREATE TABLE IF NOT EXISTS raw_data(
        load_time DateTime64(6),
        json_data String
        )
        ENGINE  = ReplacingMergeTree()
        ORDER BY json_data;
        """
        try:
            self.connection.query(table_creation)
            logging.info("TABLE raw_data WAS CREATED OR ALREADY EXISTS")
        except Exception as e:
            logging.error(f"ERROR: {e}")
            raise

    def create_parsed_table(self):
        table_creation = """
        CREATE TABLE IF NOT EXISTS parsed_table(
        _inserted_at DateTime,
        craft String,
        name String
        ) ENGINE  = ReplacingMergeTree()
        ORDER BY name ;
        """
        try:
            self.connection.query(table_creation)
            logging.info("TABLE parsed_table WAS CREATED OR ALREADY EXISTS")
        except Exception as e:
            logging.error(f"ERROR: {e}")
            raise

    def create_materialized_view(self):
        table_creation = """
        CREATE MATERIALIZED VIEW IF NOT EXISTS parsed_mv TO parsed_table AS
        SELECT
        NOW() as _inserted_at,
        JSONExtractString(json_data, 'craft') AS craft,
        JSONExtractString(json_data, 'name') AS name
        FROM raw_data;
        """
        try:
            self.connection.query(table_creation)
            logging.info("MATERIALIZED VIEW WAS CREATED OR ALREADY EXISTS")
        except Exception as e:
            logging.error(f"ERROR: {e}")
            raise


    def load_to_table(self):
        try:
            with open('for_raw_data/file_json.txt', 'r') as file:
                for line in file:
                    date_now = datetime.datetime.now()
                    jsn_data = line.strip()
                    query = f"INSERT INTO raw_data  VALUES ('{date_now}', '{jsn_data}')"
                    self.connection.command(query)
                    logging.info(f"{line} INSERTED SUCCESSFULLY")
            logging.info("DATA HAS INSERTED SUCCESSFULLY")
            self.connection.command("OPTIMIZE TABLE raw_data FINAL;")
            self.connection.command("OPTIMIZE TABLE parsed_table FINAL;")
        except Exception as e:
            logging.error(f"ERROR: {e}")
            raise



def main():

   json_data()
   db = Datebase()
   db.raw_table_creation()
   db.create_parsed_table()
   db.create_materialized_view()
   db.load_to_table()



if __name__  ==  '__main__':
    main()

