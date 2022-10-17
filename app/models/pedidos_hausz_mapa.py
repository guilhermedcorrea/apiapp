from ..extensions import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime

class PedidoFlexy(db.Model):
    __tablename__ = "PedidoFlexy"
    __bind_key__ = 'HauszMapa'
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



