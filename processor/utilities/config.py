import configparser

config_path = "config.ini"
config = configparser.ConfigParser()
config.read(config_path)
db_host = config["DEFAULT"]["DB_HOST"]
db_port = config["DEFAULT"]["DB_PORT"]
db_user = config["DEFAULT"]["DB_USER"]
db_password = config["DEFAULT"]["DB_PASSWORD"]
db_name = config["DEFAULT"]["DB_NAME"]
additional_event_table = config["DEFAULT"]["ADDITIONAL_EVENT_TABLE"]
db_driver = config["DEFAULT"]["DB_DRIVER"]
db_mysql_url = f"jdbc:mysql://{db_host}:{db_port}/{db_name}"
db_final_table = config["DEFAULT"]["DB_FINAL_TABLE"]

