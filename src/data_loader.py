"""
Módulo para carregamento e filtragem de dados de tweets
"""

import pandas as pd
import json


def carregar_tweets(arquivo_ndjson):
    """
    Extrai dados de tweets em formato NDJSON

    Args:
        arquivo_ndjson: caminho para o arquivo NDJSON

    Returns:
        DataFrame pandas com dados dos tweets
    """
    dados = []

    with open(arquivo_ndjson, 'r', encoding='utf-8') as f:
        for linha in f:
            try:
                tweet = json.loads(linha)

                # Extrai dados
                legacy = tweet.get('data', {}).get('legacy', {})
                tweet_id = tweet.get('data', {}).get('rest_id', '')

                # Extrai screen_name do usuário
                user_results = tweet.get('data', {}).get('core', {}).get('user_results', {})
                user_data = user_results.get('result', {})
                user_legacy = user_data.get('legacy', {})
                screen_name = user_legacy.get('screen_name', '')

                dados.append({
                    'full_text': legacy.get('full_text', ''),
                    'quote_count': legacy.get('quote_count', 0),
                    'reply_count': legacy.get('reply_count', 0),
                    'retweet_count': legacy.get('retweet_count', 0),
                    'favorite_count': legacy.get('favorite_count', 0),
                    'created_at': legacy.get('created_at', ''),
                    'tweet_id': tweet_id,
                    'screen_name': screen_name
                })

            except json.JSONDecodeError as e:
                print(f"Erro ao decodificar linha: {str(e)[:50]}...")
                continue

    return pd.DataFrame(dados)


def contem_termos(texto, termos_busca):
    """
    Verifica se o texto contém algum dos termos da lista

    Args:
        texto: texto para verificar
        termos_busca: lista de termos para buscar

    Returns:
        bool: True se contém algum termo, False caso contrário
    """
    texto_lower = texto.lower()
    return any(termo.lower() in texto_lower for termo in termos_busca)


def filtrar_tweets(df, termos_procurados):
    """
    Filtra tweets baseado em lista de termos

    Args:
        df: DataFrame com tweets
        termos_procurados: lista de termos para filtrar

    Returns:
        Tupla (DataFrame filtrado, lista de textos)
    """
    df_filtrado = df[df['full_text'].apply(
        contem_termos, termos_busca=termos_procurados
    )].copy()
    
    df_filtrado = df_filtrado.reset_index(drop=True)
    textos_filtrados = df_filtrado['full_text'].tolist()
    
    return df_filtrado, textos_filtrados
