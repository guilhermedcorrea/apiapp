
from ..extensions import db

class UsersGroup(db.Model):
    __tablename__ = "UsersGroup"
    __bind_key__ = 'HauszMapaDev2'
    __table_args__ = {"schema": "dbo"}
    id_grupo = db.Column(db.Integer, primary_key=True)
    nome_grupo = db.Column(db.String)
    bitativo = db.Column(db.Boolean, unique=False, nullable=False)
    datacadastro = db.Column(db.Column(db.DateTime, unique=False, nullable=False))



class Users(db.Model):

    __tablename__ = "Users"
    __bind_key__ = 'HauszMapaDev2'
    __table_args__ = {"schema": "dbo"}
    id_usuario = db.Column(db.Integer, primary_key=True)
    id_grupo = db.Column(db.Integer)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    password_hash = db.Column(db.String)
    bitusuario = db.Column(db.Boolean, unique=False, nullable=False)
    bitlogado = db.Column(db.Boolean, unique=False, nullable=False)
    datalogado = db.Column(db.Column(db.DateTime, unique=False, nullable=False)
    datacadastro = db.Column(db.Column(db.DateTime, unique=False, nullable=False))
    grupo = db.Column(db.String)
    status_login = db.Column(db.String)
 