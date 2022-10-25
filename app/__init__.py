
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from config import SECRET_KEY, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_BINDS
from .extensions import db


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SQLALCHEMY_POOL_SIZE'] = 370
    app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0

    db.init_app(app)
 
    with app.app_context():
        """BluePrints
        Diretorios onde estao os endpoints 
        referentes ao cadastro, consulta e tela de importação de arquivos
        
        """
   
        from .api.newteste import cadastronota_bp
        from .api.consulta_nf import consulta_bp
        app.register_blueprint(consulta_bp)
        

        app.register_blueprint(cadastronota_bp)
      
        
 
    return app