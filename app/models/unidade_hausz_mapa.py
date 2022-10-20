
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def configure(app):
    db.init_app(app)
    app.db = db


class Unidade(db.Model):
    __tablename__ = "Unidade"
    __bind_key__ = 'HauszLogin'
    __table_args__ = {"schema": "Cadastro"}
    IdUnidade = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String)
    IdCidade = db.Column(db.Integer)
    IdPraca = db.Column(db.Integer)
    IdPracaNovo = db.Column(db.Integer)
    UF = db.Column(db.String)
    Email = db.Column(db.String)
    bitAtivo = db.Column(db.Boolean, unique=False, nullable=False)
    bitInaugurada = db.Column(db.Boolean, unique=False, nullable=False)
    IdPipefy = db.Column(db.Integer)
    TaxaAdministrativa = db.Column(db.Float)
    TaxaLogistica = db.Column(db.Float)
    Royalties = db.Column(db.Float)
    PercentualFrete = db.Column(db.Float)
    DataInserido = db.Column(db.DateTime, unique=False, nullable=False)
    RefenciaFlexy = db.Column(db.String)
    bitPermissaoVenda = db.Column(db.Boolean, unique=False, nullable=False)
    RazaoSocial = db.Column(db.String)
    InscricaoEstadual = db.Column(db.String)
    NomeContaBancaria = db.Column(db.String)
    CodigoBanco = db.Column(db.Integer)
    AgenciaBancaria = db.Column(db.String)
    ContaBancaria = db.Column(db.String)
    FormaPagamento = db.Column(db.String)
    ChavePix = db.Column(db.String)
    InseridoPor = db.Column(db.String)
    AlteradoPor = db.Column(db.String)
    RaioObra = db.Column(db.Float)
    bitApresentacaoProjeto = db.Column(db.Boolean, unique=False, nullable=False)
    PrevisaoInauguracao = db.Column(db.DateTime, unique=False, nullable=False)
    bitConfirmaTermoResponsabilidade = db.Column(db.Boolean, unique=False, nullable=False)
    IdColaboradorKA = db.Column(db.Integer)
    IdColaboradorArq = db.Column(db.Integer)
    IdStatusUnidade = db.Column(db.Integer)
    SenhaA1 = db.Column(db.String)
    IdColaboradorGC = db.Column(db.Integer)
    ValorUnidade = db.Column(db.Float)
    DataLimiteEscolhaPonto = db.Column(db.DateTime, unique=False, nullable=False)
    ValorProjetoArquitetonico = db.Column(db.Float)
    ValorProjetoExecutivo = db.Column(db.Float)
    DataInauguracao = db.Column(db.DateTime, unique=False, nullable=False)
    Parcelas = db.Column(db.Integer)
    Pix = db.Column(db.String)
    bitLead = db.Column(db.Boolean, unique=False, nullable=False)
    EmailFranqueado = db.Column(db.String)
    FimContrato = db.Column(db.DateTime, unique=False, nullable=False)
    NomeColaborador = db.Column(db.String)
    RoyaltiesFaturamento = db.Column(db.Float)
    RoyaltiesData = db.Column(db.DateTime, unique=False, nullable=False)
    IdNivelLead = db.Column(db.Integer)
    IdColabRespWpp = db.Column(db.Integer, unique=False, nullable=False)
    bitIsencaoRAlterada = db.Column(db.Boolean, unique=False, nullable=False)
    DataAlteracao = db.Column(db.DateTime, unique=False, nullable=False)

    def __repr__(self):
        return f"IDUNIDADE - >{self.IdUnidade}, NOMEUNIDADE - > {self.Nome}"
