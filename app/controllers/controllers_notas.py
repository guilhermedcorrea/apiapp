from typing import Any
from functools import wraps
import os
from dotenv import load_dotenv
import requests

from typing import Dict, Tuple, List

"""
NOTA FISCAL CONSUMIDOR

"""
load_dotenv()

API_KEY_CONSULTA = os.getenv('API_KEY_CONSULTA')
COMPANY_ID_CONSULTA = os.getenv('COMPANY_ID_CONSULTA')

def get_metodo(f) -> Any:
    @wraps(f)
    def obtem_endpoint(*args: tuple, **kwargs: Dict[str, Any]) -> Any:
        print('Envia requisicao NFE IO CONSULTA | METODO GET')
        url = """https://api.nfse.io/v2/companies/{}/consumerinvoices?environment={}&apikey={}""".format(kwargs.get('compani_id'),kwargs.get('ambiente_nf'),kwargs.get('api_key'))
        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.status_code)
        jsons = response.json()
 
        return jsons
        
    return obtem_endpoint

@get_metodo
def get_parametros(*args: tuple, **kwargs: Dict[str, Any]) -> None:
    """Docstring"""
    print('Called function')


class NotasHausz:
    def __init__(self, pedido, data, unidade, nf):
        self.pedido = pedido
        self.data = data
        self.unidade = unidade
        self.lista_dicts = []

    def seleciona_fields(self, *args: tuple, **kwargs: dict[str, Any]) -> dict[str, Any]:pass

    def get_jsons_api(self): pass

    def emissao_nf(self) -> None: pass

       

        