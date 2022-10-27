

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
        "object_type": f"{kwargs.get('tabela')}", #Nome da tabela
        "sort": "number_field desc",
        "page": 1,
        "size": "10"
        }
      
        response = requests.post(url, json=payload, headers=headers)
        return response.json()
```


##controllers_hausz
```
classe PedidosVendaHausz e HauszMapa Faz inserção de registros e logs
```

```python

class HauszMapa(ABC):
    def call_func_hausz_mapa(self): pass

class PedidosVendaHausz(HauszMapa):
    def __init__(self, dataatual):
        self.dataatual = dataatual

class NotasHausz:
    def __init__(self, pedido, data, unidade):
        self.pedido = pedido
        self.data = data
        self.unidade = unidade

```