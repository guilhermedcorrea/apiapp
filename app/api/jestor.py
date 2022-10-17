from flask import Blueprint, request, jsonify, make_response, Response
from functools import wraps
import requests
from ..controllers.controllers_pedidos import get_pedidos_flexy
from typing import Dict, Tuple, List, Any

jestor_bp = Blueprint('jestor', __name__)


def get_metodo(f):
    @wraps(f)
    def obtem_endpoint_jestor(*args: tuple, **kwargs: Dict[str, Any]) -> Any:
        print('Envia requisicao JESTOR CONSULTA | METODO GET')
        url = "https://supply.api.jestor.com/object/list"
        payload = {
        "object_type": "notas_fiscais_de_vendas",
        "sort": "number_field desc",
        "page": 1,
        "size": "100"
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": "Bearer YjE5NzI5N2Q5YjA2MmEw1a23e3b4a7MTY2NDIzMDAyODg1ZTg2"
        }

        response = requests.post(url, json=payload, headers=headers)
        return response.json()

    return obtem_endpoint_jestor


@get_metodo
def get_parametros_nfe(*args: Any, **kwargs: Dict[str, Any]) -> Any:
    """Docstring"""
    print('Called example function')
        

@jestor_bp.route('/api/v1/jestor/notapedido/nfpedido/all', methods=['GET','POST'])
def get_jestor_nf() -> Response:
    all_notas = get_parametros_nfe()
    jsons = get_pedidos_flexy()
    pedido = [x for x in next(jsons)]
    return jsonify({'Pedido':pedido})


@jestor_bp.route('/api/v1/jestor/notapedido/nfpedido/hauasz', methods=['GET','POST'])
def retorna_pedidos_hausz():
    jrs = get_pedidos_flexy()
    pedido = [x for x in next(jrs)]
    return jsonify({'Pedidos':pedido})

'''
        try:
            jsons = get_pedidos_flexy()
            pedido = [x for x in next(jsons)]
            return jsonify({'Pedido':all_notas})
        except:
            return jsonify({"Valor":"NotFound"})
            
    elif request.method =='POST':
        try:
            jsons = get_pedidos_flexy()
     
            return jsonify({"Pedido":all_notas})
        except:
            return jsonify({"Valor":"Notfound"})


    return jsonify({'valor':None})

    #jsons = get_parametros_nfe()
'''

    
@jestor_bp.route('/api/v1/jestor/<item>', methods=['GET','POST'])
def get_jestoir_nf_item(item: str) -> Any:
    jsons = get_parametros_nfe()
    item = request.get_json()
    values = item['item']
    return values


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



