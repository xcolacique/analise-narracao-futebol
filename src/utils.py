"""
Módulo com funções utilitárias para exibição e salvamento de resultados
"""

import os


def exibir_estatisticas(df_filtrado, df_sent, df_hate, termos_procurados):
    """
    Exibe estatísticas das análises no terminal

    Args:
        df_filtrado: DataFrame com tweets filtrados
        df_sent: DataFrame com análise de sentimentos
        df_hate: DataFrame com análise de sexismo
        termos_procurados: lista de termos usados no filtro
    """
    print("\n" + "=" * 80)
    print("RESUMO DA ANÁLISE")
    print("=" * 80)
    
    print(f"\nFiltros aplicados: {', '.join(termos_procurados)}")
    print(f"Total de tweets analisados: {len(df_filtrado)}")
    
    _exibir_estatisticas_sentimento(df_sent)
    _exibir_estatisticas_sexismo(df_hate)


def _exibir_estatisticas_sentimento(df_sent):
    """Exibe estatísticas de sentimento"""
    print("\n" + "-" * 80)
    print("ANÁLISE DE SENTIMENTOS")
    print("-" * 80)
    
    distribuicao = df_sent['Sentimento'].value_counts()
    percentuais = (distribuicao / distribuicao.sum()) * 100
    
    for sentimento in distribuicao.index:
        count = distribuicao[sentimento]
        perc = percentuais[sentimento]
        emoji = _get_emoji_sentimento(sentimento)
        print(f"{emoji} {sentimento}: {count} tweets ({perc:.1f}%)")


def _exibir_estatisticas_sexismo(df_hate):
    """Exibe estatísticas de sexismo"""
    print("\n" + "-" * 80)
    print("⚠️ANÁLISE DE SEXISMO")
    print("-" * 80)
    
    total = len(df_hate)
    sexistas = df_hate['É_Sexista'].sum()
    nao_sexistas = total - sexistas
    
    print(f"Tweets sexistas (≥20%): {sexistas} ({sexistas/total*100:.1f}%)")
    print(f"Tweets não sexistas (<20%): {nao_sexistas} ({nao_sexistas/total*100:.1f}%)")
    
    print(f"\n📈 Estatísticas de probabilidade:")
    print(f"   • Média: {df_hate['Probabilidade_Sexismo'].mean():.2%}")
    print(f"   • Mediana: {df_hate['Probabilidade_Sexismo'].median():.2%}")
    print(f"   • Máxima: {df_hate['Probabilidade_Sexismo'].max():.2%}")
    print(f"   • Mínima: {df_hate['Probabilidade_Sexismo'].min():.2%}")
    
    print(f"\n📊 Distribuição por faixas:")
    faixas = df_hate['Faixa_Sexismo'].value_counts().sort_index()
    for faixa, count in faixas.items():
        perc = (count / total) * 100
        print(f"   • {faixa}: {count} ({perc:.1f}%)")


def _get_emoji_sentimento(sentimento):
    """Retorna emoji correspondente ao sentimento"""
    emojis = {
        'POS': '😊',
        'NEG': '😠',
        'NEU': '😐'
    }
    return emojis.get(sentimento, '❓')


def salvar_resultados(df_filtrado, df_sent, df_hate, output_dir='output'):
    """
    Salva resultados em arquivos CSV

    Args:
        df_filtrado: DataFrame com tweets filtrados
        df_sent: DataFrame com análise de sentimentos
        df_hate: DataFrame com análise de sexismo
        output_dir: diretório para salvar os arquivos
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Salvar DataFrames
    df_filtrado.to_csv(
        f'{output_dir}/tweets_filtrados.csv', 
        index=False, 
        encoding='utf-8'
    )
    df_sent.to_csv(
        f'{output_dir}/analise_sentimentos.csv', 
        index=False, 
        encoding='utf-8'
    )
    df_hate.to_csv(
        f'{output_dir}/analise_sexismo.csv', 
        index=False, 
        encoding='utf-8'
    )
    
    # Criar relatório resumido
    _criar_relatorio_resumo(df_filtrado, df_sent, df_hate, output_dir)
    
    print(f"\nResultados salvos em '{output_dir}/'")
    print(f"   • tweets_filtrados.csv")
    print(f"   • analise_sentimentos.csv")
    print(f"   • analise_sexismo.csv")
    print(f"   • relatorio_resumo.txt")


def _criar_relatorio_resumo(df_filtrado, df_sent, df_hate, output_dir):
    """Cria arquivo de texto com resumo da análise"""
    with open(f'{output_dir}/relatorio_resumo.txt', 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("RELATÓRIO DE ANÁLISE - NARRAÇÃO FEMININA DE FUTEBOL\n")
        f.write("=" * 80 + "\n\n")
        
        f.write(f"Total de tweets analisados: {len(df_filtrado)}\n\n")
        
        # Sentimentos
        f.write("-" * 80 + "\n")
        f.write("DISTRIBUIÇÃO DE SENTIMENTOS\n")
        f.write("-" * 80 + "\n")
        distribuicao = df_sent['Sentimento'].value_counts()
        percentuais = (distribuicao / distribuicao.sum()) * 100
        for sent, count in distribuicao.items():
            f.write(f"{sent}: {count} ({percentuais[sent]:.2f}%)\n")
        
        # Sexismo
        f.write("\n" + "-" * 80 + "\n")
        f.write("ANÁLISE DE SEXISMO\n")
        f.write("-" * 80 + "\n")
        total = len(df_hate)
        sexistas = df_hate['É_Sexista'].sum()
        f.write(f"Tweets sexistas (≥20%): {sexistas} ({sexistas/total*100:.2f}%)\n")
        f.write(f"Tweets não sexistas: {total-sexistas} ({(total-sexistas)/total*100:.2f}%)\n")
        f.write(f"\nProbabilidade média: {df_hate['Probabilidade_Sexismo'].mean():.2%}\n")
        f.write(f"Probabilidade mediana: {df_hate['Probabilidade_Sexismo'].median():.2%}\n")
