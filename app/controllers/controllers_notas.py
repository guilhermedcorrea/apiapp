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
        return float(num)
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
    @wraps(f)
    def emissao_notas_fiscais(*args: tuple, **kwargs: Dict[str, Any]) -> Any:
        for listas in args:
            for items in listas:
                print(items.get('CodigoPedido'), items.get('IdCliente'),items.get('NomeCliente')
                ,items.get('SKU'),items.get('QtdCaixa'),items.get('PrecoUnitario'), items.get('Quantidade')
                ,items.get('EAN'), items.get('NCM'),items.get('Marca'), items.get('NomeProduto'),items.get('NomeCliente')
                ,items.get('CpfCnpj'),items.get('ValorTotal'),items.get('Unidade')
                ,items.get('RazaoSocialFranquiaVenda'),items.get('Bairro'),items.get('Celular')
                ,items.get('Cep'),items.get('Complemento'),items.get('Endereco')
                ,items.get('Desconto'), items.get('DescontoItem'),items.get('Nome'),items.get('Uf'))
                        
        print('emissao notas fiscais ')
        '''
        url = """https://api.nfse.io/v2/companies/{COMPANY_ID_EMISSAO}/productinvoices/""".format(COMPANY_ID_EMISSAO)

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
        'Authorization': f'{API_KEY_EMISSAO}',
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.status_code)
        '''
        #return response.json()
        return 'teste'
        
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



       

        