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
        listas = []
        dict_item = (filter(lambda k: k,[jsons[x] for x in jsons]))
        for item in next(chain(dict_item)):
        
            dict_items = {
                "taxRegime":item['taxRegime'],
                "address":item['address'],
                "modifiedOn":item['modifiedOn'],
                "createdOn":item['createdOn'],
                "status":item['status'],
                "federalTaxNumber":item['federalTaxNumber'],
                "name":item['name'],
                "ID":item['id'],
                "accountId":item['accountId']}
            listas.append(dict_items)
         
        return make_response(jsonify({item['id']:listas})), 201
    except:
        abort(400)

@consulta_bp.route('/api/v2/companies/list/nfe/all', methods=['GET','POST'])
def consulta_nf() -> Response:
    
    try:
        lista_notas = []
        jsons = consulta_all_notas()
        dicts = [item for item in jsons['productInvoices']]
        for i in range(len(dicts)):
            dicts_nfs = {}
            dicts_nfs['serie'] = dicts[i]['serie'] 
            dicts_nfs['number'] = dicts[i]['number']
            dicts_nfs['issuer'] = dicts[i]['issuer']
            dicts_nfs['buyer'] = dicts[i]['buyer']
            dicts_nfs['totals'] = dicts[i]['totals']
            lista_notas.append({dicts[i]['number']:dicts_nfs})
    
        return make_response(jsonify(lista_notas))
    except:
        abort(400)


@consulta_bp.route('/api/v2/companies/list/nfe/idnfe', methods=['GET','POST'])
def retorna_nfe_id():
    pass

@consulta_bp.route('/api/v2/companies/list/nfe/xml/all', methods=['GET','POST'])
def retorna_all_xml():
    pass

@consulta_bp.route('/api/v2/companies/list/nfe/pdf/all', methods=['GET','POST'])
def retorna_all_pdf():
    pass

@consulta_bp.route('/api/v2/companies/list/nfe/pdf/idnf', methods=['GET','POST'])
def retorna_pdf_id_nf():
    pass


@consulta_bp.route('/api/v2/companies/list/nfe/xml/idxml', methods=['GET','POST'])
def retorna_xml_id_nf():
    pass