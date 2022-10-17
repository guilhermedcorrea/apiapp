from flask import Blueprint, request, jsonify, make_response, Response, abort
from functools import wraps
import requests
from typing import Dict, Tuple, List, Any
from itertools import chain
import os
from dotenv import load_dotenv

jestor_bp = Blueprint('jestor', __name__)

API_KEY_JESTOR = os.getenv('API_KEY_JESTOR')


def api_get_jestor(f):
    @wraps(f)
    def get_jestor_notafiscal(*args: tuple, **kwargs: Dict[str, Any]) -> Any:
        print(args, kwargs)
        print('Envia requisicao JESTOR CONSULTA | METODO GET')
        url = "https://supply.api.jestor.com/object/list"
        payload = {
        "object_type": f"{kwargs.get('tabela')}",
        "sort": "number_field desc",
        "page": 1,
        "size": "2"
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": f"{API_KEY_JESTOR}"
        }
        print(kwargs.get('tabela'))
        response = requests.post(url, json=payload, headers=headers)
        strs = response.json()
        try:
            for items in strs:
                dicts = strs[items]
                if isinstance(dicts, dict):
                    dict_items = dicts.get('items')
                    for values in dict_items:
                        if next(filter(lambda k: len(k) > 0, values), None):
                            yield values.get('codigo_pedido')
        
        except Exception as e:
            print("error", e)

    return get_jestor_notafiscal



@api_get_jestor
def get_parametros_nfe(*args: Any, **kwargs: Dict[str, Any]) -> Any:
    """Parametros entrada notas venda"""
    print('Called function --> NF')
    
        
@api_get_jestor
def get_pedidos_itens_jestor(*args: Any, **kwargs: Dict[str, Any]) -> Any:
    """Parametros entrada pedidos itens"""
    print('Called function --> pedidos itens')
    

@api_get_jestor
def get_clientes_jestor(*args: Any, **kwargs: Dict[str, Any]) -> Any:
    """Parametros entrada clientes"""
    print('Called function --> clientes')


@jestor_bp.route('/api/v1/jestor/notapedido/nfpedido/all', methods=['GET','POST'])
def get_jestor_nf() -> Response:
 
    all_notas = get_parametros_nfe()

    return jsonify({'Pedido':all_notas}), 201


@jestor_bp.route('/api/v1/jestor/pedidos/pedidositens/all')
def get_jestor_pedido_item_all() -> Response:
    tabela_jestor = 'pedidos_itens_hausz'
    jsons = get_pedidos_itens_jestor(tabela = tabela_jestor)
    print(jsons)
    
    data_jsons = request.get_json()

    return jsonify(data_jsons), 201

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
def get_jestor_clientes_all():
    tabela = 'clientes'
    clientes = get_clientes_jestor(tabela)
    return jsonify(clientes), 201


@jestor_bp.route('/api/v1/jestor/clientes/<refcliente>')
def get_jestor_clientes_ref_cliente(refcliente: Any) -> Response:
    tabela = 'clientes'
    refcliente = request.get_json()
    values = refcliente['refcliente']
    clientes = get_clientes_jestor(tabela)
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
    jsons = get_parametros_nfe()
    idnf = request.get_json()
    values = idnf['idnf']

    return values

@jestor_bp.route('/api/v1/jestor/pedido/<refpedido>', methods=['GET','POST'])
def get_jestor_pv(refpedido: str) -> Any:
    jsons = get_parametros_nfe()
    refpedido = request.get_json()
    values = refpedido['refpedido']
    return values


@jestor_bp.route('/api/v1/jestor/notapedido/<cliente>', methods=['GET','POST'])
def get_jestor_pv_cliente(cliente):
    jsons = get_parametros_nfe()
    cliente = request.get_json()
    values = cliente['cliente']
    return values



