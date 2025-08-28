Create Database Dados_Desemprego_Brasil;
Use Dados_Desemprego_Brasil;

create table Dados_2024
(Id_registro int primary key auto_increment,
Ano int,
Trimestre_num int,
Periodo varchar(20),
Qtd_Desempregados bigint,
Qtd_Empregados bigint,
Forca_trabalho bigint);

create Table Dados_2025
(Id_registro int primary key auto_increment,
Ano int,
Trimestre_num int,
Periodo varchar(20),
Qtd_Desempregados bigint,
Qtd_Empregados bigint,
Forca_trabalho bigint);

Insert into Dados_2024
values
(default, 2024, 3, "Julho - Setembro", 7000000, 102375000, 109375000);
Insert into Dados_2024
values
(default, 2024, 4, "Outubro - Dezembro", 6800000, 103700000, 110500000);
Insert into Dados_2025
values
(default, 2025, 1, "Janeiro - Março", 7700000, 102500000, 110200000);
Insert into dados_2025
values
(default, 2025, 2, "Abril - Junho", 6300000, 102300000, 108600000);

Create Table Dados_Desemprego_Estados_2025
(Id_Registro int primary key auto_increment,
Estado_UF varchar(25), 
Taxa_1Trimestre float,
Taxa_2Trimsetre float,
Situação varchar(10));

insert Into Dados_Desemprego_Estados_2025
values
(default, "Acre-AC", 8.2, 7.3, "Estável");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Acre-AC", 8.2, 7.3, "Estável");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Acre-AC", 8.2, 7.3, "Estável");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Acre-AC", 8.2, 7.3, "Estável");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Alagoas-AL", 9.0, 7.5, "Queda");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Amapá-AP", 8.6, 6.9, "Queda");
insert Into Dados_Desemprego_Estados_2025
values
(default, " ", 0, 0, " ");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Amazonas-AM", 10.0, 7.7, "Queda");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Bahia-BA", 11.1, 9.1, "Queda");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Bahia-BA", 11.1, 9.1, "Queda");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Bahia-BA", 11.1, 9.1, "Queda");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Ceará-CE", 8.0, 6.6, "Queda");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Distrito Federal-DF", 9.2, 8.7, "Estável");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Espírito Santo-ES", 4.0, 3.1, "Queda");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Goiás-GO", 5.3, 4.4, "Queda");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Maranhão-MA", 8.1, 6.6, "Queda");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Mato Grosso-MT", 11.1, 9.1, "Estável");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Mato Grosso-MT", 11.1, 9.1, "Estável");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Mato Grosso do Sul-MS", 4.0, 2.9, "Queda");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Minas Gerais-MG", 5.7, 4.0, "Queda");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Mato Grosso-MT", 11.1, 9.1, "Estável");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Pará-PA", 8.7, 6.9, "Queda");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Paraíba-PB", 8.7, 7.0, "Queda");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Paraná-PR", 4.0, 3.8, "Estável");
insert Into Dados_Desemprego_Estados_2025
values
(default, " ", 0, 0, "");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Pernambuco-PE", 11.6, 10.4, "Estável");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Piauí-PI", 10.2, 8.5, "Queda");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Rio de Janeiro-RJ", 9.3, 8.1, "Queda");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Rio Grande do Norte-RN", 9.9, 7.5, "Queda");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Rio Grande do Sul", 5.3, 4.3, "Queda");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Rondônia-RO", 3.1, 2.3, "Estável");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Roraima-RR", 7.5, 5.9, "Estável");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Santa Catarina", 3.0, 2.2, "Queda");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Mato Grosso-MT", 11.1, 9.1, "Estável");
insert Into Dados_Desemprego_Estados_2025
values
(default, "São Paulo-SP", 6.3, 5.1, "Queda");
insert Into Dados_Desemprego_Estados_2025
values
(default, "São Paulo-SP", 6.3, 5.1, "Queda");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Sergipe-SE", 9.3, 8.1, "Estável");
insert Into Dados_Desemprego_Estados_2025
values
(default, "Tocantins-TO", 6.4, 5.3, "Estável");
