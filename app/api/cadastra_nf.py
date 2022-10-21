
from flask import (Blueprint, Request, jsonify
    , make_response, Response, redirect, current_app, request,abort)
from flask_marshmallow import Marshmallow
from sqlalchemy import text
from itertools import chain
from ..controllers.controllers_notas import emissao_nfe
import os
from dotenv import load_dotenv
import json
from typing import Dict, Tuple, List, Literal, Any
from ..controllers.controllers_hausz_mapa import executa_select
from ..extensions import db
from itertools import groupby


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

@emissao_nfe
def notas_fiscais(*args: tuple, **kwargs: Dict[str, Any]) -> None:
    """Docstring"""
    print('Called function')


def group_keys(key) -> Any:
    return key['CodigoPedido']


#convert(date,getdate()
#teste funcao

def verifica_dict(dict_items) -> (dict | Literal['erro'] | None):
    match dict_items:
        case dict_items if len(dict_items) >1:
            for items in dict_items:
                return {items.get('CodigoPedido'):items}
        case dict_items if len(dict_items) ==1:
            for items in dict_items:
                return {items.get('CodigoPedido'):items}
        case _:
            return "erro"


@cadastro_bp.route("/api/v1/companies/emissao/", methods=['GET','POST'])
def cadastra_notas() -> Response:
    lista_pedidos: list[dict[str, str]] = []
    with db.engine.connect() as conn:
        query = (text("""
            SELECT DISTINCT *FROM [HauszMapa].[Pedidos].[PedidoFlexy] AS PFLEXY
            JOIN [HauszMapa].[Pedidos].[EnderecoPedidos]AS EPEDIDO
            ON EPEDIDO.Idcliente = PFLEXY.IdCliente
            WHERE convert(date,PFLEXY.[DataInserido])  =  '2022-10-18'
            AND PFLEXY.StatusPedido ='Em separação'"""))
        teste = conn.execute(query).all()
      
        query_dicts = [{key: value for (key, value) in row.items()} for row in teste]
        for pedidos in query_dicts:
          
            jsons = executa_select(pedido = pedidos.get('CodigoPedido'))
            dict_items = next(chain(jsons))
            #print(dict_items)
            dict_items = sorted(dict_items, key=group_keys)
        
            for key, value in groupby(dict_items, group_keys):
                #cont = len(list(value))
                dicts = verifica_dict(list(value))
                lista_pedidos.append(dicts)

    return make_response(jsonify(lista_pedidos))

@cadastro_bp.route("/api/v1/companies/cancelamento/", methods=['GET','POST'])
def cancela_nota() -> Response:
    id_nf  = request.get_json()
    try:
        return jsonify({"CANCELANF":id_nf}),201
    except:
        abort(400)

@cadastro_bp.route("/api/v1/companies/cartacorrecao/", methods=['GET','POST'])
def carta_correcao() -> Response:
    id_nf  = request.get_json()
    try:
        return jsonify({"CANCELANF":id_nf}),201
    except:
        abort(400)
