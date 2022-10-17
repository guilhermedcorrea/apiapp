from ..extensions import db
from sqlalchemy import text


def get_pedidos_flexy():
    with db.engine.connect() as conn:
        try:
            get_pedidos = conn.execute(text("""SELECT  
                *FROM [HauszMapa].[Pedidos].[PedidoFlexy]
                where convert(varchar, DataInserido,23) in ('2022-10-11') and IdEtapaFlexy = 6""")).all()
            dicts_produtos = [{key: value for (key, value) in row.items()} for row in get_pedidos]
            yield dicts_produtos
        except:
            yield 'notfound'

        