
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import Integer
from ..extensions import db
from sqlalchemy import text


def executa_select(*args, **kwargs):
    """Retorna Dicionarios Pedidos"""
    with db.engine.begin()  as conn:
        
        try:
            exec = (text("""EXEC GetOrders @refpedido = {}""".format(int(kwargs.get('pedido')))))
            exec_produtos = conn.execute(exec)
            query_dicts = [{key: value for (key, value) in row.items()} for row in exec_produtos]
            yield query_dicts
        except:
            print("error")

      
       
