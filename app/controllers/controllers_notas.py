from functools import wraps
import os
from dotenv import load_dotenv
import requests
import json
from typing import Dict, Tuple, List, Literal, Any
from ..extensions import db
from itertools import groupby, chain
from sqlalchemy import text

"""
NOTA FISCAL CONSUMIDOR

"""
load_dotenv()

API_KEY_EMISSAO = os.getenv('API_KEY_EMISSAO')
COMPANY_ID_EMISSAO = os.getenv('COMPANY_ID_EMISSAO')


def converte_float(valores):
    try:
        num = str(valores).replace("."
                ,"").replace(",",".").strip()
        return round(float(num),2)
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


def cadastrar_nfe(*args:tuple, **kwargs:dict[str, Any]) -> int:
    url = "https://api.nfse.io/v2/companies/acd0c1c8f5a1486592c6ed80d94e2bb7/productinvoices/"

    payload = json.dumps({"buyer": {"name": f"{kwargs.get('name_cliente')}","tradeName": "Comprador Nome Comercial",
        "address": {"city": {"code": "1504018","name": f"{kwargs.get('name_city')}"},"state": "SP","district": "distrito",
        "street": f"{kwargs.get('street')}","postalCode": f"{kwargs.get('postalCode')}","number": f"{kwargs.get('postalCode')}",
        "country": "BRA"},"federalTaxNumber": 99999999999999
    },"items": kwargs.get('items')})
    headers = {
    'Authorization': 't0StUhoH4JiSN72ehwrhq3nQ27gRDTSJGt2W98rDXilRTwhNoJAiGtM9WUcl9MscjjW',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    response.status_code
    return response.status_code


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



       

        