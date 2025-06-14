#Importar as bilbiotecas necessárias
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

plt.rcParams["backend"] = "TkAgg"

#Definindo, nomeando a função e passando o parâmetro com um df do pandas
def gerar_grafico_total_venda_cliente(Total_Venda_Cliente, ax):
    #Gerando um gráfico de barras
    sns.barplot(x='Cliente', y='Total vendido por cliente', data=Total_Venda_Cliente, ax=ax) #Define o tipo do gráfico, o eixo x e y e de onde virá os dados
    ax.set_title('Total Vendido por Cliente', fontsize=10) #Define o título
    ax.set_xlabel('Cliente', fontsize=3) #Define o rótulo do eixo x
    ax.set_ylabel('Total Vendido', fontsize=3) #Define o róttulo do eixo y
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='center') #Pega todos os rótulos do eixo x atual e define a rotação como 45 graus e alinha a direita

#Definindo, nomeando a função e passando o parâmetro com um df do pandas
def gerar_grafico_receita_categoria_produto(Receita_categoria_produto, ax):
    #Gerando um gráfico de linhas
    sns.barplot(x='Categoria', y='Receita Bruta', data=Receita_categoria_produto, ax=ax) #Define o tipo do gráfico, verifica os nomes das colunas e de onde virá os dados
    ax.set_title('Receita por categoria de produto', fontsize=10) #Define o título
    ax.set_xlabel('Categoria do Produto') #Define o rótulo do eixo x
    ax.set_ylabel('Receita Total') #Define o róttulo do eixo y
    ax.set_xticklabels(ax.get_xticklabels(), ha='center') #Define a rotação como 45 graus do eixo x


def gerar_grafico_produtos_mais_vendidos(Produtos_mais_vendidos, ax):
    sns.barplot(x='Produto', y='Quantidade vendida', data=Produtos_mais_vendidos, ax=ax)
    ax.set_title('Produtos Mais Vendidos', fontsize=10)
    ax.set_xlabel('Produto')
    ax.set_ylabel('Quantidade Vendida')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')


def gerar_grafico_vendas_por_mes(Vendas_Mes, ax):
    #Grafico de linha
    sns.lineplot(x='Mês', y='Total de Vendas', data=Vendas_Mes, marker='o', ax=ax)
    ax.set_title('Vendas Totais por Mês', fontsize=10)
    ax.set_xlabel('Mês')
    ax.set_ylabel('Total de Vendas')
    ax.grid(True)
    ax.set_xticklabels(ax.get_xticklabels(), ha='right')

#Criando e exibindo um painel com os 4 gráficos
def exibir_dashboard_1(Total_Venda_Cliente,Receita_categoria_produto):

    #Cria uma figura e determina um conjunto de eixos com 1,2 (linha, colunas) de gráficos e define o tamanho do total da figura em polegadas
    fig, axes = plt.subplots(1,2, figsize=(18,7))

    #Fixa cada gráfico em su determinado eixo
    #[0,0] primeira linha, primeira coluna
    gerar_grafico_total_venda_cliente(Total_Venda_Cliente, axes[0])

    #[0,1] primeira linha, segunda coluna
    gerar_grafico_receita_categoria_produto(Receita_categoria_produto, axes[1])

    #Ajusta o layout para evitar sobreposição, reserva espaço para o título e exibe-o dashboard
    plt.tight_layout()
    #plt.show() #Descomente para visualizar o gráfico diretamente em execução local

def exibir_dashboard_2(Produtos_mais_vendidos, Venda_Mes):
    
    fig, axes = plt.subplots(1,2, figsize=(18,7))

    gerar_grafico_produtos_mais_vendidos(Produtos_mais_vendidos, axes[0])
    gerar_grafico_vendas_por_mes(Venda_Mes, axes[1])

    plt.tight_layout()
    #plt.show() #Descomente para visualizar o gráfico diretamente em execução local
