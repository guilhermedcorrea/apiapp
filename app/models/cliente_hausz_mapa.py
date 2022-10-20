from ..extensions import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime


class Cliente(db.Model):
    __tablename__ = "Cliente"
    __bind_key__ = 'HauszLogin'
    __table_args__ = {"schema": "Cadastro"}
    IdCliente = db.Column(db.Integer, primary_key=True)
    NomeCliente = db.Column(db.String)
    IdUsuario = db.Column(db.Integer)
    PerfilObra = db.Column(db.Integer)
    IdUnidade = db.Column(db.Integer)
    DataObra = db.Column(db.DateTime, unique=False, nullable=False)
    NomeArquiteto = db.Column(db.String)
    BairroOportunidade = db.Column(db.String)
    InstagramCliente = db.Column(db.String)
    CpfCnpj = db.Column(db.String)
    CEPObra = db.Column(db.String)
    IdCidade = db.Column(db.Integer)
    EnderecoObra = db.Column(db.String)
    NumeroObra = db.Column(db.String)
    ComplementoObra = db.Column(db.String)
    codigo_cliente_omie = db.Column(db.String)
    bitAtivo = db.Column(db.Boolean, unique=False, nullable=False)
    IdSistema = db.Column(db.Integer)

    def __repr__(self):
        return f"idcliente - > {self.IdCliente}, NomeCliente - >{self.NomeCliente}"

    
class EnderecoPedidos(db.Model):
    __tablename__ = "EnderecoPedidos"
    __table_args__ = {"schema": "Pedidos"}
    IdEndPedido = db.Column(db.Integer, primary_key=True)
    CodigoPedido = db.Column(db.Integer)
    IdCliente = db.Column(db.Integer)
    Endereco = db.Column(db.String)
    Numero = db.Column(db.String)
    Bairro = db.Column(db.String)
    Cep = db.Column(db.String)
    Complemento = db.Column(db.String)
    IdCidade = db.Column(db.Integer)
    DataCadastro = db.Column(db.DateTime, unique=False, nullable=False)
    InseridoPor = db.Column(db.String)
    DataAlteracao = db.Column(db.DateTime, unique=False, nullable=False)
    bitAtivo = db.Column(db.Boolean, unique=False, nullable=False)
    AlteradoPor = db.Column(db.String)
    Celular = db.Column(db.String)
    Observacao = db.Column(db.String)
    bitShowRoom = db.Column(db.Boolean, unique=False, nullable=False)
    bitNumeroValido = db.Column(db.Boolean, unique=False, nullable=False)

