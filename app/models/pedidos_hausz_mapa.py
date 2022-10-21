from ..extensions import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime


class PedidoFlexy(db.Model):
    __tablename__ = "PedidoFlexy"
    __table_args__ = {"schema": "Pedidos"}
    IdPedidoFlexy = db.Column(db.Integer, primary_key=True)
    IdOrcamento = db.Column(db.Integer)
    CodigoPedido = db.Column(db.Integer)
    PrecoFrete = db.Column(db.DateTime, unique=False, nullable=False)
    StatusPedido = db.Column(db.String)
    IdPromocaoFlexy = db.Column(db.Integer)
    IdCliente = db.Column(db.Integer)
    IdColaborador = db.Column(db.Integer)
    Comissao = db.Column(db.DateTime, unique=False, nullable=False)
    IdUnidade = db.Column(db.Integer)
    IdFormaPagamento = db.Column(db.Integer)
    IdAtributo = db.Column(db.Integer)
    ValorTotal = db.Column(db.DateTime, unique=False, nullable=False)
    IdEtapaFlexy = db.Column(db.Integer)
    Desconto = db.Column(db.DateTime, unique=False, nullable=False)
    ValorEntrada = db.Column(db.DateTime, unique=False, nullable=False)
    DataInserido = db.Column(db.DateTime, unique=False, nullable=False)
    BitSplit = db.Column(db.Boolean, unique=False, nullable=False)
    BitOmie = db.Column(db.Boolean, unique=False, nullable=False)
    CodPedidoOmie = db.Column(db.String)
    NumPedidoOmie = db.Column(db.String)
    ValorTotalDescontado = db.Column(db.Float)
    Split = db.Column(db.Float)
    Margem =  db.Column(db.Float)
    WmsEtapa = db.Column(db.Integer)
    DataInseridoOmie = db.Column(db.DateTime, unique=False, nullable=False)
    NumPedidoFornecedor = db.Column(db.String)
    PedidoPai = db.Column(db.Integer)
    PrevisaoEntrega = db.Column(db.DateTime, unique=False, nullable=False)
    bitDesconto = db.Column(db.Boolean, unique=False, nullable=False)
    bitAtualizadoStatus = db.Column(db.Boolean, unique=False, nullable=False)
    NomePedido = db.Column(db.String)
    OrigemPedido = db.Column(db.String)
    DesmPedido = db.Column(db.Integer)
    IdEspecialista = db.Column(db.Integer)
    IdOrderJet = db.Column(db.Integer)
    IdSistema = db.Column(db.Integer)
    IdCardJestor = db.Column(db.Integer)
    PrevisaoOriginal  = db.Column(db.DateTime, unique=False, nullable=False)



#Pedido Etapa Flexy
'''
class EtapaFlexy(db.Model):
    __tablename__ = "PedidoFlexy"
    __bind_key__ = 'HauszMapa'
    __table_args__ = {"schema": "Pedidos"}

    IdEtapa = db.Column(db.Integer, primary_key=True)
    NomeEtapa = db.Column(db.String)
    bitAtivo = db.Column(db.Boolean, unique=False, nullable=False)
    DataInserido = db.Column(db.DateTime, unique=False, nullable=False)
    InseridoPor = db.Column(db.String)
    CodigoStatusJet = db.Column(db.String)
    NameStatusJet = db.Column(db.String)
    IdStatus = db.Column(db.Integer)

    def __repr__(self):
        return f"idetapa - > {self.IdEtapa}, NomeEtapa - > {self.NomeEtapa}"
'''
class ItensFlexy(db.Model):
    __tablename__ = "ItensFlexy"
    __table_args__ = {"schema": "Pedidos"}

    IdPedidoItensFlexy = db.Column(db.Integer, primary_key=True)
    CodigoPedido = db.Column(db.Integer)
    Quantidade = db.Column(db.Float)
    QuantidadeReservada = db.Column(db.Float)
    QtdCaixa = db.Column(db.Float)
    PrecoUnitario = db.Column(db.Float)
    IdProduto = db.Column(db.Integer)
    SKU = db.Column(db.String)
    CodigoReferencia = db.Column(db.String)
    IdEndEntregaFlexy = db.Column(db.Integer)
    PrevisaoColeta = db.Column(db.DateTime, unique=False, nullable=False)
    EntregaDiaMinimo = db.Column(db.DateTime, unique=False, nullable=False)
    EntregaDiaMaximo = db.Column(db.DateTime, unique=False, nullable=False)
    DataMinimaEntrega = db.Column(db.DateTime, unique=False, nullable=False)
    DataMaximaEntrega = db.Column(db.DateTime, unique=False, nullable=False)
    LocalEstoque = db.Column(db.Integer)
    Transportador = db.Column(db.Integer)
    Observacoes = db.Column(db.String)
    IdPromocaoFlexy = db.Column(db.Integer)
    MvaOriginal = db.Column(db.Float)
    MvaAjustado = db.Column(db.Float)
    AliquotaInterna = db.Column(db.Float)
    AliquotaExterna = db.Column(db.Float)
    TaxaFrete = db.Column(db.Float)
    IPI = db.Column(db.Float)
    IdPropriedadesPedidoFlexy =db.Column(db.Integer)
    IdEstoque = db.Column(db.Integer)
    CodigoPedidoCompra = db.Column(db.Integer)
    DescontoItem = db.Column(db.Float)
    PrecoUnitarioDescontado = db.Column(db.Float)
    DataInserido = db.Column(db.DateTime, unique=False, nullable=False)
    bitAtivo = db.Column(db.Boolean, unique=False, nullable=False)
    CodigoPedidoCompra2 = db.Column(db.Integer)
    PedidoPai = db.Column(db.Integer)
    CustoUnitario = db.Column(db.Float)
    IdStatusReserva = db.Column(db.Integer)












