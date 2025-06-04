-- Criação do banco de dados
Create database if not exists LojaVendas;
use lojavendas;

-- Tabela de Clientes
Create table Clientes
(id_cliente int auto_increment primary key,
nome varchar(100),
email varchar(100),
cidade varchar(50),
estado varchar(2),
data_cadastro DATE);

-- Tabela de Produtos
Create Table Produtos
(id_produto int auto_increment primary key,
nome varchar(100),
categoria varchar(50),
preco Decimal(10,2),
estoque int);

-- Tabela de Vendas
Create Table Vendas
(id_venda int auto_increment primary key,
id_cliente int,
data_venda Date,
forma_pagamento varchar(20),
foreign key (id_cliente) references Clientes(id_cliente));

-- Tabela de Itens de Venda
Create Table ItensVenda
(id_item int auto_increment primary key,
id_venda int,
id_produto int,
quantidade int,
preco_unitario decimal(10,2),
foreign key (id_venda) references Vendas(id_cliente),
foreign key (id_produto) references Produtos(id_produto));