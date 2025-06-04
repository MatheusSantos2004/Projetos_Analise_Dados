import pandas as pd #Importa a biblioteca do pandas

# Caminho do arquivo Excel
base_convo = r"C:\Users\Mathe\OneDrive\Área de Trabalho\Projeto Convocação\Base de Dados Excel\Convocação.xlsx"

# Leitura das planilhas
df_jogadores = pd.read_excel(base_convo, sheet_name='Jogadores')
df_clubes = pd.read_excel(base_convo, sheet_name='Clubes')
df_esta = pd.read_excel(base_convo, sheet_name='Estatisticas_24_25')

# Remove colunas 'Unnamed:'
def limpar_unnamed_columns(df):
    cols_a_pular = [col for col in df.columns if not col.startswith('Unnamed:')]
    return df[cols_a_pular]

df_jogadores = limpar_unnamed_columns(df_jogadores)
df_clubes = limpar_unnamed_columns(df_clubes)
df_esta = limpar_unnamed_columns(df_esta)

# Junta os dataframes
jogadores_clubes = pd.merge(df_jogadores, df_clubes, on='Id_Clube', how='inner')
jogadores_completo = pd.merge(jogadores_clubes, df_esta, on='Id_Jogador', how='inner')

# Remove colunas desnecessárias
jogadores_completo = jogadores_completo.drop(['Id_Clube', 'Id_Jogador'], axis=1)

# Resultado final
jogadores_completo
