from typing import Any
from flask import Blueprint, request, jsonify, make_response, Response
from functools import wraps
import os
from dotenv import load_dotenv
import requests

from typing import Dict, Tuple, List
consulta_bp = Blueprint('consultanf', __name__)
"""
NOTA FISCAL CONSUMIDOR

"""
load_dotenv()

API_KEY_CONSULTA = os.getenv('API_KEY_CONSULTA')
COMPANY_ID_CONSULTA = os.getenv('COMPANY_ID_CONSULTA')

def get_metodo(f) -> Any:
    @wraps(f)
    def obtem_endpoint(*args: tuple, **kwargs: Dict[str, Any]) -> Any:
        print('Envia requisicao NFE IO CONSULTA | METODO GET')
        url = """https://api.nfse.io/v2/companies/{}/consumerinvoices?environment={}&apikey={}""".format(kwargs.get('compani_id'),kwargs.get('ambiente_nf'),kwargs.get('api_key'))
        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.status_code)
        jsons = response.json()
 
        return jsons
        
    return obtem_endpoint

@get_metodo
def get_parametros(*args: tuple, **kwargs: Dict[str, Any]) -> None:
    """Docstring"""
    print('Called example function')


"""
Lista notas
https://nfe.io/docs/desenvolvedores/rest-api/nota-fiscal-de-consumidor-v2/#/

"""
@consulta_bp.route('/api/v1/companies/consumerinvoices/', methods=['GET','POST'])
def listas_nfs() -> Response:
    jsons = get_parametros(compani_id= COMPANY_ID_CONSULTA,ambiente_nf='test', api_key=API_KEY_CONSULTA)

    return jsonify({"NFE":jsons})

@consulta_bp.route('/api/v1/companies/consumerinvoices/<consumer_invoice_id>', methods=['GET','POST'])
def consultar_nf_id(consumer_invoice_id: str) -> Response:
    consumer_invoice_id = request.get_json()
    values = consumer_invoice_id['consumer_invoice_id']
    print(values)
    return jsonify({"Notas":values})

@consulta_bp.route('/api/v1/companies/consumerinvoices/<consumer_invoice_id>/items', methods=['GET','POST'])
def consultar_produtos_id_nf(consumer_invoice_id: str) -> Response:
    consumer_invoice_id = request.get_json()
    values = consumer_invoice_id['consumer_invoice_id']
    return jsonify({"Notas":values})

@consulta_bp.route('/api/v1/companies/consumerinvoices/<consumer_invoice_id>/events', methods=['GET','POST'])
def consultar_eventos_nf_id(consumer_invoice_id: str) -> Response:
    consumer_invoice_id = request.get_json()
    values = consumer_invoice_id['consumer_invoice_id']
    return jsonify({"Notas":values})

@consulta_bp.route('/api/v1/companies/consumerinvoices/<consumer_invoice_id>/xml', methods=['GET','POST'])
def consultar_xml_nf(consumer_invoice_id: str) -> Response:
    consumer_invoice_id = request.get_json()
    values = consumer_invoice_id['consumer_invoice_id']
    print(consumer_invoice_id)
    return jsonify({"Notas":values})

@consulta_bp.route('/api/v1/companies/consumerinvoices/<consumer_invoice_id>/rejeicao/xml', methods=['GET','POST'])
def consultar_xml_rejeicao_id(consumer_invoice_id: str) -> Response:
    consumer_invoice_id = request.get_json()
    values = consumer_invoice_id['consumer_invoice_id']
    print(values)
    return jsonify({"Notas":values})