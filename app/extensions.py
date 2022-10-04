from flask_sqlalchemy import SQLAlchemy
from apifairy import APIFairy, response, arguments, authenticate, other_responses
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
apifairy = APIFairy()
ma = Marshmallow()