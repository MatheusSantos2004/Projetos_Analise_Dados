-- View de Total vendido por cliente
Create view Total_vendido_por_cliente as
select c.Nome as Cliente, sum(iv.preco_unitario * iv.quantidade) as 'Total vendido por cliente' 
from clientes c inner join vendas v on c.id_cliente = v.id_cliente 
inner join itensvenda iv on v.id_venda = iv.id_venda group by c.nome;

-- View de Receita por categoria de produto
Create view Receita_categoria_de_produto as
select p.categoria as Categoria, sum(iv.preco_unitario * iv.quantidade) as 'Receita Bruta'
from produtos p inner join itensvenda iv
on p.id_produto = iv.id_produto group by p.categoria;

-- View de Produtos mais vendidos
Create view Produtos_mais_vendidos as
select p.nome as Produto, sum(iv.quantidade) as 'Quantidade vendida' from produtos p inner join itensvenda iv
on p.id_produto = iv.id_produto group by p.nome;

-- View Vendas por mês
Create view Vendas_por_mês as
select monthname(data_venda) as Mês, count(id_venda) as 'Total de Vendas' from vendas 
group by month(data_venda), monthname(data_venda)
order by month(data_venda);