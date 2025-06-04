#Importar as bibliotecas
import pandas as pd
import mysql.connector
import warnings

#Importa as funções de dashboards do arquivo graficos.py
from graficos import exibir_dashboard_1
from graficos import exibir_dashboard_2

#Importa a função de tradução do arquivo transformacoes.py
from transformacoes import traduzir_e_ordenar_meses

warnings.filterwarnings('ignore')

#Inicializa as variáveis dos DFs fora do try
Total_Venda_Cliente = None
Receita_categoria_produto = None
Produtos_mais_vendidos = None
Vendas_Mes = None
conexao=None #Inicializa a variável, garantindo que exista

#Fazer a conexão com o banco de dados MySQL
try:
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '098123',
        database = 'lojavendas'
    )

    if conexao.is_connected():
        print("Conexão ao banco de dados estabelecida com sucesso")

    #Criando os DataFrames, lendo as views e inserindo os dados em arquivos csv
    Total_Venda_Cliente = pd.read_sql("Select * from Total_vendido_por_cliente", conexao)
    Total_Venda_Cliente.to_csv(r'C:\Users\Mathe\OneDrive\Área de Trabalho\Projeto Loja Venda\DadosCSV\Total_Venda_Cliente.csv', index=False)

    Receita_categoria_produto = pd.read_sql("Select * from Receita_categoria_de_produto", conexao)
    Receita_categoria_produto.to_csv(r'C:\Users\Mathe\OneDrive\Área de Trabalho\Projeto Loja Venda\DadosCSV\Receita_categoria_produto.csv', index=False)

    Produtos_mais_vendidos = pd.read_sql("Select * from Produtos_mais_vendidos", conexao)
    Produtos_mais_vendidos.to_csv(r'C:\Users\Mathe\OneDrive\Área de Trabalho\Projeto Loja Venda\DadosCSV\Produtos_mais_vendidos.csv',index=False)

    Vendas_Mes = pd.read_sql("Select * from Vendas_por_mês", conexao)
    Vendas_Mes = traduzir_e_ordenar_meses(Vendas_Mes)
    Vendas_Mes.to_csv(r'C:\Users\Mathe\OneDrive\Área de Trabalho\Projeto Loja Venda\DadosCSV\Venda_Mes.csv', index=False)


    #Chamando a função de transformação de dados para Vendas_Mes
    print("\nProcessando dados de Vendas por Mês...")
    if Vendas_Mes is not None:
        Vendas_Mes = traduzir_e_ordenar_meses(Vendas_Mes)
        print("Processamento de Vendas por Mês concluído.")
    else:
            print("Aviso: Vendas_Mes não foi carregado, pulando processamento de meses.")

    #Chamando a nova função para exibir o dashboard
    print("\nGerando dashboard separados com os gráficos...")
    #Verifica se TODAS cada variável (df) existe e não é nula dentro do df principal
    if all(df is not None for df in [Total_Venda_Cliente, Receita_categoria_produto]):
        exibir_dashboard_1(Total_Venda_Cliente, Receita_categoria_produto)
        print("Geração do dashboard concluída.")
    else:
        print("Aviso: Nem todos os DataFrames foram carregados com sucesso. Dashboard não será exibido.")

    if all(df is not None for df in [Produtos_mais_vendidos, Vendas_Mes]):
        exibir_dashboard_2(Produtos_mais_vendidos, Vendas_Mes)
        print("Geração do dashboard concluída.")
    else:
        print("Aviso: Nem todos os DataFrames foram carregados com sucesso. Dashboard não será exibido.")

#Caso a conexão falhe
except mysql.connector.Error as err:
    if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR: #Erro de usuário e senha
        print("Algo está errado com seu nome de usuário ou senha.")
    elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR: #Erro de banco de dados inexistente
        print("O banco de dados não existe.")
    else:
        print(f"Erro no MySQL: {err}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}") #Erro diferente dos menciandos acima
#Fecha a conexão
finally:
    if conexao and conexao.is_connected():
        conexao.close()
        print("\nConexão ao banco de dados fechada.")