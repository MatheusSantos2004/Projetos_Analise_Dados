import pandas as pd

def traduzir_e_ordenar_meses(Vendas_mes):
    #Cria o dicionário de mapeamento dos meses (tradução)
    meses_em_portugues = {
        'January': 'Janeiro',
        'February': 'Fevereiro',
        'March': 'Março',
        'April': 'Abril',
        'May': 'Maio',
        'June': 'Junho',
        'July': 'Julho',
        'August': 'Agosto',
        'September': 'Setembro',
        'October': 'Outubro',
        'November': 'Novembro',
        'December': 'Dezembro'
    }

    if 'Mês' in Vendas_mes.columns:
        Vendas_mes['Mês'] = Vendas_mes['Mês'].map(meses_em_portugues)
    else:
        print("Aviso: Coluna 'Mês' não encontrada no DataFrame para tradução.")
        return Vendas_mes

    #Ordena os meses cronologicamente
    ordem_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    
    #Trata os caso onde alguns meses podem não existir no DataFrame
    Vendas_mes['Mês'] = pd.Categorical(Vendas_mes['Mês'], categories=ordem_meses, ordered=True)

    # Ordena o DataFrame pela nova coluna categórica 'Mes'
    Vendas_mes = Vendas_mes.sort_values('Mês')

    return Vendas_mes