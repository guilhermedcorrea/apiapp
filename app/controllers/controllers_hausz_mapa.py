
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import Integer
from ..extensions import db
from sqlalchemy import text


def executa_select(*args, **kwargs):
  
    """Retorna Dicionarios Pedidos"""
    for arg in args:
        with db.engine.begin()  as conn:
            
            try:
                exec = (text("""EXEC GetOrders @refpedido = {}""".format(int(arg))))
                exec_produtos = conn.execute(exec)
                query_dicts = [{key: value for (key, value) in row.items()} for row in exec_produtos]
                yield query_dicts
            except Exception as e:
                print(e)

      
      
