
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from config import SECRET_KEY, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_BINDS
from .extensions import db


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
        """BluePrints
        Diretorios onde estao os endpoints 
        referentes ao cadastro, consulta e tela de importação de arquivos
        
        """
        #Não mover esses imports para cima ou causara erro de contexto ou importação circular
        from .api.cadastra_nf import cadastro_bp
        from .api.consulta_nf import consulta_bp
        from .api.jestor import jestor_bp
        from .admin.hausz_admin import admin_bp


        app.register_blueprint(cadastro_bp)
        app.register_blueprint(consulta_bp)
        app.register_blueprint(jestor_bp)
        app.register_blueprint(admin_bp)
        
 
    return app