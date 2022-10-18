from datetime import datetime
from .base_log import Jestor
from functools import wraps
import requests
from typing import Dict, Tuple, List, Any, Literal
from dotenv import load_dotenv
import os

API_KEY_JESTOR = os.getenv('API_KEY_JESTOR')

"""Ira substituir a função colocada no jestor.py"""
def api_get_jestor(f):
    @wraps(f)
    def get_jestor_notafiscal(*args: tuple, **kwargs: Dict[str, Any]) -> Any:
        print(args, kwargs)
        print('GET JESTOR | METODO GET')
        url = "https://supply.api.jestor.com/object/list"
        payload = {
        "object_type": f"{kwargs.get('tabela')}",
        "sort": "number_field desc",
        "page": 1,
        "size": "10"
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": f"{API_KEY_JESTOR}"
        }
    
        response = requests.post(url, json=payload, headers=headers)
        strs = response.json()
        try:
            for items in strs:
                dicts = strs[items]
                if isinstance(dicts, dict):
                    dict_items = dicts.get('items')
                    for values in dict_items:
                        if next(filter(lambda k: len(k) > 0, values), None):
                            dict_pedidos = {}
                            if type(values) == dict:
                                dict_pedidos.update(values)
                                yield dict_pedidos
                            else:
                                return "Error"
        except Exception as e:
            print("error", e)
             
    return get_jestor_notafiscal

class JestorHausz(Jestor):
    def __init__(self, data = None, pedido = None, cliente = None, nf = None
                 , status = None, tabela = None):
        self.data: datetime = data
        self.pedido: str = pedido
        self.cliente: str = cliente
        self.nf:int = nf
        self.status: str = status
        self.tabela: str = tabela
        self.cont: int = 0

    @api_get_jestor
    def get_api_jestor(self, *args: tuple, **kwargs: dict[str, Any]) -> dict[str, Any]:

        return kwargs
    
    @api_get_jestor
    def get_parametros_nfe(self,*args: Any, **kwargs: dict[str, Any]) -> dict[str, Any]:
        """Parametros entrada notas venda"""
        print('Called function --> NF')
        return kwargs
           
    @api_get_jestor
    def get_pedidos_itens_jestor(self, *args: Any, **kwargs: dict[str, Any]) -> dict[str, Any]:
        """Parametros entrada pedidos itens"""
        print('Called function --> pedidos itens')
        return kwargs
    
    @api_get_jestor
    def get_clientes_jestor(self, *args: Any, **kwargs: dict[str, Any]) -> dict[str, Any]:
        return kwargs
    
    @api_get_jestor
    def get_pedidos_compras_jestor(self, *args: Any, **kwargs: dict[str, Any]) -> dict[str, Any]:
        return kwargs
    
    def registra_log_jestor(self, *agrs, **kwargs) -> None:
        return kwargs

    def insert_valores_jestor(self, *args: tuple, **kwargs: dict[str, Any]) -> None:
        return kwargs

    def check_pedido_venda_jestor(self) -> None:
        return 

    def check_pedido_compras_jestor(self) -> None:
        return 

    def check_notas_jestor(self) -> None:
        return


    

    





    
    