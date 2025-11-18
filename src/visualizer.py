"""
Módulo para geração de visualizações e gráficos
"""

import matplotlib.pyplot as plt
import os


# Cores padrão para os gráficos
CORES_SENTIMENTO = {
    'NEG': '#ef4444',
    'POS': '#22c55e',
    'NEU': '#94a3b8'
}

CORES_SEXISMO = {
    'sexista': '#ef4444',
    'nao_sexista': '#22c55e'
}


def plotar_sentimentos(df_sent, output_dir='output'):
    """
    Gera gráficos de distribuição de sentimentos

    Args:
        df_sent: DataFrame com análise de sentimentos
        output_dir: diretório para salvar os gráficos
    """
    print("\n[3/3] Gerando visualizações...")
    os.makedirs(output_dir, exist_ok=True)
    
    distribuicao = df_sent['Sentimento'].value_counts()
    percentuais = (distribuicao / distribuicao.sum()) * 100
    colors = [CORES_SENTIMENTO.get(sent, '#gray') for sent in distribuicao.index]
    
    # Gráfico de pizza
    _criar_grafico_pizza(distribuicao, percentuais, colors, output_dir)
    
    # Gráfico de barras
    _criar_grafico_barras(distribuicao, percentuais, colors, output_dir)
    
    print(f"  ✓ Gráficos de sentimentos salvos em '{output_dir}/'")


def _criar_grafico_pizza(distribuicao, percentuais, colors, output_dir):
    """Cria gráfico de pizza para sentimentos"""
    plt.figure(figsize=(10, 8))
    plt.pie(
        distribuicao.values,
        labels=distribuicao.index,
        autopct='%1.1f%%',
        colors=colors,
        startangle=90,
        textprops={'fontsize': 12, 'weight': 'bold'}
    )
    plt.title('Distribuição de Sentimentos', fontsize=16, weight='bold', pad=20)
    
    legend_labels = [
        f'{sent}: {count} ({percentuais[sent]:.2f}%)'
        for sent, count in distribuicao.items()
    ]
    plt.legend(legend_labels, loc='best', fontsize=10)
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/sentimentos_pizza.png', dpi=300, bbox_inches='tight')
    plt.close()


def _criar_grafico_barras(distribuicao, percentuais, colors, output_dir):
    """Cria gráfico de barras para sentimentos"""
    plt.figure(figsize=(10, 6))
    bars = plt.bar(
        distribuicao.index, 
        distribuicao.values, 
        color=colors, 
        edgecolor='black', 
        linewidth=1.2
    )
    
    # Adicionar valores em cima das barras
    for bar, valor, perc in zip(bars, distribuicao.values, percentuais):
        plt.text(
            bar.get_x() + bar.get_width()/2, 
            bar.get_height() + 1,
            f'{valor}\n({perc:.1f}%)',
            ha='center', 
            va='bottom', 
            fontsize=11, 
            weight='bold'
        )
    
    plt.xlabel('Sentimento', fontsize=12, weight='bold')
    plt.ylabel('Quantidade', fontsize=12, weight='bold')
    plt.title('Distribuição de Sentimentos', fontsize=16, weight='bold', pad=20)
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/sentimentos_barras.png', dpi=300, bbox_inches='tight')
    plt.close()


def plotar_sexismo(df_hate, output_dir='output'):
    """
    Gera gráfico de classificação de sexismo

    Args:
        df_hate: DataFrame com análise de sexismo
        output_dir: diretório para salvar o gráfico
    """
    os.makedirs(output_dir, exist_ok=True)
    
    plt.figure(figsize=(10, 8))
    sexista_count = df_hate['É_Sexista'].value_counts()
    
    # Mapear True/False para labels descritivos
    labels = ['Não Sexista (<20%)', 'Sexista (≥20%)']
    # Garantir ordem correta (False primeiro, depois True)
    values = [sexista_count.get(False, 0), sexista_count.get(True, 0)]
    colors = [CORES_SEXISMO['nao_sexista'], CORES_SEXISMO['sexista']]
    explode = (0, 0.1)  # Destaca a fatia de sexistas
    
    plt.pie(
        values, 
        labels=labels, 
        autopct='%1.1f%%',
        colors=colors, 
        startangle=90, 
        explode=explode,
        textprops={'fontsize': 12, 'weight': 'bold'}
    )
    plt.title(
        'Classificação de Sexismo (Limiar 20%)', 
        fontsize=16, 
        weight='bold', 
        pad=20
    )
    plt.tight_layout()
    plt.savefig(f'{output_dir}/sexismo_classificacao.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"  ✓ Gráfico de sexismo salvo em '{output_dir}/'")


def plotar_distribuicao_faixas(df_hate, output_dir='output'):
    """
    Gera gráfico de distribuição por faixas de probabilidade de sexismo
    
    Args:
        df_hate: DataFrame com análise de sexismo
        output_dir: diretório para salvar o gráfico
    """
    os.makedirs(output_dir, exist_ok=True)
    
    distribuicao = df_hate['Faixa_Sexismo'].value_counts().sort_index()
    
    plt.figure(figsize=(12, 6))
    bars = plt.bar(
        range(len(distribuicao)), 
        distribuicao.values,
        color='#6366f1',
        edgecolor='black',
        linewidth=1.2
    )
    
    plt.xticks(range(len(distribuicao)), distribuicao.index, rotation=45, ha='right')
    plt.xlabel('Faixa de Probabilidade', fontsize=12, weight='bold')
    plt.ylabel('Quantidade de Tweets', fontsize=12, weight='bold')
    plt.title('Distribuição por Faixas de Probabilidade de Sexismo', 
              fontsize=14, weight='bold', pad=20)
    
    # Adicionar valores em cima das barras
    for bar, valor in zip(bars, distribuicao.values):
        plt.text(
            bar.get_x() + bar.get_width()/2,
            bar.get_height() + 0.5,
            str(valor),
            ha='center',
            va='bottom',
            fontsize=10,
            weight='bold'
        )
    
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/sexismo_faixas.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"  ✓ Gráfico de faixas de sexismo salvo em '{output_dir}/'")
