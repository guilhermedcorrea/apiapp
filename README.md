

##cadastra_nf
```
Emissao notas ficais
https://nfe.io/docs/desenvolvedores/rest-api/nota-fiscal-de-produto-v2/#/
```

##consulta_nf
```
NOTA FISCAL CONSUMIDOR
```

##consulta_nf
```
Recebe nome da tabela como parametro pela função wraps


```
```python
exemplo

def get_metodo_nf(f):
    @wraps(f)
    def get_jestor_notafiscal(*args: tuple, **kwargs: Dict[str, Any]) -> Any:
        print(args, kwargs)
        print('Envia requisicao JESTOR CONSULTA | METODO GET')
        url = "https://supply.api.jestor.com/object/list"
        payload = {
        "object_type": f"{kwargs.get('tabela')}",
        "sort": "number_field desc",
        "page": 1,
        "size": "10"
        }
      
        response = requests.post(url, json=payload, headers=headers)
        return response.json()
```
