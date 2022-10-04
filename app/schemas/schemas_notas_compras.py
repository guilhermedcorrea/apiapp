
from ..models.models_notas_compras import PedidoCompraNotaEntrada, NotaFiscalCompraItens
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

'''
class PedidoCompraDanfeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = PedidoCompraDanfe
        include_fk = True
        load_instance = True

    IdPedidoCompraDanfe = auto_field()
    CodigoPedidoCompra = auto_field()
    ChaveNF = auto_field()
    UrlXML = auto_field()
    IdStatusFaturamento  = auto_field()
    bitAtivo = auto_field()
    DataInserido = auto_field()
    NumNfOmie = auto_field()

'''

class PedidoCompraNotaEntradaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = PedidoCompraNotaEntrada
        include_fk = True
        load_instance = True


    IdPedidoCompraNotaEntrada = auto_field()
    ChaveNF = auto_field()
    CodigoPedidoCompra = auto_field()
    CNPJFornecedor = auto_field()
    SKU = auto_field()
    DataInserido = auto_field()
    bitAtivo = auto_field()
    Quantidade = auto_field()
    NumNfOmie = auto_field()
    SerieNfOmie = auto_field()
    ValorItem = auto_field()
    CustoNf = auto_field()
    DataEmissaoNf = auto_field()
    IdStatusItem = auto_field()
    EnviadoWMS = auto_field()



class NotaFiscalCompraItensSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = NotaFiscalCompraItens
        include_fk = True
        load_instance = True
  
    IdItensNF = auto_field()
    IdNFe = auto_field()
    CodigoProduto = auto_field()
    EAN = auto_field()
    Produto = auto_field()
    NCM = auto_field()
    CEST = auto_field()
    CFOP = auto_field()
    UnidadeComercial = auto_field()
    QuantidadeCompra = auto_field()
    ValorUnidComprada = auto_field()
    ValorProduto = auto_field()
    EANTributavel = auto_field()
    UnidadeTributavel = auto_field()
    QuantidadeTributavel =auto_field()
    ValorUnidTributavel =auto_field()
    indTot = auto_field()
