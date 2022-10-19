import requests
from datetime import datetime
import os
from dotenv import load_dotenv


load_dotenv()

API_KEY_JESTOR = os.getenv('API_KEY_JESTOR')

def data_atual():
    now = str(datetime.now()).split()[0]
    return now

dataa = "2022-09-10"

def pedidos_vendas_hausz(*args, **kwargs):
    url = "https://supply.api.jestor.com/object/list"

    payload = {
        "object_type": "pedidos_hausz",
        "sort": "number_field desc",
        "page": 1,
        "size": "100",
        "filters": [
            {
                "field": "criado_em",
                "operator": ">=",
                "value": f"{dataa}"
            }
        ]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f"{API_KEY_JESTOR}"
    }

    response = requests.post(url, json=payload, headers=headers)

    strs = response.json()
    dicts = strs['data']
    dict_item = dicts.get('items')
    for items in  dict_item:
        dict_pedido = {}
        if items.get('criado_em'):
            dict_pedido['CodigoPedido'] = items.get('codigopedido')
            dict_pedido['CriadoEm'] = items.get('criado_em')
            dict_pedido['PedidoPai'] = items.get('pedidopai')
            dict_pedido['StatusPedido'] = items.get('status_pedido')
            unidade = items.get('unidade')
            dict_pedido.update(unidade)
            if dict_pedido['CodigoPedido'] == f"{kwargs.get('codigo_pedido')}":
                yield dict_pedido



def get_item_jestor():

    url = "https://supply.api.jestor.com/object/list"
    payload = {
            "object_type": "pedidos_itens_hausz",
            "sort": "number_field desc",
            "page": 1,
            "size": "100"
            }
    headers = {
                "accept": "application/json",
                "content-type": "application/json",
                "Authorization": f"{API_KEY_JESTOR}"
            }

    lista_coluna = []
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

def retorna_jsons_pedidos():
    items = get_item_jestor()
    for pedidos in items:
        
        pedido_dict = {}

        if isinstance(pedidos, dict):
            ref_pedido = pedidos.get('codigo_pedido')
            jsons_pedidos = next(pedidos_vendas_hausz(codigo_pedido = ref_pedido.get('codigopedido')))
            pedido_dict['REFERENCIA_UNIDADE'] = jsons_pedidos.get('name')
            pedido_dict['CRIADO_POR'] = jsons_pedidos.get('criado_por')
            pedido_dict['NOME_FRANQUIA'] = jsons_pedidos.get('nome')
            pedido_dict['CRIADO_EM'] = jsons_pedidos.get('criado_em')
            pedido_dict['ATUALIZADO_EM'] = jsons_pedidos.get('atualizado_em')
            pedido_dict['EMPRESA'] = jsons_pedidos.get('empresa')
            pedido_dict['UNIDADE_BANCO'] = jsons_pedidos.get('idunidadebanco')
            pedido_dict['jestor_object_label'] = jsons_pedidos.get('jestor_object_label')
            pedido_dict['EMAIL'] = jsons_pedidos.get('email')
            pedido_dict['REFERENCIA_FRANQUIA'] = jsons_pedidos.get('name')
            pedido_dict['CODIGO_PEDIDO_PAI'] = jsons_pedidos.get('PedidoPai')
            pedido_dict['STATUS_PEDIDO'] = jsons_pedidos.get('StatusPedido')
            pedido_dict['ID_UNIDADE'] = jsons_pedidos.get('id_unidades')

            pedidos.update(pedido_dict)
            yield pedidos

pedidos_values = retorna_jsons_pedidos()
for pedido in pedidos_values:
    print(pedido)
