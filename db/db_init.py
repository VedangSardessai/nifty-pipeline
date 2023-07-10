from dotenv import dotenv_values
import psycopg2

env_vars = dotenv_values('.env')
username = env_vars['USERNAME']
password = env_vars['PASSWORD']
database_name = env_vars['DBNAME']
port = env_vars['PORT']

# Database connection details
db_host = 'localhost'
db_port = port
db_name = database_name
db_user = username
db_password = password

conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    database=db_name,
    user=db_user,
    password=db_password
)
