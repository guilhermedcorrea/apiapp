from typing import Any
from flask import Blueprint, request, jsonify, make_response, Response, abort, current_app
from functools import wraps
import os
from dotenv import load_dotenv
import requests
from typing import Dict, Tuple, List, Literal
from ..extensions import db
from ..models.pedidos_hausz_mapa import PedidoFlexy
from ..models.cliente_hausz_mapa import EnderecoPedidos

from sqlalchemy import text
from datetime import datetime
from itertools import chain
from ..controllers.controllers_hausz_mapa import executa_select
from ..controllers.controllers_notas import consulta_all_notas, consulta_nfe_por_id
from itertools import groupby


def register_handlers(app):
    if current_app.config.get('DEBUG') is True:
        current_app.logger.debug('Errors')
        return

    @current_app.errorhandler(404)
    def not_found_error(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

    @current_app.errorhandler(500)
    def internal_error(error):
        return make_response(jsonify({"Error":"internal error"}), 500)
    

    @current_app.errorhandler(500)
    def ModuleNotFoundError(*args, **kwargs):
        return make_response(jsonify({"Error":"internal error"}), 500)

    @current_app.errorhandler(404)
    def page_not_found(*args, **kwargs):
        return make_response(jsonify({"Error":"Endpoint NotFound"}), 404)
   
    @current_app.errorhandler(405)
    def method_not_allowed_page(*args, **kwargs):
        return make_response(jsonify({"Error":"Endpoint NotFound"}), 405)

consulta_bp = Blueprint('consultanf', __name__)
register_handlers(current_app)

from ..controllers.controllers_notas import get_metodo, list_all_empresas

"""
NOTA FISCAL CONSUMIDOR
"""
load_dotenv()

API_KEY_EMISSAO = os.getenv('API_KEY_EMISSAO')
COMPANY_ID_EMISSAO = os.getenv('COMPANY_ID_EMISSAO')

@get_metodo
def get_parametros(*args: tuple, **kwargs: Dict[str, Any]) -> None:
    """Docstring"""
    print('Called function')

@list_all_empresas
def get_list_empresas(*args: tuple, **kwargs: Dict[str, Any]) -> None:
    print("teste")

"""
Lista notas
https://nfe.io/docs/desenvolvedores/rest-api/nota-fiscal-de-consumidor-v2/#/
"""

@consulta_bp.route('/api/v2/companies/list/empresas/all', methods=['GET','POST'])
def listas_all_empresas() -> Response:
    try:
        jsons = get_list_empresas(api_key= API_KEY_EMISSAO)
        return make_response(jsonify(jsons)), 201
    except:
        abort(400)

@consulta_bp.route('/api/v2/companies/list/nfe/all', methods=['GET','POST'])
def consulta_nf() -> Response:
    try:
        jsons = consulta_all_notas()
        return make_response(jsonify(jsons))
    except:
        abort(400)
        
@consulta_bp.route('/api/v2/companies/list/nfe/idnfe', methods=['GET','POST'])
<<<<<<< HEAD
def consulta_nfe_id() -> Response:
=======

def consulta_nfe_id():
>>>>>>> 5d3397dfbdb23ac89f5e0f807dc77c49e577763f
    try:
        id_nf  = request.get_json()
        id_nf = id_nf['IdNfe']
        jsons_nf = consulta_nfe_por_id(id_nf)
        return make_response(jsonify(jsons_nf))
    except:
<<<<<<< HEAD
        abort(400)
        
        
@consulta_bp.route('/api/v2/companies/list/nfe/list/xml',methods=['GET','POST'])
def consulta_xml_nfe() -> Response:
    data = request.get_json()
    return make_response(jsonify({"xml":"teste"})), 201


@consulta_bp.route('/api/v2/companies/list/xml/rejeicao',methods=['GET','POST'])
def get_produtos_nfe_rejeicao() -> Response:
    data = request.get_json()
    return make_response(jsonify({"rejeicao":"teste"})), 201


@consulta_bp.route('/api/v2/companies/list/nfe/list/pdf',methods=['GET','POST'])
def consulta_xml_pdf() -> Response:
    data = request.get_json()
    return make_response(jsonify({"pdf":"teste"})), 201


@consulta_bp.route('/api/v2/companies/list/nfe/items',methods=['GET','POST'])
def get_produtos_nfe() -> Response:
    data = request.get_json()
    return make_response(jsonify({"items":"teste"})), 201


@consulta_bp.route('/api/v2/companies/nfe/cartacorrecao',methods=['GET','POST'])
def carta_correcao_nfe() -> Response:
    data = request.get_json()
    return make_response(jsonify({"correcao":"teste"})), 201
    
=======
        abort(400)
>>>>>>> 5d3397dfbdb23ac89f5e0f807dc77c49e577763f
