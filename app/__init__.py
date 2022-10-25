
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from config import SECRET_KEY, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_BINDS
from .extensions import db


#db = SQLAlchemy()

def create_app() -> Flask:
    app = Flask(__name__, template_folder='templates')
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SQLALCHEMY_POOL_SIZE'] = 370
    app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0


   
    db.init_app(app)
 
   
    with app.app_context():
        from .api.cadastra_nf import cadastro_bp
        from .api.consulta_nf import consulta_bp
        from .api.jestor import jestor_bp
        #from .admin.admin import admin_bp
        from .api.teste import testes

        app.register_blueprint(testes)
        app.register_blueprint(cadastro_bp)
        app.register_blueprint(consulta_bp)
        app.register_blueprint(jestor_bp)
 
    return app