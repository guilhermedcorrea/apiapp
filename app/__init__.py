
from flask import Flask
from config import SQLALCHEMY_DATABASE_URI
import os
from .extensions import db, ma

from flask_sqlalchemy import SQLAlchemy

def create_app(test_config=None) -> Flask:

    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.getenv('UID'),
            SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI,
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
           
        )
    else:
        app.config.from_mapping(test_config)

 
    from .api.cadastra_nf import cadastro_bp
    from .api.consulta_nf import consulta_bp
    from .api.jestor import jestor_bp

    with app.app_context():
      
        app.register_blueprint(cadastro_bp)
        app.register_blueprint(consulta_bp)
        app.register_blueprint(jestor_bp)
 
    return app