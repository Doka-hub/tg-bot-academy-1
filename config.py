import os

from dotenv import load_dotenv

load_dotenv()

# MYSQL
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_HOST = os.getenv('MYSQL_HOST')

# TG BOT
TOKEN = os.getenv('TOKEN')
