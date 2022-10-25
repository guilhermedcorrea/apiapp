<<<<<<< HEAD

from errno import EDEADLK
=======
>>>>>>> 05a4405b5ab28accf03a72fde75913ef0f3a3298
from flask import (Blueprint, Request, jsonify
    , make_response, Response, redirect, current_app, request,abort)
from flask_marshmallow import Marshmallow
from sqlalchemy import text
from itertools import chain


from ..controllers.controllers_notas import cadastrar_nfe
from ..models.pedidos_hausz_mapa import ItensFlexy, PedidoFlexy
from ..models.cliente_hausz_mapa import Cidade,Estado, EnderecoPedidos
import os
from dotenv import load_dotenv
import json
from typing import Dict, Tuple, List, Literal, Any
from ..controllers.controllers_hausz_mapa import executa_select

from ..extensions import db
from itertools import groupby
from sqlalchemy import select
from datetime import datetime, date, timedelta



def register_handlers(app):
    if current_app.config.get('DEBUG') is True:
        current_app.logger.debug('Errors')
        return

    @current_app.errorhandler(404)
    def not_found_error(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

    @current_app.errorhandler(500)
    def internal_error(error):
        return make_response(jsonify({"Error":"internal error"}), 500)
    

    @current_app.errorhandler(500)
    def ModuleNotFoundError(*args, **kwargs):
        return make_response(jsonify({"Error":"internal error"}), 500)

    @current_app.errorhandler(404)
    def page_not_found(*args, **kwargs):
        return make_response(jsonify({"Error":"Endpoint NotFound"}), 404)
   
    @current_app.errorhandler(405)
    def method_not_allowed_page(*args, **kwargs):
        return make_response(jsonify({"Error":"Endpoint NotFound"}), 405)

cadastro_bp = Blueprint('cadastronf', __name__)
#Handlers
register_handlers(current_app)


load_dotenv()

API_KEY_EMISSAO = os.getenv('API_KEY_EMISSAO')
COMPANY_ID_EMISSAO = os.getenv('COMPANY_ID_EMISSAO')

"""
Emissao notas ficais
https://nfe.io/docs/desenvolvedores/rest-api/nota-fiscal-de-produto-v2/#/
"""



def group_keys(key) -> Any:
    return key['CodigoPedido']


@cadastro_bp.route("/api/v2/companies/emissao/", methods=['GET','POST'])
def cadastra_notas() -> Response:
    """Ajustar ordem nfs"""
    lista_pedidos: list[dict[str, str]] = []
    with db.engine.connect() as conn:

        pedidos = conn.execute(db.select(PedidoFlexy).filter(PedidoFlexy.StatusPedido=='Em separação')).all()
        
        pedidos_sep = [next(executa_select(pedido[2])) for pedido in pedidos]
        #jsons = cadastrar_nfe(next(chain(pedidos_sep)))
        for key, value in groupby(next(chain(pedidos_sep)), group_keys):
            lista = list(value)
            lista_values = []
            lista_item = []
            buyer = {}
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

            print(jsons)
      
            return make_response(jsonify({"NotaFiscal":"Criada Com Sucesso"
                ,"Status":200,"Pedido":buyer['CodigoPedido'],"Cliente":buyer['namecliente'],"item":jsons})),201
        return "Error"


@cadastro_bp.route("/api/v2/companies/emissao/<pedido>", methods=['GET','POST'])
def cadastra_nota_referencia(pedido):

    jsons = executa_select(pedido = int(pedido))
    dict_items = next(chain(jsons))
          
    #dict_items = sorted(dict_items, key=group_keys)
    #for key, value in groupby(dict_items, group_keys):

    #    dicts = verifica_dict(next(value))
        #pedido_nf = emissao_nf(dicts,API_KEY_EMISSAO,COMPANY_ID_EMISSAO)
    print(dict_items)
    pedido_nf = emissao_nf(dict_items,API_KEY_EMISSAO,COMPANY_ID_EMISSAO)
    return make_response(jsonify(dict_items)),201
   


@cadastro_bp.route("/api/v2/companies/cancelamento/", methods=['GET','POST'])
def cancela_nota() -> Response:
    id_nf  = request.get_json()
    values = int(id_nf['id'])

    with db.engine.connect() as conn:
        query =  ItensFlexy.query.filter_by(CodigoPedido=values).first_or_404()

        items = {
                "CodigoPedido":query.CodigoPedido,
                "Quantidade":query.Quantidade,
                "QuantidadeCaixa":query.QtdCaixa
                }
        
    return jsonify({"CANCELANF":items}),201
   
@cadastro_bp.route("/api/v1/companies/cartacorrecao/", methods=['GET','POST'])
@cadastro_bp.route("/api/v2/companies/cartacorrecao/", methods=['GET','POST'])
def carta_correcao() -> Response:
    id_nf  = request.get_json()
    try:
        return jsonify({"CANCELANF":id_nf}),201
    except:
        abort(400)
