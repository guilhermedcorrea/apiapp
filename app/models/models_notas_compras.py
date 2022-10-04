from ..extensions import db

class PedidoCompraNotaEntrada(db.Model):
    __tablename__ = "PedidoCompraNotaEntrada"
    __table_args__ = {"schema": "Pedidos"}
    IdPedidoCompraNotaEntrada = db.Column(db.Integer, primary_key=True)
    ChaveNF = db.Column(db.String(255))
    CodigoPedidoCompra = db.Column(db.Integer)
    CNPJFornecedor = db.Column(db.String(14))
    SKU = db.Column(db.String(250))
    DataInserido = db.Column(db.DateTime, unique=False, nullable=True)
    bitAtivo = db.Column(db.Boolean, nullable=False)
    Quantidade = db.Column(db.Float, unique=False, nullable=True)
    NumNfOmie = db.Column(db.Integer, unique=False, nullable=True)
    SerieNfOmie = db.Column(db.Integer, unique=False, nullable=True)
    ValorItem = db.Column(db.Float, unique=False, nullable=True)
    CustoNf = db.Column(db.Float, unique=False, nullable=True)
    DataEmissaoNf = db.Column(db.DateTime, unique=False, nullable=True)
    IdStatusItem = db.Column(db.Integer)
    EnviadoWMS = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.IdPedidoCompraNotaEntrada}'




class PedidoCompraShowroom(db.Model):
    __tablename__ = "PedidoCompra"
    __table_args__ = {"schema": "ShowRoom"}
    IdPedidoCompra = db.Column(db.Integer, primary_key=True)
    CodigoPedidoCompra = db.Column(db.Integer, unique=False, nullable=True)
    CodigoPedidoCompraOmie = db.Column(db.Integer, unique=False, nullable=True)
    PrevisaoEntrega =  db.Column(db.DateTime, unique=False, nullable=True)
    IdMarca = db.Column(db.Integer, unique=False, nullable=True)
    Observacao = db.Column(db.String(255), unique=False, nullable=True)
    bitAtivo = db.Column(db.Boolean, unique=False, nullable=True)
    IdStatusCompra = db.Column(db.Integer, unique=False, nullable=True)
    IdSituacao = db.Column(db.Integer, unique=False, nullable=True)
    EnviadoEmail = db.Column(db.Boolean, unique=False, nullable=True)
    dataInserido = db.Column(db.DateTime, unique=False, nullable=True)
    bitOmie = db.Column(db.Boolean, nullable=True)
    NumPedidoFornecedor = db.Column(db.Integer, unique=False, nullable=True)
    Idfornecedor = db.Column(db.Integer, unique=False, nullable=True)
    StatusPgto = db.Column(db.Integer, unique=False, nullable=True)

    def __repr__(self):
        return f'{self.IdPedidoCompraItens}'


class PedidoCompraItens(db.Model):
    __tablename__ = "PedidoCompraItens"
    __bind_key__ = 'HauszMapa'
    __table_args__ = {"schema": "ShowRoom"}

    IdPedidoCompraItem = db.Column()
    CodigoPedidoCompra = db.Column()
    IdProduto = db.Column()
    IdStatusItem = db.Column()
    StatusItem = db.Column()
    ValorUnitario = db.Column()
    Quantidade = db.Column()
    QuantidadeEstoque = db.Column()
    QuantidadeColeta = db.Column()
    QuantidadeAtendida = db.Column()
    PrevisaoEntrega = db.Column()
    bitAtivo = db.Column()
    bitAtrelado = db.Column()
    DataInserido = db.Column()
    CustoHausz = db.Column()
    CustoFranquia = db.Column()
    NumPedidoFornecedor = db.Column()
    DataLiberadoColeta = db.Column()

   

'''
class NotaFiscalCompra(db.Model):
    __tablename__ = "NotaFiscalCompra"
    __bind_key__ = 'HauszMapa'
    __table_args__ = {"schema": "Pedidos"}

    IdNFe = db.Column()
    CodigoPedido = db.Column()
    CodPedidoOmie = db.Column()
    NumPedidoOmie = db.Column()
    cNF = db.Column()
    natOp = db.Column()
    Modelo = db.Column()
    Serie = db.Column()
    NumeroNF = db.Column()
    DataEmissao = db.Column()
    DataSaiEnt = db.Column()
    Tipo = db.Column()
    IdDestino = db.Column()
    MunFG = db.Column()
    TipoImpressao = db.Column()
    TipoEmissao = db.Column()
    DigitoVerificados = db.Column()
    EANTributavel = db.Column()
    TipoAmbiente = db.Column()
    FinalidadeEmissao = db.Column()
    IdentificadorConsuFinal = db.Column()
    IndicadorPresenca = db.Column()
    ProcessoEmissao = db.Column()
    VersaoProcesso = db.Column()
    CnpjEmitente = db.Column()
    NomeEmitente = db.Column()
    NomeFantasiaEmitente = db.Column()
    EnderecoEmitente = db.Column()
    NumeroEmitente = db.Column()
    BairroEmitente = db.Column()
    CodigoMunicipioEmitente = db.Column()
    MunicipioEmitente = db.Column()
    UFEmitente = db.Column()
    CepEmitente = db.Column()
    IEEmitente = db.Column()
    CnpjDestino = db.Column()
    NomeDestino = db.Column()
    EnderecoDestino = db.Column()
    NumeroDestino = db.Column()
    ComplementoDestino = db.Column()
    BairroDestino = db.Column()
    CodigoMunicipioDestino = db.Column()
    MunicipioDestino = db.Column()
    UFDestino = db.Column()
    CepDestino = db.Column()
    IEDestino = db.Column()
    BaseCalculo = db.Column()
    ICMS = db.Column()
    FCP = db.Column()
    BCST = db.Column()
    ST = db.Column()
    FCPST = db.Column()
    FCPSTRet = db.Column()
    VProd = db.Column()
    VFrete = db.Column()
    VSeg = db.Column()
    VDesc = db.Column()
    VII = db.Column()
    VIPI = db.Column()
    VIPIDevolv = db.Column()
    VPIS = db.Column()
    Cofins = db.Column()
    Outro = db.Column()
    VNF = db.Column()
    ModFrete = db.Column()
    QVolume = db.Column()
    Esp = db.Column()
    Marca = db.Column()
    PesoL = db.Column()
    PesoB = db.Column()
    tpAmb = db.Column()
    verAplic = db.Column()
    chNFE = db.Column()
    dhRecbto = db.Column()
    nProt = db.Column()
    digVal = db.Column()
    cStat = db.Column()
    xMotivo = db.Column()
    XML = db.Column()
    DataInserido = db.Column()
    bitXml = db.Column()

'''
    
class NotaFiscalCompraItens(db.Model):
    __tablename__ = "NotaFiscalCompraItens"
    __bind_key__ = 'HauszMapa'
    __table_args__ = {"schema": "Pedidos"}

    IdItensNF = db.Column(db.Integer, primary_key=True)
    IdNFe = db.Column(db.Integer)
    CodigoProduto = db.Column(db.String())
    EAN = db.Column(db.String())
    Produto = db.Column(db.String())
    NCM = db.Column(db.String())
    CEST = db.Column(db.String())
    CFOP = db.Column(db.String())
    UnidadeComercial = db.Column(db.Float)
    QuantidadeCompra = db.Column(db.Integer)
    ValorUnidComprada = db.Column(db.Float)
    ValorProduto = db.Column(db.Float)
    EANTributavel = db.Column(db.String())
    UnidadeTributavel = db.Column(db.Integer)
    QuantidadeTributavel = db.Column(db.Float)
    ValorUnidTributavel = db.Column(db.Float)
    indTot = db.Column(db.Boolean, nullable=True)

