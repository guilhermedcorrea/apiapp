
from flask import Flask
from config import SQLALCHEMY_DATABASE_URI
import os
from .extensions import db, apifairy, ma

from flask_sqlalchemy import SQLAlchemy

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.getenv('UID'),
            SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI,
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            APIFAIRY_TITLE = 'Integração HauszJestor',
            APIFAIRY_VERSION = 'v1.0',
            APIFAIRY_UI = 'swagger_ui',


        )
    else:
        app.config.from_mapping(test_config)

    db.init_app(app)
    apifairy.init_app(app)
    ma.init_app(app)


    from .api.api_notas_compras import nfcompras_bp
  
    with app.app_context():
    
        app.register_blueprint(nfcompras_bp)
 
    return app