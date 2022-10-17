from abc import ABC, abstractmethod
from datetime import datetime
from functools import wraps



def registralog(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)
    return wrapper

@registralog
def registro_notas():
    """Docstring"""
    print('Called function notas')


@registralog
def registro_pedidos():
    """Docstring"""
    print('Called function pedidos')


class HauszMapa(ABC):
    def call_func_hausz_mapa(self): pass
     

    def before(self):pass

    def insert_pedidos_hausz(self): pass

    @abstractmethod
    def registra_log_hausz(self): pass

    @abstractmethod
    def registra_log_hausz(self):pass

    @abstractmethod
    def check_pedido_venda_hausz(self):pass

    @abstractmethod
    def check_pedido_compras_hausz(self):pass

    @abstractmethod
    def check_notas_hausz(self):pass


class Jestor(ABC):
    def __init__(self, data_atual):
        self.data_atual = data_atual

    def call_func_jestor(self):
        pass

    def insert_pedidos_jestor(self):
        pass

    @abstractmethod
    def registra_log_jestor(self):pass

    @abstractmethod
    def check_pedido_venda_jestor(self):pass

    @abstractmethod
    def check_pedido_compras_jestor(self):pass

    @abstractmethod
    def check_notas_jestor(self):pass
