
from flask import (Blueprint, Request, jsonify
    , make_response, Response, redirect, current_app, request,abort)
from flask_marshmallow import Marshmallow
from sqlalchemy import text
from itertools import chain

from ..controllers.controllers_hausz import PedidosComprasHausz



cadastro_bp = Blueprint('cadastronf', __name__)
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY_EMISSAO = os.getenv('API_KEY_EMISSAO')
COMPANY_ID_EMISSAO = os.getenv('COMPANY_ID_EMISSAO')

@current_app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify({'error': 'Not found'}), 404)



"""
Emissao notas ficais
https://nfe.io/docs/desenvolvedores/rest-api/nota-fiscal-de-produto-v2/#/
"""

@cadastro_bp.route("/api/v1/companies/emissao/", methods=['GET','POST'])
def cadastra_notas() -> Response:
    try:
        valores = request.get_json()
        print(valores)
        #pedidos = get_pedidos_flexy()
        #pedido = [x for x in next(pedidos)]
        return jsonify({"nf":'emissao'}), 201
    except:
        abort(400)

    


@cadastro_bp.route("/api/v1/companies/cancelamento/", methods=['GET','POST'])
def cancela_nota() -> Response:
    id_nf  = request.get_json()
    try:
        return jsonify({"CANCELANF":id_nf}),201
    except:
        abort(400)