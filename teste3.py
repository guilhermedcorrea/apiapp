item = [{"name":"teste1","valor":30.8,"quantidade":3}
        ,{"name":"teste4","valor":44.8,"quantidade":9}
        ,{"name":"teste2","valor":40.8,"quantidade":30}]

teste = [(x.get('valor') * x.get('quantidade')) for x in item]
print(sum(teste))