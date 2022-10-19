
from flask import Flask
from config import SQLALCHEMY_DATABASE_URI
import os
from .extensions import db, ma
from flask import make_response, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def page_not_found(e):
  return make_response(jsonify({'error': 'Not found'}), 404)

def create_app(test_config=None) -> Flask:

    app = Flask(__name__, instance_relative_config=True)
    app.register_error_handler(404, page_not_found)
    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.getenv('UID'),
            SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI,
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
           
        )
    else:
        app.config.from_mapping(test_config)

    db.init_app(app)
    from .api.cadastra_nf import cadastro_bp
    from .api.consulta_nf import consulta_bp
    from .api.jestor import jestor_bp

    with app.app_context():
      
        app.register_blueprint(cadastro_bp)
        app.register_blueprint(consulta_bp)
        app.register_blueprint(jestor_bp)
 
    return app