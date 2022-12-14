from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime

from flask_sqlalchemy import SQLAlchemy
from ..extensions import db


class NotaFiscal(db.Model):
    __tablename__ = "NotaFiscal"
    __table_args__ = {"schema": "Pedidos"}

    IdNFe = db.Column(db.Integer, primary_key=True)
    CodigoPedido = db.Column(db.Integer)
    CodPedidoOmie = db.Column(db.Integer)
    NumPedidoOmie = db.Column(db.Integer)
    cNF = db.Column(db.Integer)
    natOp = db.Column(db.String)
    Modelo = db.Column(db.String)
    Serie = db.Column(db.Integer)
    NumeroNF = db.Column(db.Integer)
    DataEmissao = db.Column(db.DateTime, unique=False, nullable=False)
    DataSaiEnt = db.Column(db.DateTime, unique=False, nullable=False)
    Tipo = db.Column(db.Integer)
    IdDestino = db.Column(db.Integer)
    MunFG = db.Column(db.Integer)
    TipoImpressao = db.Column(db.Integer)
    TipoEmissao = db.Column(db.Integer)
    DigitoVerificados = db.Column(db.Integer)
    EANTributavel = db.Column(db.String)
    TipoAmbiente = db.Column(db.Integer)
    FinalidadeEmissao = db.Column(db.Integer)
    IdentificadorConsuFinal = db.Column(db.Boolean, unique=False, nullable=False)
    IndicadorPresenca = db.Column(db.Integer)
    ProcessoEmissao = db.Column(db.Integer)
    VersaoProcesso = db.Column(db.String)
    CnpjEmitente = db.Column(db.String)
    NomeEmitente = db.Column(db.String)
    NomeFantasiaEmitente = db.Column(db.String)
    EnderecoEmitente = db.Column(db.String)
    NumeroEmitente = db.Column(db.String)
    BairroEmitente = db.Column(db.String)
    CodigoMunicipioEmitente = db.Column(db.Integer)
    MunicipioEmitente = db.Column(db.String)
    UFEmitente = db.Column(db.String)
    CepEmitente = db.Column(db.Integer)
    IEEmitente = db.Column(db.String)
    CnpjDestino = db.Column(db.Integer)
    NomeDestino = db.Column(db.String)
    EnderecoDestino = db.Column(db.String)
    NumeroDestino = db.Column(db.String)
    ComplementoDestino = db.Column(db.String)
    BairroDestino = db.Column(db.String)
    CodigoMunicipioDestino = db.Column(db.Integer)
    MunicipioDestino = db.Column(db.String)
    UFDestino = db.Column(db.String)
    CepDestino = db.Column(db.String)
    IEDestino = db.Column(db.String)
    BaseCalculo = db.Column(db.Float)
    ICMS = db.Column(db.Float)
    FCP = db.Column(db.Float)
    BCST = db.Column(db.Float)
    ST = db.Column(db.Float)
    FCPST = db.Column(db.Float)
    FCPSTRet = db.Column(db.Float)
    VProd = db.Column(db.Float)
    VFrete = db.Column(db.Float)
    VSeg = db.Column(db.Float)
    VDesc = db.Column(db.Float)
    VII = db.Column(db.Float)
    VIPI = db.Column(db.Float)
    VIPIDevolv = db.Column(db.Float)
    VPIS = db.Column(db.Float)
    Cofins = db.Column(db.Float)
    Outro = db.Column(db.Float)
    VNF = db.Column(db.Float)
    ModFrete = db.Column(db.Integer)
    QVolume = db.Column(db.Integer)
    Esp = db.Column(db.String)
    Marca = db.Column(db.String)
    PesoL = db.Column(db.Float)
    PesoB = db.Column(db.Float)
    tpAmb = db.Column(db.Integer)
    verAplic = db.Column(db.String)
    chNFE = db.Column(db.String)
    dhRecbto = db.Column(db.DateTime, unique=False, nullable=False)
    nProt = db.Column(db.String)
    digVal = db.Column(db.String)
    cStat = db.Column(db.Integer)
    xMotivo = db.Column(db.String)
    XML = db.Column(db.String)
    DataInserido = db.Column(db.DateTime, unique=False, nullable=False)
    bitXml = db.Column(db.Boolean, unique=False, nullable=False)


    def __repr__(self):
        return f"'Codigo -> Pedido'{self.CodigoPedido},'IdDoDestini - >' {self.IdDestino}"

class NotaFiscalItens(db.Model):
    __tablename__ = "NotaFiscalItens"
    __table_args__ = {"schema": "Pedidos"}

    IdItensNF = db.Column(db.Integer, primary_key=True)
    IdNFe = db.Column(db.Integer)
    CodigoProduto = db.Column(db.String)
    EAN = db.Column(db.String)
    Produto = db.Column(db.String)
    NCM = db.Column(db.String)
    CEST = db.Column(db.String)
    CFOP = db.Column(db.String)
    UnidadeComercial = db.Column(db.Float)
    QuantidadeCompra = db.Column(db.Float)
    ValorUnidComprada = db.Column(db.Float) 
    ValorProduto = db.Column(db.Float) 
    EANTributavel = db.Column(db.String)
    UnidadeTributavel = db.Column(db.String)
    QuantidadeTributavel = db.Column(db.Integer)
    ValorUnidTributavel = db.Column(db.Float) 
    indTot = db.Column(db.Boolean, unique=False, nullable=False)

    def __repr__(self):
        return f" CodigoNfe - >{self.IdNFe}, Quantidade - > {self.QuantidadeCompra}, CodigoProduto -> {self.CodigoProduto}"


