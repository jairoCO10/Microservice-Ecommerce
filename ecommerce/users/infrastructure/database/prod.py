import os
from dotenv import load_dotenv


load_dotenv(".env.prod")


SERVER_TYPE = os.getenv("SERVER_TYPE")
LIBRARY_SERVER = os.getenv("LIBRARY_SERVER")
SQL_USER = os.getenv("SQLUSER")
SQL_PASSWORD = os.getenv("PASSWORD")
SQL_SERVER = os.getenv("HOST")
SQL_PORT = os.getenv("PORTSQL")
SQL_DB = os.getenv("DATABASE")
