from .base_log import HauszMapa
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy
from typing import Dict, Tuple, List, Any, Generator, Literal
from ..extensions import db


def get_pedidos_flexy() -> List[dict]:

    try:
         with db.engine.begin() as conn:
            exec = (text(""" EXEC GetOrders = {}""".format()))
            exec_produtos = conn.execute(exec)
            dicts_produtos = [{key: value for (key, value) in row.items()} for row in exec_produtos]
            yield dicts_produtos
    except:
        print('erro')
       



