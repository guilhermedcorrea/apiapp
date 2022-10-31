import json
import requests
import shlex
import json
import subprocess
import urllib.request, urllib.error, urllib.parse
import urllib.request
import certifi
from io import BytesIO
from urllib.parse import urlencode
from typing import Generator, Any, Literal
from itertools import chain



def get_nota_saida_omie(idnota) -> Generator[Any, None, None]:

    valor = r"""curl -s https://app.omie.com.br/api/v1/produtos/nfconsultar/ -H 'Content-type: application/json' -d '{"call":"ConsultarNF","app_key":"1566467100198","app_secret":"8f7c2ebf7899831ecce7c488e69a3e33","param":[{"nCodNF":0,"nNF":"618"}]}'"""
    new_val = valor.replace('"nNF":"618"',f'"nNF":"{idnota}"')
    lCmd = shlex.split(new_val)
    p = subprocess.Popen(lCmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    json_data = json.loads(out.decode("utf-8"))
    yield json_data


def get_recebimento_nf(chave) -> Generator[Any, None, None]:

    valor = r"""curl -s https://app.omie.com.br/api/v1/produtos/recebimentonfe/ -H 'Content-type: application/json' -d '{"call":"ConsultarRecebimento","app_key":"1566467100198","app_secret":"8f7c2ebf7899831ecce7c488e69a3e33","param":[{"nIdReceb":0,"cChaveNfe":""}]}'"""
    new_val = valor.replace('cChaveNfe":""',f'cChaveNfe":"{chave}"')
    lCmd = shlex.split(new_val)
    p = subprocess.Popen(lCmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    json_data = json.loads(out.decode("utf-8"))
    yield json_data
   


def get_valores(valor) -> (Literal['list', 'DICT'] | None):
    match valor:
        case valor if type(valor)  == list:
            return ('list')
        
        case valor if type(valor) == dict:
            return ('DICT')
        
        case _:
            
            print("teste")

def notas_entrada_omie(pag: Any) -> Generator[Any, None, None]:
    valor = r"""curl -s https://app.omie.com.br/api/v1/produtos/recebimentonfe/ -H 'Content-type: application/json' -d '{"call":"ListarRecebimentos","app_key":"1566467100198","app_secret":"8f7c2ebf7899831ecce7c488e69a3e33","param":[{"nPagina":1,"nRegistrosPorPagina":2}]}'"""
    new_val = valor.replace('"nPagina":1,',f'"nPagina":{pag},')
    lCmd = shlex.split(new_val)
    p = subprocess.Popen(lCmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)



    out, err = p.communicate()
    json_data = json.loads(out.decode("utf-8"))
    yield json_data

for i in range(1, 10):
    jsons = notas_entrada_omie(i)

    for items in jsons:
        new_item = items.get('recebimentos')
        for new in new_item:
            item = new.keys()
           
            for key in item:
                produtos_nota = {}
                nfentrada = new[key]
               
                if isinstance(nfentrada.get('cChaveNFe'), str):
                    
                    chave_nfe = nfentrada.get('cChaveNFe')
                   
                    jsons = next(get_recebimento_nf(chave_nfe))
                    resultado = get_valores(jsons)
               
                    
                    '''
                    #for key in next(jsons).keys():
                    for keys, values in next(jsons).items():
                        if isinstance(values, list):
                            print(values)
                        try:
                            refs = values.keys()
                            for item in refs:
                                print(item)
                                dicts = {}
                                if isinstance(item, dict):
                                    dicts[item] = values[item]
                                
                                   
                                                            
                        except:
                            pass
                       
                    '''      
                            
   
