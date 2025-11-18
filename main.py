"""
Script principal para análise de sentimentos em tweets sobre narração feminina de futebol
"""

import sys
import os
from src.data_loader import carregar_tweets, filtrar_tweets
from src.analyzer import analisar_sentimento, analisar_sexismo
from src.visualizer import plotar_sentimentos, plotar_sexismo
from src.utils import exibir_estatisticas, salvar_resultados


def main():
    """Função principal"""
    print("=" * 80)
    print("ANÁLISE DE SENTIMENTOS - NARRAÇÃO FEMININA DE FUTEBOL")
    print("=" * 80)
    
    # Solicita arquivo
    if len(sys.argv) > 1:
        arquivo = sys.argv[1]
    else:
        arquivo = input("\nDigite o caminho do arquivo NDJSON: ")
    
    if not os.path.exists(arquivo):
        print(f"\nErro: Arquivo '{arquivo}' não encontrado!")
        sys.exit(1)
    
    # Termos para filtrar (pode ser movido para config.py)
    termos_procurados = ["mulher narrando", "narradora", "renata silveira"]
    
    # Extração e filtro
    print("\nCarregando tweets...")
    df = carregar_tweets(arquivo)
    print(f"✓ Total de tweets extraídos: {len(df)}")
    
    print(f"\n Aplicando filtros: {', '.join(termos_procurados)}")
    df_filtrado, textos_filtrados = filtrar_tweets(df, termos_procurados)
    print(f"✓ Tweets filtrados: {len(df_filtrado)} ({len(df_filtrado)/len(df)*100:.1f}%)")
    
    if len(df_filtrado) == 0:
        print("\n Nenhum tweet encontrado com os termos especificados!")
        sys.exit(0)
    
    # Análises
    df_sent = analisar_sentimento(textos_filtrados)
    df_hate = analisar_sexismo(textos_filtrados)
    
    # Visualizações
    plotar_sentimentos(df_sent)
    plotar_sexismo(df_hate)
    
    # Estatísticas
    exibir_estatisticas(df_filtrado, df_sent, df_hate, termos_procurados)
    
    # Salvar resultados
    salvar_resultados(df_filtrado, df_sent, df_hate)
    
    print("\n" + "=" * 80)
    print("ANÁLISE CONCLUÍDA!")
    print("=" * 80)


if __name__ == "__main__":
    main()
