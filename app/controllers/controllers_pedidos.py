from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy
from typing import Dict, Tuple, List, Any, Generator, Literal

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db


def get_pedidos_flexy() -> List[dict]:
    with db.engine.connect() as conn:
        try:
            get_pedidos = conn.execute(text("""SELECT * FROM [HauszMapa].[Pedidos].[ItensFlexy] AS IFLEXY
                    JOIN [HauszMapa].[Pedidos].[PedidoFlexy] AS PFLEXY
                    ON PFLEXY.CodigoPedido = IFLEXY.CodigoPedido
                    WHERE convert(varchar, PFLEXY.DataInserido,23) =  convert(varchar, GETDATE(),23)""")).all()
             
            dicts_produtos = [{key: value for (key, value) in row.items()} for row in get_pedidos]
            
      

            yield dicts_produtos
        except:
            yield 'notfound'

        