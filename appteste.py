
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
import urllib
import pyodbc
import os
from urllib.parse import quote_plus
from urllib import parse
from dotenv import load_dotenv
from os import path
from sqlalchemy import text
from urllib.parse import urlencode, quote_plus


app = Flask(__name__)

params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};"
                                 "SERVER=w2019.hausz.com.br;"
                                 "DATABASE=HauszMapa;"
                                 "UID=Aplicacao.Guilherme;"
                                 "PWD=4PL1C4ÇAO_3STOQUF202#")



SQLALCHEMY_DATABASE_URI= ("mssql+pyodbc:///?odbc_connect=%s" % params)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
