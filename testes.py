from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from config import SECRET_KEY, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_BINDS
from sqlalchemy import func, select


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_POOL_SIZE'] = 370
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0


db = SQLAlchemy(app)

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


'''
def testes():
    with db.engine.connect() as conn:
        transactions_data = conn.execute(select(func.strftime('%', PedidoFlexy.DataInserido)
                    ,func.sum(PedidoFlexy.DataInserido)).group_by()).all()
        print(transactions_data)
testes()
'''


'''

        query = (text("""
            SELECT DISTINCT *FROM [HauszMapa].[Pedidos].[PedidoFlexy] AS PFLEXY
            JOIN [HauszMapa].[Pedidos].[EnderecoPedidos]AS EPEDIDO
            ON EPEDIDO.Idcliente = PFLEXY.IdCliente
            JOIN [HauszMapa].[Cadastro].[Cidade] as ccidade
            ON ccidade.IdCidade = EPEDIDO.IdCidade
            JOIN [HauszMapa].[Cadastro].[Estado] as cestado
            ON cestado.IdEstado = ccidade.IdEstado
            WHERE convert(date,PFLEXY.[DataInserido])  =  '2022-10-18'
            AND PFLEXY.StatusPedido ='Em separação'"""))
        teste = conn.execute(query).all()
      
        query_dicts = [{key: value for (key, value) in row.items()} for row in teste]
        for pedidos in query_dicts:
          
            jsons = executa_select(pedido = pedidos.get('CodigoPedido'))
            dict_items = next(chain(jsons))
            #print(dict_items)
            dict_items = sorted(dict_items, key=group_keys)
            for key, value in groupby(dict_items, group_keys):
                #cont = len(list(value))
                dicts = verifica_dict(list(value))
                dicts.update(pedidos)
                lista_pedidos.append(dicts)
    
    emissao_nf(lista_pedidos,API_KEY_EMISSAO,COMPANY_ID_EMISSAO)
    return make_response(jsonify({'EmitindoNFE':lista_pedidos})),201
'''