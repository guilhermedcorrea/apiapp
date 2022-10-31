

from functools import wraps
import os
from dotenv import load_dotenv
from flask import jsonify
import requests
import json
from typing import Dict, Tuple, List, Literal, Any
from ..extensions import db
from itertools import groupby, chain
from sqlalchemy import text
from flask import current_app, make_response, abort

"""
NOTA FISCAL CONSUMIDOR
"""
load_dotenv()

API_KEY_EMISSAO = os.getenv('API_KEY_EMISSAO')
COMPANY_ID_EMISSAO = os.getenv('COMPANY_ID_EMISSAO')


@current_app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

def converte_float(valores):
    try:
        num = str(valores).replace("."
                ,"").replace(",",".").strip()
        yield round(float(num),2)
    except:
        return float(0)

def get_metodo(f) -> Any:
    @wraps(f)
    def obtem_endpoint(*args: tuple, **kwargs: Dict[str, Any]) -> Any:
        print('Envia requisicao NFE IO CONSULTA | METODO GET')

        '''
        url = """https://api.nfse.io/v2/companies/{}/productinvoices?environment=production&apikey={}""".format(kwargs.get('compani_id'), kwargs.get('api_key'))
        payload={}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.status_code)
        jsons = response.json()
        '''
        #return jsons
        return (kwargs.get('CodigoPedido'))
    return obtem_endpoint


def emissao_nfe(f) -> Any:
    """Emissão notas fiscais produto"""
    @wraps(f)
    def emissao_notas_fiscais(*args: tuple, **kwargs: Dict[str, Any]) -> Any:
        if isinstance(args, tuple):
            dict_items = next(chain(args))
            for items in dict_items:
            
                url = """https://api.nfse.io/v2/companies/{}/productinvoices/""".format(os.getenv('COMPANY_ID_EMISSAO'))

                payload = json.dumps({"buyer": {"name": f"{items.get('name_cliente')}","tradeName": "Comprador Nome Comercial",
                    "address": {"city": {"code": "1504018","name": f"{items.get('name_city')}"},"state": "SP","district": "distrito",
                    "street": f"{items.get('street')}","postalCode": f"{items.get('postalCode')}","number": f"{items.get('postalCode')}",
                    "country": "BRA"},"federalTaxNumber": 99999999999999
                },"items": items.get('items')})
                headers = {
                'Authorization': 't0StUhoH4JiSN72ehwrhq3nQ27gRDTSJGt2W98rDXilRTwhNoJAiGtM9WUcl9MscjjW',
                'Content-Type': 'application/json'
                }

                response = requests.request("POST", url, headers=headers, data=payload)

                response.status_code
                return response.status_code
        
    return emissao_notas_fiscais

@get_metodo
def get_parametros(*args: tuple, **kwargs: Dict[str, Any]) -> None:
    """Docstring"""
    print('Called function')


def list_all_empresas(f) -> Any:
    @wraps(f)
    def obtem_endpoint(*args: tuple, **kwargs: Dict[str, Any]) -> Any:

        print('Envia requisicao NFE IO CONSULTA | METODO GET')
      

        url = "https://api.nfse.io/v2/companies?apikey={}".format(kwargs.get('api_key'))


        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.status_code)
        jsons = response.json()

        return jsons
        
    return obtem_endpoint


def listar_xml_nfs_emitidas():
    url = "https://api.nfse.io/v2/companies/acd0c1c8f5a1486592c6ed80d94e2bb7/productinvoices/xml?environment=test&apikey=t0StUhoH4JiSN72ehwrhq3nQ27gRDTSJGt2W98rDXilRTwhNoJAiGtM9WUcl9MscjjW"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()
 


def lista_produtos_nfe(refproduto):
    url = """https://api.nfse.io/v2/companies/acd0c1c8f5a1486592c6ed80d94e2bb7/productinvoices/{}/items?apikey=t0StUhoH4JiSN72ehwrhq3nQ27gRDTSJGt2W98rDXilRTwhNoJAiGtM9WUcl9MscjjW""".format(refproduto)

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()


def consulta_all_notas():
    url =f'https://api.nfse.io/v2/companies/acd0c1c8f5a1486592c6ed80d94e2bb7/productinvoices?environment=test&apikey=t0StUhoH4JiSN72ehwrhq3nQ27gRDTSJGt2W98rDXilRTwhNoJAiGtM9WUcl9MscjjW'

    payload = []
    headers = []
    
    response = requests.request("GET", url, headers=headers, data=payload)
 
    jsons = response.json()
    return jsons


def consulta_nfe_por_id(idnfe):
    url = """https://api.nfse.io/v2/companies/acd0c1c8f5a1486592c6ed80d94e2bb7/productinvoices/{}/events?apikey=t0StUhoH4JiSN72ehwrhq3nQ27gRDTSJGt2W98rDXilRTwhNoJAiGtM9WUcl9MscjjW""".format(idnfe)

    payload = {}
    headers = {}
    
    response = requests.request('GET', url, headers=headers, data=payload)
    return response.json()
    