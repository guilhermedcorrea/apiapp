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
            
            try:
                ValorTotal = converte_float(listas.get('ValorTotal'))
                QtdCaixa = converte_float(listas.get('QtdCaixa'))
                PrecoUnitario = converte_float(listas.get('PrecoUnitario'))
                Quantidade = converte_float(listas.get('Quantidade'))
                Desconto = converte_float(listas.get('Desconto'))
                DescontoItem = converte_float(listas.get('DescontoItem'))
                print('valor total -->',ValorTotal)
            except Exception as e:
                print(e)
            
            '''
                print(items.get('CodigoPedido'), items.get('IdCliente'),items.get('NomeCliente')
                ,items.get('SKU'),QtdCaixa,PrecoUnitario, Quantidade
                ,items.get('EAN'), items.get('NCM'),items.get('Marca'), items.get('NomeProduto'),items.get('NomeCliente')
                ,items.get('CpfCnpj'),ValorTotal,items.get('Unidade')
                ,items.get('RazaoSocialFranquiaVenda'),items.get('Bairro'),items.get('Celular')
                ,items.get('Cep'),items.get('Complemento'),items.get('Endereco')
                ,Desconto, DescontoItem,items.get('Nome'),items.get('Uf'),items.get('Numero'))
            '''   
        print('emissao notas fiscais ')
     
        url = """https://api.nfse.io/v2/companies/{}/productinvoices/""".format(kwargs.get('COMPANY_ID_EMISSAO'))
        try:
            payload = json.dumps({
            "buyer": {
                "name": f"{listas.get('NomeCliente')}","tradeName": f"{listas.get('NomeCliente')}","address": {"city": {"code": f"{listas.get('Cep')}","name": f"{listas.get('Nome')}"
                },"state": f"{listas.get('Uf')}","district": "distrito","street": f"{listas.get('Endereco')}","postalCode": f"{listas.get('Cep')}","number": f"{listas.get('Numero')}","country": "BRA"},
                "federalTaxNumber": 99999999999999
            },
            "items": [{"code": f"{listas.get('SKU')}","unitAmount": 87.9,"quantity": f"{Quantidade}","cfop": 5102, "ncm": f"{listas.get('NCM')}","codeGTIN": f"{listas.get('EAN')}",
                "codeTaxGTIN": f"{listas.get('EAN')}","tax": {"totalTax": 6,"icms": {"csosn": "102","origin": "0"},"pis": { "amount": 0,"rate": 0,"baseTax": 208,          "cst": "08"
                    },"cofins": {"amount": 0,"rate": 0,"baseTax": 208,"cst": "08"}},"cest": "","description": f"{listas.get('NomeCliente')}"
                }]})
            headers = {
            'Authorization': f"{kwargs.get('API_KEY_EMISSAO')}",
            'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            print(response.status_code)
            print(f"Nota Emitida",listas['CodigoPedido'])
        except Exception as e:
            print(f"Nota nao Emitida ",e,listas['CodigoPedido'])

        
      
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



       

        