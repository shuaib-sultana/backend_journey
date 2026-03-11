"""
Docstring for app.config:\n
config file for setting of the app and database .\n
It make it easy to change the database server or setting of any model of app .
"""
from app.password import DB_pass

class Config_db:
  '''
  Class for defintion the db setting.
  '''
  DB_user="root"
  DB_host="localhost"
  DB_name="users"
  DB_password=DB_pass

def get_db_config():
  '''
  Function to get the setting of database server for connection .
  \n\n
  return :
  setting of database as dictionary
  '''
  return {
    "user":Config_db.DB_user,
    "host":Config_db.DB_host,
    "password":Config_db.DB_password,
    "database":Config_db.DB_name,
  }

