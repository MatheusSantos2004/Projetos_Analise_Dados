import pandas as pd

def traduzir_e_ordenar_meses(Vendas_mes):
    # Cria o dicionário de mapeamento dos meses (tradução)
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

    if 'Mês' not in Vendas_mes.columns:
        print("Aviso: Coluna 'Mês' não encontrada no DataFrame.")
        return Vendas_mes

    # Traduz os meses de inglês para português
    Vendas_mes['Mês'] = Vendas_mes['Mês'].map(meses_em_portugues).fillna(Vendas_mes['Mês'])

    # Ordena os meses cronologicamente
    ordem_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    
    # Trata os casos onde alguns meses podem não existir no DataFrame
    Vendas_mes['Mês'] = pd.Categorical(Vendas_mes['Mês'], categories=ordem_meses, ordered=True)

    # Ordena o DataFrame pela nova coluna categórica 'Mês'
    Vendas_mes = Vendas_mes.sort_values('Mês')

    return Vendas_mes
