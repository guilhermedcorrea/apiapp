from functools import wraps
import os
from dotenv import load_dotenv
import requests
import json
from typing import Dict, Tuple, List, Any

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
    @wraps(f)
    def emissao_notas_fiscais(*args: tuple, **kwargs: Dict[str, Any]) -> Any:

        print('emissao notas fiscais ')

        url = "https://api.nfse.io/v2/companies/acd0c1c8f5a1486592c6ed80d94e2bb7/productinvoices/"

        payload = json.dumps({
        "buyer": {
            "name": "Teste NF TESTE","tradeName": "Comprador Nome Comercial","address": {"city": {"code": "1751488","name": "Marilia"
            },"state": "SP","district": "distrito","street": "Alameda Madri","postalCode": "1751488","number": "555","country": "BRA"},
            "federalTaxNumber": 99999999999999
        },
        "items": [{"code": "20968A","unitAmount": 87.9,"quantity": 33.9,"cfop": 5102, "ncm": "69072100","codeGTIN": "7894287914364",
            "codeTaxGTIN": "7894287914364","tax": {"totalTax": 6,"icms": {"csosn": "102","origin": "0"},"pis": { "amount": 0,"rate": 0,"baseTax": 208,          "cst": "08"
                },"cofins": {"amount": 0,"rate": 0,"baseTax": 208,"cst": "08"}},"cest": "","description": "TESTE DE PRODUTO - WITMOB"
            }]})
        headers = {
        'Authorization': 't0StUhoH4JiSN72ehwrhq3nQ27gRDTSJGt2W98rDXilRTwhNoJAiGtM9WUcl9MscjjW',
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.status_code)
 
        return response.json()
        
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




class NotasHausz:
    def __init__(self, pedido, data, unidade, nf):
        self.pedido = pedido
        self.data = data
        self.unidade = unidade
        self.lista_dicts = []

    def seleciona_fields(self, *args: tuple, **kwargs: dict[str, Any]) -> dict[str, Any]:pass

    def get_jsons_api(self): pass

    def emissao_nf(self) -> None: pass

       

        