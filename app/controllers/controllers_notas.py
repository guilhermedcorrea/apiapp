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
    @wraps(f)
    def emissao_notas_fiscais(*args: tuple, **kwargs: Dict[str, Any]) -> Any:
        if isinstance(args, tuple):
            dict_items = next(chain(args))
            for items in dict_items:
            
                try:
                    ValorTotal = next(converte_float(items.get('ValorTotal')))
                    QtdCaixa = next(converte_float(items.get('QtdCaixa')))
                    PrecoUnitario = next(converte_float(items.get('PrecoUnitario')))
                    Quantidade = next(converte_float(items.get('Quantidade')))
                    Desconto = next(converte_float(items.get('Desconto')))
                    DescontoItem = next(converte_float(items.get('DescontoItem')))
                    print('valor total -->',ValorTotal)
                except Exception as e:
                    print(e)
               
                print(items.get('CodigoPedido'), items.get('IdCliente'),items.get('NomeCliente')
                    ,items.get('SKU'),QtdCaixa,PrecoUnitario, Quantidade
                    ,items.get('EAN'), items.get('NCM'),items.get('Marca'), items.get('NomeProduto'),items.get('NomeCliente')
                    ,items.get('CpfCnpj'),ValorTotal,items.get('Unidade')
                    ,items.get('RazaoSocialFranquiaVenda'),items.get('Bairro'),items.get('Celular')
                    ,items.get('Cep'),items.get('Complemento'),items.get('Endereco')
                    ,Desconto, DescontoItem,items.get('Nome'),items.get('Uf'),items.get('Numero'))   
   
        #for arg in args:
        #    print(arg['UFranquiaVenda'])
     
                url = """https://api.nfse.io/v2/companies/{}/productinvoices/""".format(kwargs.get('COMPANY_ID_EMISSAO'))
                try:
                    payload = json.dumps({
                    "buyer": {
                        "name": f"{items.get('NomeCliente')}","tradeName": f"{items.get('NomeCliente')}","address": {"city": {"code": f"{items.get('Cep')}","name": f"{items.get('Nome')}"
                        },"state": f"{items.get('Uf')}","district": "distrito","street": f"{items.get('Endereco')}","postalCode": f"{items.get('Cep')}","number": f"{items.get('Numero')}","country": "BRA"},
                        "federalTaxNumber": ""
                    },
                    "items": [{"code": f"{items.get('SKU')}","unitAmount": f"{PrecoUnitario}","quantity": f"{Quantidade}","cfop": 5102, "ncm": f"{items.get('NCM')}","codeGTIN": f"{items.get('EAN')}",
                        "codeTaxGTIN": f"{items.get('EAN')}","tax": {"totalTax": 6,"icms": {"csosn": "102","origin": "0"},"pis": { "amount": "","rate": "","baseTax": "","cst": ""
                            },"cofins": {"amount": "","rate": "","baseTax": "","cst": "08"}},"cest": "","description": f"{items.get('NomeCliente')}"
                        }]})
                    headers = {
                    'Authorization': f"{kwargs.get('API_KEY_EMISSAO')}",
                    'Content-Type': 'application/json'
                    }

                    response = requests.request("POST", url, headers=headers, data=payload)
                    if response.status_code == 200:
                        return jsonify({"NOTAEMITIDA":items.get('CodigoPedido')})
                    else:
                        return jsonify({"error":"notanaoemitida"})
                except Exception as e:
                    abort(400)
                    #print(f"Nota nao Emitida ",e,items['CodigoPedido'])

        #return response.json()
        print(response.status_code)
    
        return  jsonify({"Value":response.status_code})
        
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


def consulta_all_notas():
    url ='https://api.nfse.io/v2/companies/acd0c1c8f5a1486592c6ed80d94e2bb7/productinvoices?environment=test&apikey=t0StUhoH4JiSN72ehwrhq3nQ27gRDTSJGt2W98rDXilRTwhNoJAiGtM9WUcl9MscjjW'

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
    
    