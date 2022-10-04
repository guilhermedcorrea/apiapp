from ..extensions import db
from ..models.models_notas_compras import PedidoCompraNotaEntrada, NotaFiscalCompraItens
from ..schemas.schemas_notas_compras import PedidoCompraNotaEntradaSchema , NotaFiscalCompraItensSchema
from sqlalchemy import select
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask import current_app



def nf_compras(page):
    with db.engine.connect() as conn:
        schema = PedidoCompraNotaEntradaSchema(many=True)
        pcompras = conn.execute(select(PedidoCompraNotaEntrada).order_by(PedidoCompraNotaEntrada.IdPedidoCompraNotaEntrada).limit(20).offset(page)).all()

        schemasnf = schema.dump(pcompras)
        if next(filter(lambda pedido: len(pedido)>0,schemasnf), None):
            for items in schemasnf:
                dict_nf = {}
                dict_nf['chavenf'] = items.get('ChaveNF')
                dict_nf['numeronf'] = items.get('NumNfOmie')
                dict_nf['cnpjfornecedor'] = items.get('CNPJFornecedor')
                #dict_nf['marca'] = schemasnf['']
                dict_nf['codigopedidocompra'] = items.get('CodigoPedidoCompra')
                #dict_nf['dataemissao'] = schemasnf.get('DataEmissaoNf')
                dict_nf['criadoem'] = items.get('DataInserido')
          
                yield dict_nf



def nf_compras_item(nf):
    with db.engine.connect() as conn:
        schema = PedidoCompraNotaEntradaSchema(many=True)
        itemnfscompras = conn.execute(select(PedidoCompraNotaEntrada.ChaveNF, PedidoCompraNotaEntrada.CodigoPedidoCompra
        ,PedidoCompraNotaEntrada.DataEmissaoNf,PedidoCompraNotaEntrada.DataInserido,PedidoCompraNotaEntrada.SKU,PedidoCompraNotaEntrada.SerieNfOmie
         ,PedidoCompraNotaEntrada.NumNfOmie).where(PedidoCompraNotaEntrada.NumNfOmie == nf)).all()

        schemasnf = schema.dump(itemnfscompras)
        return schemasnf

    '''
        dict_nf_item = {}

        dict_nf_item['chavenf']
        dict_nf_item['numeronf']
        dict_nf_item['cnpjfornecedor']
        dict_nf_item['marca']
        dict_nf_item['codigopedidocompra']
        dict_nf_item['sku']
        dict_nf_item['nomedosku']
        dict_nf_item['quantidadenf']
        dict_nf_item['fatordeconversaodanf']
        dict_nf_item['bitativo']
        dict_nf_item['datadaemissaonf']
        dict_nf_item['valorunitarionf']
        dict_nf_item['valortotalitem']
        dict_nf_item[ 'recordid']
        dict_nf_item['status']

    '''