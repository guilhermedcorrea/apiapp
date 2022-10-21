from abc import ABC, abstractmethod
from datetime import datetime
from functools import wraps
from typing import Dict, Tuple, List, Any


def registralog(f):
    @wraps(f)
    def wrapper(*args: tuple, **kwds:dict[str, Any]) -> Any:
        print('Calling decorated function')
        return f(*args, **kwds)
    return wrapper

@registralog
def registro_notas() -> None:
    """Docstring"""
    print('Called function notas')


@registralog
def registro_pedidos() -> None:
    """Docstring"""
    print('Called function pedidos')


class HauszMapa(ABC):
    def call_func_hausz_mapa(self) -> None: pass
     
    def before(self) -> None:pass

    def insert_pedidos_hausz(self) -> None: pass

    @abstractmethod
    def registra_log_hausz(self) -> None: pass

    @abstractmethod
    def registra_log_hausz(self) -> None:pass

    @abstractmethod
    def check_pedido_venda_hausz(self) -> None:pass

    @abstractmethod
    def check_pedido_compras_hausz(self) -> None:pass

    @abstractmethod
    def check_notas_hausz(self) -> None:pass


class Jestor(ABC):
    def __init__(self, data_atual):
        self.data_atual = data_atual

    def call_func_jestor(self) -> None:
        pass

    def insert_pedidos_jestor(self) -> None:
        pass

    @abstractmethod
    def registra_log_jestor(self) -> None:pass

    @abstractmethod
    def check_pedido_venda_jestor(self) -> None:pass

    @abstractmethod
    def check_pedido_compras_jestor(self) -> None:pass

    @abstractmethod
    def check_notas_jestor(self) -> None:pass
