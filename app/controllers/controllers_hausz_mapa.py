
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import Integer
from ..extensions import db
from sqlalchemy import text


def executa_select():
    with db.engine.connect() as conn:

        get_pedidos = (text("""
            SELECT DISTINCT cliente.NomeCliente,pbasico.[IdProduto],pbasico.[SKU],pbasico.[NomeProduto]
                ,pbasico.[EAN],pbasico.[NCM],pbasico.[CEST],pmarca.Marca     
                ,pbasico.[IdMarca] ,pbasico.[IdSubCat],pbasico.[EstoqueAtual],pbasico.[SaldoAtual]
                ,pbasico.[PesoCubado]  ,pbasico.[Peso],pdetalhes.[SKU],pdetalhes.[TamanhoBarra]
                ,pdetalhes.[Unidade],pdetalhes.[FatorVenda],pdetalhes.[FatorMultiplicador]
                ,pdetalhes.[FatorUnitario] ,pdetalhes.[Garantia] ,pdetalhes.[Comprimento]
                ,pdetalhes.[Largura],pdetalhes.[Altura] ,pdetalhes.[Peso],iflexy.[IdPedidoItensFlexy]
                ,iflexy.[CodigoPedido] ,iflexy.[Quantidade] ,iflexy.[QuantidadeReservada]
                ,iflexy.[QtdCaixa],iflexy.[PrecoUnitario],iflexy.[IdProduto],iflexy.[SKU],iflexy.[CodigoReferencia]
                ,iflexy.[IdEndEntregaFlexy],iflexy.[LocalEstoque] ,iflexy.[Transportador] 
                ,iflexy.[Observacoes],iflexy.[MvaOriginal],iflexy.[MvaAjustado] ,iflexy.[AliquotaInterna]  
                ,iflexy.[AliquotaExterna],iflexy.[TaxaFrete],iflexy.[IPI],iflexy.[IdPropriedadesPedidoFlexy],iflexy.[IdEstoque] 
                ,iflexy.[DescontoItem],iflexy.[PrecoUnitarioDescontado] ,iflexy.[DataInserido],iflexy.[CodigoPedidoCompra]
                ,iflexy.[CustoUnitario],iflexy.[PedidoPai],iflexy.[CodigoPedidoCompra2]
                ,cliente.[IdCliente],cliente.[NomeCliente],cliente.[IdUsuario]
                ,cliente.[IdUnidade],cliente.[CpfCnpj]
                ,pflexy.[IdPedidoFlexy],pflexy.[IdOrcamento],pflexy.[CodigoPedido],pflexy.[PrecoFrete]
                ,pflexy.[StatusPedido] ,pflexy.[IdPromocaoFlexy],pflexy.[IdCliente],pflexy.[IdColaborador]
                ,pflexy.[Comissao] ,pflexy.[IdUnidade],pflexy.[IdFormaPagamento],pflexy.[IdAtributo],pflexy.[ValorTotal]
                ,pflexy.[IdEtapaFlexy],pflexy.[Desconto],pflexy.[ValorEntrada],pflexy.[DataInserido],pflexy.[BitSplit]
                ,pflexy.[ValorTotalDescontado],pflexy.[Split],pflexy.[Margem],pflexy.[WmsEtapa]
                ,pflexy.[NumPedidoFornecedor],pflexy.[PedidoPai]
                ,pflexy.[bitDesconto],pflexy.[bitAtualizadoStatus],pflexy.[NomePedido],pflexy.[OrigemPedido]
                ,pflexy.[DesmPedido] ,pflexy.[IdEspecialista] ,pflexy.[IdOrderJet],
                unfranquia.[IdUnidade],unfranquia.[Nome] as 'FranquiaRealizouVenda',unfranquia.[IdCidade] as 'IdFranquiaVenda'
                ,unfranquia.[IdPraca] as 'IdPRacaFranquiaVenda'
                ,unfranquia.[IdPracaNovo]
                ,unfranquia.[UF] as 'UFranquiaVenda',unfranquia.[Email] as 'EmailFranquiaVenda'
                ,unfranquia.[TaxaAdministrativa],unfranquia.[TaxaLogistica]
                ,unfranquia.[RazaoSocial] as 'RazaoSocialFranquiaVenda'
                ,pflexy.[IdSistema],pflexy.[IdCardJestor],
                ecliente.Bairro, ecliente.Endereco, ecliente.Complemento, ecliente.Cep, ecliente.Numero
                , ecliente.Observacao,ecliente.IdCidade,ccidade.Nome, escliente.Nome
                FROM [HauszMapa].[Pedidos].[ItensFlexy] as iflexy
                JOIN [HauszMapa].[Produtos].[ProdutoDetalhe] as pdetalhes
                ON pdetalhes.IdProduto = iflexy.IdProduto
                JOIN [HauszMapa].[Pedidos].[PedidoFlexy] as pflexy
                ON pflexy.CodigoPedido = iflexy.CodigoPedido
                JOIN [HauszLogin].[Cadastro].[Cliente] as cliente
                ON cliente.IdCliente = pflexy.IdCliente
                JOIN [HauszLogin].[Cadastro].[Unidade] as unfranquia
                ON unfranquia.IdUnidade = pflexy.IdUnidade
                JOIN [HauszMapa].[Produtos].[ProdutoBasico] as pbasico
                ON pbasico.SKU = pdetalhes.[SKU]
                JOIN [HauszMapa].[Pedidos].[EnderecoPedidos] as enderecopedido
                ON enderecopedido.IdCliente = pflexy.IdCliente
                JOIN [HauszMapa].[Produtos].[Marca] as pmarca
                ON pmarca.[IdMarca] = pbasico.IdMarca
                JOIN [HauszMapa].[Pedidos].[EnderecoPedidos] AS ecliente
                ON ecliente.IdCliente = cliente.IdCliente
                JOIN [HauszMapa].[Cadastro].[Cidade] as ccidade
                ON ccidade.IdCidade = ecliente.IdCidade
                JOIN [HauszMapa].[Cadastro].[Estado] as escliente
                ON escliente.IdEstado = ccidade.IdEstado
                WHERE convert(date,iflexy.[DataInserido])  =  convert(date,getdate())"""))

        exec_produtos = conn.execute(get_pedidos).all()

        query_dicts = [{key: value for (key, value) in row.items()} for row in exec_produtos]
        yield query_dicts
       
