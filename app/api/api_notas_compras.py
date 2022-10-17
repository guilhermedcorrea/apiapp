from flask import Blueprint
from flask import (jsonify, Response, make_response, request, redirect, current_app)
from ..models.models_notas_compras import PedidoCompraNotaEntrada
from ..schemas.schemas_notas_compras import PedidoCompraNotaEntradaSchema
from ..controllers.controllers_notas_compras import nf_compras, nf_compras_item
from apifairy import APIFairy, response, arguments, authenticate, other_responses
from flask_marshmallow import Marshmallow
from ..extensions import ma

"""
Notas Fiscais Pedidos Compras
"""

class PaginationSchema(ma.Schema):
    page = ma.Int(missing=1)
    page_size = ma.Int(missing=10)


class PedidoComprasNotaentradaSchema(ma.Schema):
    refidhausz = ma.Int()
    chavenf = ma.Str()
    cnpjfornecedor = ma.Str()
    codigopedidocompra = ma.Str()
    criadoem = ma.Date()


nfcompras_bp = Blueprint('nfcompras', __name__, url_prefix='/notas/compras')

@nfcompras_bp.route('/api/v1/hausz/notascompras/<int:page>')
#@response(PedidoComprasNotaentradaSchema, 201)
@other_responses({404:'User not found'})
def retorna_all_notas_compras(page):
    nfs = nf_compras(page)
    strs = list(nfs)
 
    return jsonify(strs), 201


@nfcompras_bp.route('/api/v1/hausz/notascompras/nf/<nf>')
def retorna_notas_compras_nf(nf):
     
    notas = nf_compras_item(nf)
    
    return jsonify(notas)


@nfcompras_bp.route('/api/v1/hausz/notascompras/item/all')
def retorna_notas_compras_item_all(nf):
    return {"NumeroNf":nf}

@nfcompras_bp.route('/api/v1/hausz/notascompras/item/<int:nf>')
def retorna_notas_compras_all_nf(nf):
    return {"NumeroNf":nf}

