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
        "size": "2"
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": f"{API_KEY_JESTOR}"
        }
        print(kwargs.get('tabela'))
        response = requests.post(url, json=payload, headers=headers)
        strs = response.json()
        try:
            for items in strs:
                dicts = strs[items]
                if isinstance(dicts, dict):
                    dict_items = dicts.get('items')
                    for values in dict_items:
                        if next(filter(lambda k: len(k) > 0, values), None):
                            yield values.get('codigo_pedido')
        
        except Exception as e:
            print("error", e)

    return get_jestor_notafiscal


class JestorHausz(Jestor):
    def __init__(self, data, pedido, cliente, nf, status, tabela):
        self.data = data
        self.pedido = pedido
        self.cliente = cliente
        self.nf=nf
        self.status = status
        self.tabela = tabela

    @api_get_jestor
    def get_api_jestor(self, *args: tuple, **kwargs: dict[str, Any]) -> dict[str, Any]:

        return kwargs
        
    
    def registra_log_jestor(self, *agrs, **kwargs) -> None:pass

    def insert_valores_jestor(self, *args: tuple, **kwargs: dict[str, Any]): pass

    def check_pedido_venda_jestor(self) -> None:pass


    def check_pedido_compras_jestor(self) -> None:pass

    def check_notas_jestor(self) -> None:pass


    

    





    
    