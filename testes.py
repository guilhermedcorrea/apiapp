from flask import Blueprint,make_response
from ..extensions import db
from sqlalchemy import text
from itertools import groupby, chain
import requests
import json
import os
from dotenv import load_dotenv
from flask import jsonify
testes = Blueprint('teste', __name__)



def key_func(k):
    return k['CodigoPedido']



load_dotenv()

API_KEY_EMISSAO = os.getenv('API_KEY_EMISSAO')
COMPANY_ID_EMISSAO = os.getenv('COMPANY_ID_EMISSAO')


def cadastrar_nfe(*args, **kwargs):
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
  
@testes.route("/testes", methods=['GET','POST'])
def teste():
    
    '''
    cidade_pv =  dict_pedidos['buyer']['address']

    pv_produto = dict_pedidos['items'][0]
    tax = dict_pedidos['items'][0]['tax']
    '''

    with db.engine.connect() as conn:
            query = (text("""SELECT *FROM [HauszMapa].[Pedidos].[ItensFlexy] as iflexy
                JOIN [HauszMapa].[Pedidos].[PedidoFlexy] as pflexy
                ON iflexy.CodigoPedido = pflexy.CodigoPedido
                JOIN [HauszMapa].[Produtos].[ProdutoBasico] as pbasico
                ON pbasico.SKU = iflexy.SKU
                JOIN [HauszLogin].[Cadastro].[Cliente] as cliente
                ON cliente.IdCliente = pflexy.IdCliente
                JOIN [HauszMapa].[Pedidos].[EnderecoPedidos] as epedido
                ON epedido.IdCliente = cliente.IdCliente
                JOIN [HauszLogin].[Cadastro].[Cidade] as cidade
                ON cidade.IdCidade = epedido.IdCidade
                JOIN [HauszLogin].[Cadastro].[Estado] as estado
                ON estado.IdEstado = cidade.IdEstado
                WHERE iflexy.CodigoPedido = 70829 """))
                     
            teste = conn.execute(query).all()
            query_dicts = [{key: value for (key, value) in row.items()} for row in teste]
            INFO = sorted(query_dicts, key=key_func)
            lista_values = []
            lista_item = []
            buyer = {}
            for key, value in groupby(INFO, key_func):
                lista = list(value)

                for i in range(len(lista)):

                    buyer['namecliente'] = lista[i].get('NomeCliente')
                    buyer['tradeName'] = lista[0].get('NomeCliente')
                    buyer['code'] = lista[i].get('Cep')
                    buyer['name'] = lista[i].get('Nome')
                    buyer['street'] = lista[i].get('Endereco')
                    buyer['number'] = lista[i].get('Numero')
                    buyer['postalCode'] = lista[i].get('Cep')
                    buyer['description'] = lista[i]['CodigoPedido']
                    buyer['CodigoPedido'] = lista[i]['CodigoPedido']

                  
                    new_item = {"code": f"{lista[i]['SKU']}","unitAmount": float(lista[i]['PrecoUnitario']), "quantity": float(lista[i]['Quantidade'])
                    ,"cfop": 5102,"ncm": f"{lista[i]['NCM']}",
                    "codeGTIN": f"{lista[i]['EAN']}","codeTaxGTIN": f"{lista[i]['EAN']}", "tax": {"totalTax": 6, "icms": {
                    "csosn": "102","origin": "0"},"pis": {"amount": 0,"rate": 0,"baseTax": 208,"cst": "08" },
                    "cofins": {"amount": 0,"rate": 0,"baseTax": 208,"cst": "08"}},"cest": "",
                    "description": f"{lista[i].get('NomeProduto')}"}
    
                    
                    lista_item.append(new_item)
                
            jsons = cadastrar_nfe(items = lista_item, name_cliente=buyer.get('namecliente'), tradeName=buyer.get('tradeName'),code=buyer.get('code')
                ,name_city=buyer.get('name'),street=buyer.get('street'),number=buyer.get('number')
                    ,postalCode=buyer.get('postalCode'),description=buyer.get('description'),id=buyer.get('CodigoPedido'))

         
                 
    return make_response(jsonify({"NotaFiscal":"Criada Com Sucesso"
        ,"Status":200,"Pedido":buyer['CodigoPedido'],"Cliente":buyer['namecliente'],"item":jsons})),201