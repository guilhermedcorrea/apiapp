from flask import Blueprint, request, jsonify, make_response, Response
from functools import wraps
import requests
from ..controllers.controllers_pedidos import get_pedidos_flexy
from typing import Dict, Tuple, List, Any
from itertools import chain
jestor_bp = Blueprint('jestor', __name__)


def get_metodo_nf(f):
    @wraps(f)
    def get_jestor_notafiscal(*args: tuple, **kwargs: Dict[str, Any]) -> Any:
        print(args, kwargs)
        print('Envia requisicao JESTOR CONSULTA | METODO GET')
        url = "https://supply.api.jestor.com/object/list"
        payload = {
        "object_type": f"{kwargs.get('tabela')}",
        "sort": "number_field desc",
        "page": 1,
        "size": "10"
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": "Bearer YjE5NzI5N2Q5YjA2MmEw1a23e3b4a7MTY2NDIzMDAyODg1ZTg2"
        }

        response = requests.post(url, json=payload, headers=headers)
        return response.json()

    return get_jestor_notafiscal



@get_metodo_nf
def get_parametros_nfe(*args: Any, **kwargs: Dict[str, Any]) -> Any:
    """Parametros entrada notas venda"""
    print('Called example function')
    
        
@get_metodo_nf
def get_pedidos_itens_jestor(*args: Any, **kwargs: Dict[str, Any]) -> Any:
    """Parametros entrada pedidos itens"""
    

@jestor_bp.route('/api/v1/jestor/notapedido/nfpedido/all', methods=['GET','POST'])
def get_jestor_nf() -> Response:
 
    all_notas = get_parametros_nfe()
    jsons = get_pedidos_flexy()
    pedido = [x for x in next(jsons)]
    return jsonify({'Pedido':pedido})


@jestor_bp.route('/api/v1/jestor/pedidos/pedidositens/all')
def get_jestor_pedido_item_all() -> Response:
    tabela_jestor = 'pedidos_itens_hausz'
    jsons = get_pedidos_itens_jestor(tabela = tabela_jestor)
    data_jsons = request.get_json()
    print(jsons)
  
    return jsonify(data_jsons)

@jestor_bp.route('/api/v1/jestor/pedidos/pedidositens/<data>')
def get_jestor_pedido_item_data(data: Any) -> Response:
    data = request.get_json()
    values = data['data']

    return jsonify(values)

@jestor_bp.route('/api/v1/jestor/pedidos/pedidositens/<refpedido>')
def get_jestor_pedido_item_refpedido(refpedido: Any) -> Response:
    refpedido = request.get_json()
    values = refpedido['refpedido']

    return jsonify(values)

@jestor_bp.route('/api/v1/jestor/pedidos/pedidositens/<status>')
def get_jestor_pedido_item_status(status: Any) -> Response:
    status = request.get_json()
    values = status['status']

    return jsonify(values)

@jestor_bp.route('/api/v1/jestor/pedidos/pedidositens/<cliente>')
def get_jestor_pedido_item_cliente(cliente: Any) -> Response:
    cliente = request.get_json()
    values = cliente['cliente']

    return jsonify(values)

@jestor_bp.route('/api/v1/jestor/<item>', methods=['GET','POST'])
def get_jestor_nf_item(item: str) -> Any:
    item = request.get_json()
    values = item['item']

    return jsonify(values)


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



