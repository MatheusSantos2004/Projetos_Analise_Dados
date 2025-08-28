#Importando as bibliotecas
import pandas as pd
import mysql.connector
import warnings

warnings.filterwarnings('ignore')

conexao = None #Inicializa a variável, garantindo a sua existência

#Fazer conexão com o banco de dados MySQL
try:
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '098123',
        database = 'dados_desemprego_brasil'
    )

    if conexao.is_connected():
        print("Conexão ao banco de dados estabelecida com sucesso")

#Acesse a base de dados, faz a busca e lê os dados com base na querie e salva em uma variável
    Dados_2024 = pd.read_sql("Select * from dados_2024", conexao)
    Dados_2025 = pd.read_sql("Select * from dados_2025", conexao)
    Dados_Desemprego_Estados_2025 = pd.read_sql("Select * from dados_desemprego_estados_2025", conexao)

#Junta os dados das duas tabelas Dados_2024 e Dados_2025 e depois exclui a coluna
    Dados_Desemprego = pd.concat([Dados_2024, Dados_2025], ignore_index= True)
    Dados_Desemprego = Dados_Desemprego.drop(['Id_registro'], axis= 1)

#Remove colunas em branco e nulas do dados, exclui duplicados e reseta o índice
    Dados_Desemprego_Estados_2025 = Dados_Desemprego_Estados_2025[
        ~((Dados_Desemprego_Estados_2025['Taxa_1Trimestre'] == 0.0)&
          (Dados_Desemprego_Estados_2025['Taxa_2Trimestre'] == 0.0))
    ]

    Dados_Desemprego_Estados_2025 = Dados_Desemprego_Estados_2025.drop_duplicates(subset=['Estado_UF'], keep='first')

    Dados_Desemprego_Estados_2025 = Dados_Desemprego_Estados_2025.drop(['Id_Registro'], axis= 1)

    Dados_Desemprego_Estados_2025 = Dados_Desemprego_Estados_2025.reset_index(drop= True)

#Caso a conexão falhe
except mysql.connector.Error as err:
    if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR: #Erro de usuário e senha
        print("Algo está errado com seu nome de usuário ou senha.")
    elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR: #Erro de banco de dados inexistentes
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

# Exportar para CSV
Dados_Desemprego.to_csv(r"C:\Users\Mathe\OneDrive\Área de Trabalho\Projetos Dados\Projeto_Desemprego\Dados_CSV\Dados_Desemprego.csv", index=False, encoding='utf-8-sig')
Dados_Desemprego_Estados_2025.to_csv(r"C:\Users\Mathe\OneDrive\Área de Trabalho\Projetos Dados\Projeto_Desemprego\Dados_CSV\Dados_Desemprego_Estados_2025.csv", index=False, encoding='utf-8-sig')

print("Exportação concluída com sucesso!")
