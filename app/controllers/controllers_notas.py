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

def emissao_nfe(f) -> Any:
    @wraps(f)
    def emissao_notas_fiscais(*args: tuple, **kwargs: Dict[str, Any]) -> Any:
        for listas in args:
            for items in listas:
                ValorTotal = converte_float(items.get('ValorTotal'))
                QtdCaixa = converte_float(items.get('QtdCaixa'))
                PrecoUnitario = converte_float(items.get('PrecoUnitario'))
                Quantidade = converte_float(items.get('Quantidade'))
                Desconto = converte_float(items.get('Desconto'))
                DescontoItem = converte_float(items.get('DescontoItem'))

                print('valor total -->',ValorTotal)
                print(items.get('CodigoPedido'), items.get('IdCliente'),items.get('NomeCliente')
                ,items.get('SKU'),QtdCaixa,PrecoUnitario, Quantidade
                ,items.get('EAN'), items.get('NCM'),items.get('Marca'), items.get('NomeProduto'),items.get('NomeCliente')
                ,items.get('CpfCnpj'),ValorTotal,items.get('Unidade')
                ,items.get('RazaoSocialFranquiaVenda'),items.get('Bairro'),items.get('Celular')
                ,items.get('Cep'),items.get('Complemento'),items.get('Endereco')
                ,Desconto, DescontoItem,items.get('Nome'),items.get('Uf'),items.get('Numero'))
                    
        print('emissao notas fiscais ')
     
        url = """https://api.nfse.io/v2/companies/{}/productinvoices/""".format(kwargs.get('COMPANY_ID_EMISSAO'))

        payload = json.dumps({
        "buyer": {
            "name": f"{items.get('NomeCliente')}","tradeName": f"{items.get('NomeCliente')}","address": {"city": {"code": f"{items.get('Cep')}","name": f"{items.get('Nome')}"
            },"state": f"{items.get('Uf')}","district": "distrito","street": f"{items.get('Endereco')}","postalCode": f"{items.get('Cep')}","number": f"{items.get('Numero')}","country": "BRA"},
            "federalTaxNumber": 99999999999999
        },
        "items": [{"code": f"{items.get('SKU')}","unitAmount": 87.9,"quantity": f"{Quantidade}","cfop": 5102, "ncm": f"{items.get('NCM')}","codeGTIN": f"{items.get('EAN')}",
            "codeTaxGTIN": f"{items.get('EAN')}","tax": {"totalTax": 6,"icms": {"csosn": "102","origin": "0"},"pis": { "amount": 0,"rate": 0,"baseTax": 208,          "cst": "08"
                },"cofins": {"amount": 0,"rate": 0,"baseTax": 208,"cst": "08"}},"cest": "","description": f"{items.get('NomeCliente')}"
            }]})
        headers = {
        'Authorization': f"{kwargs.get('API_KEY_EMISSAO')}",
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.status_code)
      
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



       

        