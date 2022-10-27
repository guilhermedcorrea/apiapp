from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask_marshmallow import Marshmallow

db = SQLAlchemy()

ma = Marshmallow()