from appteste import db
from sqlalchemy import text


def teste():
    with db.engine.connect() as conn:
            query = (text("""
                    SELECT DISTINCT TOP(1) *FROM [HauszMapa].[Pedidos].[PedidoFlexy] AS PFLEXY
                    JOIN [HauszMapa].[Pedidos].[EnderecoPedidos]AS EPEDIDO
                    ON EPEDIDO.Idcliente = PFLEXY.IdCliente
                    JOIN [HauszMapa].[Cadastro].[Cidade] as ccidade
                    ON ccidade.IdCidade = EPEDIDO.IdCidade
                    JOIN [HauszMapa].[Cadastro].[Estado] as cestado
                    ON cestado.IdEstado = ccidade.IdEstado
                    WHERE convert(date,PFLEXY.[DataInserido])  =  '2022-10-24'
                    AND PFLEXY.StatusPedido ='Em separação'"""))
            teste = conn.execute(query).all()
            query_dicts = [{key: value for (key, value) in row.items()} for row in teste]
            for pedidos in query_dicts:
                print(pedidos)

