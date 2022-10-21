from typing import Any
from flask import Blueprint, request, jsonify, make_response, Response, abort, current_app
from functools import wraps
import os
from dotenv import load_dotenv
import requests
from typing import Dict, Tuple, List
from ..extensions import db
from ..models.pedidos_hausz_mapa import PedidoFlexy
from ..models.cliente_hausz_mapa import EnderecoPedidos
from sqlalchemy import text
from datetime import datetime
from itertools import chain
from ..controllers.controllers_hausz_mapa import executa_select
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

consulta_bp = Blueprint('consultanf', __name__)
register_handlers(current_app)

from ..controllers.controllers_notas import get_metodo, list_all_empresas

"""
NOTA FISCAL CONSUMIDOR

"""
load_dotenv()



API_KEY_EMISSAO = os.getenv('API_KEY_EMISSAO')
COMPANY_ID_EMISSAO = os.getenv('COMPANY_ID_EMISSAO')


@get_metodo
def get_parametros(*args: tuple, **kwargs: Dict[str, Any]) -> None:
    """Docstring"""
    print('Called function')


@list_all_empresas
def get_list_empresas(*args: tuple, **kwargs: Dict[str, Any]) -> None:
    print("teste")


"""
Lista notas
https://nfe.io/docs/desenvolvedores/rest-api/nota-fiscal-de-consumidor-v2/#/

"""

@consulta_bp.route('/api/v2/companies/list/empresas/all', methods=['GET','POST'])
def listas_all_empresas() -> Response:
    try:
        jsons = get_list_empresas(api_key= API_KEY_EMISSAO)
        return make_response(jsonify(jsons)), 201
    except:
        abort(400)

@consulta_bp.route('/api/v2/companies/list/nfe/all', methods=['GET','POST'])
def consulta_nf():
    try:
        jsons = get_parametros(compani_id=COMPANY_ID_EMISSAO, api_key=API_KEY_EMISSAO)
        return make_response(jsonify(jsons))
    except:
        abort(400)
  
def group_keys(key):
    return key['CodigoPedido']

#teste funcao
@consulta_bp.route("/api/v1/teste", methods=['GET','POST'])
def retorna_teste():
    lista_pedidos = []
    with db.engine.connect() as conn:
        query = (text("""
            SELECT DISTINCT *FROM [HauszMapa].[Pedidos].[PedidoFlexy] AS PFLEXY
            JOIN [HauszMapa].[Pedidos].[EnderecoPedidos]AS EPEDIDO
            ON EPEDIDO.Idcliente = PFLEXY.IdCliente
            WHERE convert(date,PFLEXY.[DataInserido])  =  convert(date,getdate()) 
            AND PFLEXY.StatusPedido ='Em separação'"""))
        teste = conn.execute(query).all()
        query_dicts = [{key: value for (key, value) in row.items()} for row in teste]
        for pedidos in query_dicts:
      
            jsons = executa_select(pedido = pedidos.get('CodigoPedido'))
            dict_items = next(chain(jsons))
            dict_items = sorted(dict_items, key=group_keys)
 
            for key, value in groupby(dict_items, group_keys):
                print(key)
                print(list(value))
            '''
            dict_items.update(pedidos)
            dict_pedidos = {}
            dict_pedidos['CodigoPedido'] = dict_items.get('CodigoPedido')
            dict_pedidos['IdCliente'] = dict_items.get('IdCliente')
            dict_pedidos['IdPedidoFlexy'] = dict_items.get('IdPedidoFlexy')
            dict_pedidos['NomeCliente'] = dict_items.get('NomeCliente')
            dict_pedidos['IdFormaPagamento'] = dict_items.get('IdFormaPagamento')
            dict_pedidos['IdEtapaFlexy'] = dict_items.get('IdEtapaFlexy')
            dict_pedidos['StatusPedido'] = dict_items.get('StatusPedido')
            dict_pedidos['Transportador'] = dict_items.get('')
            dict_pedidos['IdUnidade'] = dict_items.get('Transportador')
            dict_pedidos['Franquia'] = dict_items.get('FranquiaRealizouVenda')
            dict_pedidos['IdFranquiaVenda'] = dict_items.get('IdFranquiaVenda')
            dict_pedidos['IdProduto'] = dict_items.get('IdProduto')
            dict_pedidos['SKU'] = dict_items.get('SKU')
            dict_pedidos['Quantidade'] = dict_items.get('Quantidade')
            dict_pedidos['QuantidadeReservada'] =dict_items.get('QuantidadeReservada')
            dict_pedidos['NomeProduto'] =dict_items.get('NomeProduto')
            dict_pedidos['EAN'] = dict_items.get('EAN')
            dict_pedidos['NCM'] = dict_items.get('NCM')
            dict_pedidos['CEST'] = dict_items.get('CEST')
            dict_pedidos['Marca'] = dict_items.get('Marca')
            dict_pedidos['IdMarca'] = dict_items.get('IdMarca')
            dict_pedidos['PesoCubado'] =  dict_items.get('PesoCubado')
            dict_pedidos['Peso'] =  dict_items.get('Peso')
            dict_pedidos['TamanhoBarra'] =  dict_items.get('TamanhoBarra')
            dict_pedidos['Unidade'] =  dict_items.get('Unidade')
            dict_pedidos['FatorVenda'] =  dict_items.get('FatorVenda')
            dict_pedidos['FatorMultiplicador'] =  dict_items.get('FatorMultiplicador')
            dict_pedidos['FatorUnitario'] =  dict_items.get('FatorUnitario')
            dict_pedidos['Garantia'] =  dict_items.get('Garantia')
            dict_pedidos['Comprimento'] =  dict_items.get('Comprimento')
            dict_pedidos['Largura'] =  dict_items.get('Largura')
            dict_pedidos['Altura'] =  dict_items.get('Altura')
            dict_pedidos['PrecoUnitario'] =  dict_items.get('PrecoUnitario')
            dict_pedidos['MvaOriginal'] =  dict_items.get('MvaOriginal')
            dict_pedidos['MvaAjustado'] =  dict_items.get('MvaAjustado')
            dict_pedidos['AliquotaInterna'] =  dict_items.get('AliquotaInterna')
            dict_pedidos['AliquotaExterna'] =  dict_items.get('AliquotaExterna')
            dict_pedidos['TaxaFrete'] =  dict_items.get('TaxaFrete')
            dict_pedidos['IPI'] =  dict_items.get('IPI')
            dict_pedidos['IdCliente'] =  dict_items.get('IdCliente')
            dict_pedidos['PrecoFrete'] =  dict_items.get('PrecoFrete')
            dict_pedidos['Desconto'] =  dict_items.get('Desconto')
            dict_pedidos['ValorEntrada'] =  dict_items.get('ValorEntrada')
            dict_pedidos['DataInserido'] =  dict_items.get('DataInserido')
            dict_pedidos['OrigemPedido'] =  dict_items.get('OrigemPedido')
            dict_pedidos['EnderecoCliente'] =  dict_items.get('EnderecoCliente')
            dict_pedidos['Numero'] =  dict_items.get('Numero')
            dict_pedidos['Bairro'] =  dict_items.get('Bairro')
            dict_pedidos['Cep'] =  dict_items.get('Cep')
            dict_pedidos['Complemento'] =  dict_items.get('Complemento')
            dict_pedidos['Observacao'] =  dict_items.get('Observacao')
            dict_pedidos['bitShowRoom'] =  dict_items.get('bitShowRoom')
            '''
          

            return jsonify({dict_items.get('CodigoPedido'):dict_items})
            
         

       
   


'''
@consulta_bp.route('/api/v1/companies/consumerinvoices/<consumer_invoice_id>', methods=['GET','POST'])
def consultar_nf_id(consumer_invoice_id: str) -> Response:
    consumer_invoice_id = request.get_json()
    values = consumer_invoice_id['consumer_invoice_id']
    print(values)
    return jsonify({"Notas":values})


@consulta_bp.route('/api/v1/companies/consumerinvoices/<consumer_invoice_id>/items', methods=['GET','POST'])
def consultar_produtos_id_nf(consumer_invoice_id: str) -> Response:
    consumer_invoice_id = request.get_json()
    values = consumer_invoice_id['consumer_invoice_id']
    return jsonify({"Notas":values})


@consulta_bp.route('/api/v1/companies/consumerinvoices/<consumer_invoice_id>/events', methods=['GET','POST'])
def consultar_eventos_nf_id(consumer_invoice_id: str) -> Response:
    consumer_invoice_id = request.get_json()
    values = consumer_invoice_id['consumer_invoice_id']
    return jsonify({"Notas":values})


@consulta_bp.route('/api/v1/companies/consumerinvoices/<consumer_invoice_id>/xml', methods=['GET','POST'])
def consultar_xml_nf(consumer_invoice_id: str) -> Response:
    consumer_invoice_id = request.get_json()
    values = consumer_invoice_id['consumer_invoice_id']
    print(consumer_invoice_id)
    return jsonify({"Notas":values})


@consulta_bp.route('/api/v1/companies/consumerinvoices/<consumer_invoice_id>/rejeicao/xml', methods=['GET','POST'])
def consultar_xml_rejeicao_id(consumer_invoice_id: str) -> Response:
    consumer_invoice_id = request.get_json()
    values = consumer_invoice_id['consumer_invoice_id']
    print(values)
    return jsonify({"Notas":values})
'''