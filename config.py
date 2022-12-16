import urllib
import pyodbc
import os
from urllib.parse import quote_plus
from urllib import parse
from dotenv import load_dotenv
from os import path

load_dotenv()
driver = os.getenv('driver')
server = os.getenv('Server')
database = os.getenv('Database')
usuario = os.getenv('UID')
password = os.getenv('PWD')
basedir = path.abspath(path.dirname(__file__))



load_dotenv(path.join(basedir, '.env'))



#basedir = os.path.abspath(os.path.dirname(__file__))


UPLOADFOLDER = join_path = os.path.join(
            os.path.abspath(os.path.join(
                os.path.dirname(__file__)
                , os.path.pardir)))


TEMPLATE_FOLDER = os.path.abspath(os.path.dirname(__file__)) 

paramsdev = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};"
                                 "SERVER=f"{server};"
                                 "DATABASE=f"{database}"
                                 "UID=f"{usuario}"
                                 "PWD=f"{password}")

params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};"
                                  "SERVER=f"{server};"
                                 "DATABASE=f"{database}"
                                 "UID=f"{usuario}"
                                 "PWD=f"{password}")

SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'


SQLALCHEMY_DATABASE_URI= ("mssql+pyodbc:///?odbc_connect=%s" % params)

SQLALCHEMY_BINDS = {
    "HauszMapaDev2": ("mssql+pyodbc:///?odbc_connect=%s" %paramsdev),
    "HauszMapa": ("mssql+pyodbc:///?odbc_connect=%s" %params)
}
