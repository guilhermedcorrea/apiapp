from flask import Blueprint, request, jsonify, make_response, Response, abort, current_app
from functools import wraps
import requests
from typing import Dict, Tuple, List, Any, Literal
from itertools import chain
import os
from dotenv import load_dotenv


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


jestor_bp = Blueprint('jestor', __name__)
register_handlers(current_app)

from ..controllers.controllers_jestor import JestorHausz


@jestor_bp.route('/api/v1/jestor/notapedido/nfpedido/all', methods=['GET','POST'])
def get_jestor_nf() -> Response:
    tabela = 'notas_fiscais_de_vendas'
    all_notas = next(JestorHausz.get_parametros_nfe(tabela))
    print(all_notas)
    #if isinstance(all_notas, dict):
    #    return jsonify({all_notas})
    return ({"error":"notfound"})


@jestor_bp.route('/api/v1/jestor/pedidos/pedidositens/all', methods=['GET','POST'])
def get_jestor_pedido_item_all() -> Response:
    """Consulta e Insere Pedidos no jestor"""
    tabela_jestor = 'pedidos_itens_hausz'
    jsons = next(JestorHausz.get_api_jestor(tabela = tabela_jestor))
    if isinstance(jsons, dict):
        if request.method == 'GET':
            try:
                return ({jsons.get('codigopedido'):jsons})
            except Exception as e:
                abort(400)
        elif request.method == 'POST':
            try:
                return jsonify("cria dict, insere pedido {}".format(jsons.get('codigopedido')))
            except Exception as e:
                abort(400)
                
        return "Error"
    return "Error"
   

@jestor_bp.route('/api/v1/jestor/pedidos/pedidositens/<data>')
def get_jestor_pedido_item_data(data: Any) -> Response:
    data = request.get_json()
    values = data['data']

    return jsonify(values), 201

@jestor_bp.route('/api/v1/jestor/pedidos/pedidositens/<refpedido>')
def get_jestor_pedido_item_refpedido(refpedido: Any) -> Response:
    refpedido = request.get_json()
    values = refpedido['refpedido']
    return jsonify(values), 201


@jestor_bp.route('/api/v1/jestor/clientes/all')
def get_jestor_clientes_all()-> tuple[Response, Literal[201]]:
    tabela = 'clientes'
    clientes = JestorHausz.get_clientes_jestor(tabela)
    return jsonify(clientes), 201


@jestor_bp.route('/api/v1/jestor/clientes/<refcliente>')
def get_jestor_clientes_ref_cliente(refcliente: Any) -> Response:
    tabela = 'clientes'
    refcliente = request.get_json()
    values = refcliente['refcliente']
    clientes = JestorHausz.get_clientes_jestor(tabela)
    return jsonify(clientes)

@jestor_bp.route('/api/v1/jestor/pedidos/pedidositens/<status>')
def get_jestor_pedido_item_status(status: Any) -> Response:
    status = request.get_json()
    values = status['status']

    return jsonify(values), 201

@jestor_bp.route('/api/v1/jestor/pedidos/pedidositens/<cliente>')
def get_jestor_pedido_item_cliente(cliente: Any) -> Response:
    cliente = request.get_json()
    values = cliente['cliente']

    return jsonify(values), 201

@jestor_bp.route('/api/v1/jestor/<item>', methods=['GET','POST'])
def get_jestor_nf_item(item: str) -> Any:
    item = request.get_json()
    values = item['item']

    return jsonify(values), 201


@jestor_bp.route('/api/v1/jestor/notapedido/<idnf>', methods=['GET','POST'])
def get_jestor_nf_pedido_idnf(idnf: int) -> Any:
    jsons = JestorHausz.get_parametros_nfe()
    idnf = request.get_json()
    values = idnf['idnf']

    return values

@jestor_bp.route('/api/v1/jestor/pedido/<refpedido>', methods=['GET','POST'])
def get_jestor_pv(refpedido: str) -> Any:
    jsons = JestorHausz.get_parametros_nfe()
    refpedido = request.get_json()
    values = refpedido['refpedido']
    return values

@jestor_bp.route('/api/v1/jestor/notapedido/<cliente>', methods=['GET','POST'])
def get_jestor_pv_cliente(cliente):
    jsons = JestorHausz.get_parametros_nfe()
    cliente = request.get_json()
    values = cliente['cliente']
    return values



