from typing import Any
from flask import Blueprint, request, jsonify, make_response, Response, abort, current_app
from functools import wraps
import os
from dotenv import load_dotenv
import requests
from typing import Dict, Tuple, List, Literal
from ..extensions import db, ma
from ..models.pedidos_hausz_mapa import PedidoFlexy
from ..models.cliente_hausz_mapa import EnderecoPedidos
from apifairy import response, other_responses, body, arguments, authenticate
from sqlalchemy import text
from datetime import datetime
from itertools import chain
from ..controllers.controllers_notas import consulta_all_notas, consulta_nfe_por_id, listar_xml_nfs_emitidas, lista_produtos_nfe
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

class ListCompaniesAll(ma.Schema):
    ID = ma.Int()
    taxRegime = ma.Str()
    address = ma.Str()
    modifiedOn = ma.Str()
    createdOn = ma.Str()
    status = ma.Str()
    federalTaxNumber = ma.Str()
    name = ma.Str()
    accountId = ma.Str()
    

@consulta_bp.route('/api/v2/companies/list/empresas/all', methods=['GET'])
@response(ListCompaniesAll, 201)
def listas_all_empresas() -> Response:
    """Retorna lista de empresas cadastradas"""
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

class CompaniesListNfeAll(ma.Schema):
    serie = ma.Str()
    number = ma.Str()
    issuer = ma.Str()
    buyer = ma.Str()
    totals = ma.Str()
    

@consulta_bp.route('/api/v2/companies/list/nfe/all', methods=['GET','POST'])
@response(CompaniesListNfeAll, 201)
def consulta_nf() -> Response:
    """Retorna todas as notas fiscais emitidas"""
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
        
'''
[{'companyId': 'acd0c1c8f5a1486592c6ed80d94e2bb7',
'id': '223b5879af86407485ed8efd4f929f9f', 'taxUnitAmount': 9.98,
'quantityTax': 5.0, 'totalAmount': 49.9, 'unitAmount': 9.98, 'quantity': 5.0, 
'totalIndicator': True, 'cfop': 5102, 'tax': {'totalTax': 6.0,
'icms': {'baseTaxFCPSTAmount': 0.0, 'fcpstRetAmount': 0.0, 'fcpstRetRate': 0.0, 
'fcpstAmount': 0.0, 'fcpstRate': 0.0, 'snCreditAmount': 0.0, 'snCreditRate': 0.0,
'csosn': '102', 'origin': '0'}, 'pis': {'amount': 0.0, 'rate': 0.0, 'baseTax': 208.0, 'cst': '08'}, 'cofins': {'amount': 0.0, 'rate': 0.0, 'baseTax': 208.0, 'cst': '08'}}, 'cest': '', 'unitTax': 'UN', 'unit': 'UN', 'ncm': '47079000',
'description': 'TESTE DE PRODUTO - WITMOB', 'codeGTIN': 'SEM GTIN', 'code': '001'}]


'''      
class CompaniesListProdutosNfe(ma.Schema):
    id = ma.Str()
    companyId = ma.Str()
  
@consulta_bp.route('/api/v2/companies/list/produtos/nfe', methods=['GET','POST'])
def retorna_produtos_nfe():
    idnota = request.get_json()
    ref_nota = idnota['IdNota']
    lista_dicts = []
    jsons = lista_produtos_nfe(ref_nota)
    print(jsons)
    for keys in jsons.get('items'):
        dicts = {}
        dicts['companyId'] = jsons.get('companyId')
        dicts['id'] = jsons.get('id')
        dicts.update(keys)
        lista_dicts.append(dicts)
    
    return make_response(jsonify(lista_dicts)), 201
       
    


@consulta_bp.route('/api/v2/companies/list/nfe/idnfe', methods=['GET','POST'])
def retorna_nfe_id():
    pass


@consulta_bp.route('/api/v2/companies/list/nfe/xml/all', methods=['GET','POST'])
def retorna_all_xml():
    """Retorna lista de todos xmls de nfs emitidas"""
    jsons = listar_xml_nfs_emitidas()
    return make_response(jsonify(jsons))
 

@consulta_bp.route('/api/v2/companies/list/nfe/pdf/all', methods=['GET','POST'])
def retorna_all_pdf():
    pass

@consulta_bp.route('/api/v2/companies/list/nfe/pdf/idnf', methods=['GET','POST'])
def retorna_pdf_id_nf():
    pass

@consulta_bp.route('/api/v2/companies/list/nfe/xml/idxml', methods=['GET','POST'])
def retorna_xml_id_nf():
    pass