"""
Módulo para análise de sentimentos e detecção de sexismo
"""

import pandas as pd
from pysentimiento import create_analyzer


def analisar_sentimento(textos):
    """
    Analisa sentimento dos textos usando pysentimiento

    Args:
        textos: lista de textos para análise

    Returns:
        DataFrame com resultados da análise de sentimento
    """
    print("\n[1/3] Analisando sentimentos...")
    analyzer = create_analyzer(task="sentiment", lang="pt")
    
    resultados = []
    total = len(textos)
    
    for i, frase in enumerate(textos, 1):
        if i % 10 == 0 or i == total:
            print(f"  Processados {i}/{total} tweets...")
        
        resultado = analyzer.predict(frase)
        resultados.append({
            "Frase": frase,
            "Sentimento": resultado.output,
            "Positivo": resultado.probas["POS"],
            "Negativo": resultado.probas["NEG"],
            "Neutro": resultado.probas["NEU"]
        })
    
    return pd.DataFrame(resultados)


def analisar_sexismo(textos, limiar=0.20):
    """
    Analisa probabilidade de sexismo nos textos

    Args:
        textos: lista de textos para análise
        limiar: valor mínimo para considerar sexista (padrão: 0.20)

    Returns:
        DataFrame com resultados da análise de sexismo
    """
    print("\n[2/3] Analisando sexismo...")
    analyzer = create_analyzer(task="hate_speech", lang="pt")
    
    resultados = []
    total = len(textos)
    
    for i, frase in enumerate(textos, 1):
        if i % 10 == 0 or i == total:
            print(f"  Processados {i}/{total} tweets...")
        
        resultado = analyzer.predict(frase)
        prob_sexismo = resultado.probas["Sexism"]
        resultados.append({
            "Frase": frase,
            "Probabilidade_Sexismo": prob_sexismo,
            "É_Sexista": prob_sexismo >= limiar
        })
    
    df = pd.DataFrame(resultados)
    
    # Adicionar faixas de probabilidade
    bins = [0, 0.20, 0.40, 0.60, 0.80, 1.0]
    labels = [
        'Muito Baixo (0-20%)', 
        'Baixo (20-40%)', 
        'Médio (40-60%)', 
        'Alto (60-80%)', 
        'Muito Alto (80-100%)'
    ]
    df['Faixa_Sexismo'] = pd.cut(
        df['Probabilidade_Sexismo'], 
        bins=bins, 
        labels=labels, 
        include_lowest=True
    )
    
    return df
