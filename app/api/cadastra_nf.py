from flask import Blueprint,make_response, request
from ..extensions import db
from sqlalchemy import text
from itertools import groupby, chain
import os
from dotenv import load_dotenv
from flask import jsonify
import json
from typing import Generator, Any
from collections import defaultdict, ChainMap
from operator import itemgetter
from ..controllers.controllers_notas import emissao_nfe
from ..controllers.controllers_hausz import get_pedidos_flexy
from .omie_api import get_nota_saida_omie

cadastronota_bp = Blueprint('teste', __name__)


def key_func(k):
    
    return k['CodigoPedido']

load_dotenv()

API_KEY_EMISSAO = os.getenv('API_KEY_EMISSAO')
COMPANY_ID_EMISSAO = os.getenv('COMPANY_ID_EMISSAO')


    
def ajuste_dict(pedido: Any, nota: Any) -> Generator[dict, None, None]:
    jsons = next(get_nota_saida_omie(int(nota)))

    dict = {}
    try:
        det = jsons['det']
    except Exception as e:

        det['notfound']
        
    try:
        total = jsons['total']
    except Exception as e:
        print(e)
    try:
        info = jsons['info']
    except Exception as e:
        info['notfound']
    try:
        compl = jsons['compl']
    except Exception as e:
        compl['notfound']
    titulos = jsons['titulos']

    dict.update(det[0])
    dict.update(total['ICMSTot'])
    dict.update(info)
    dict.update(compl)
    dict.update(titulos[0])
    new_dict = {k:v for k,v in dict.items()}
    new_dict.get('nfProdInt')
    #print(new_dict.get('prod'))
    dict_p = {}
    new_dict.get('nfProdInt')
    dict_p.update(new_dict.get('nfProdInt'))
    new_dict.get('prod')
    dict_p.update(new_dict.get('prod'))
    yield dict_p
   

@cadastronota_bp.route('/testenota', methods=['GET','POST'])
def cadastra_nota_teste() -> Any:
    with db.engine.connect() as conn:
        data = request.get_json()
        ref_pedido = data['CodigoPedido']

        with db.engine.begin() as conn:

            try:
                exec = (text( """ProdutosTax @codigopedido = {}""".format(ref_pedido)))
                exec_produtos = conn.execute(exec)

            except:

                print('erro')

        query_dicts = [{key: value for (key, value) in row.items()} for row in exec_produtos]
        jsons = next(chain(query_dicts))
        jsons_nf = next(ajuste_dict(jsons['NumeroNF'], jsons['CodigoPedido']))
        newjs = next(get_pedidos_flexy(pedido = jsons['CodigoPedido']))
        jsons.update(newjs[0])
        
        listas = []
        produto_dicts = ChainMap(jsons, jsons_nf)
   
        listas.append({k:v for k,v in produto_dicts.items()})
        INFO = sorted(listas, key=key_func)
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
                buyer['CFOP'] = lista[i]['CFOP']
                buyer['vBCST'] = lista[i]['vBCST']
                buyer['cOrigem'] = lista[i]['cOrigem']
                
                    
                new_item = {"code": f"{lista[i]['SKU']}","unitAmount": float(lista[i]['PrecoUnitario']), "quantity": float(lista[i]['Quantidade'])
                    ,"cfop": f"{lista[i]['CFOP']}","ncm": f"{lista[i]['NCM']}",
                    "codeGTIN": f"{lista[i]['EAN']}","codeTaxGTIN": f"{lista[i]['EAN']}", "tax": {"totalTax": 6, "icms": {
                    "csosn": "102","origin": f"{lista[i]['cOrigem']}"},"pis": {"amount": 0,"rate": 0,"baseTax": 208,"cst": f"{lista[i]['vBCST']}" },
                    "cofins": {"amount": 0,"rate": 0,"baseTax": 208,"cst": "08"}},"cest": "",
                    "description": f"{lista[i].get('NomeProduto')}"}
                  
                lista_item.append(new_item)
                   
            jsons = emissao_nfe(items = lista_item, name_cliente=buyer.get('namecliente'), tradeName=buyer.get('tradeName'),code=buyer.get('code')
                ,name_city=buyer.get('name'),street=buyer.get('street'),number=buyer.get('number')
                    ,postalCode=buyer.get('postalCode'),description=buyer.get('description'),id=buyer.get('CodigoPedido'))
       
        return make_response(jsonify({"NotaFiscal":"Criada Com Sucesso"
        ,"Status":200,"Pedido":buyer['CodigoPedido'],"Cliente":buyer['namecliente'],"item":jsons})),201