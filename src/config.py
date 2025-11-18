"""
Configurações do projeto
"""

# Termos para filtrar tweets
TERMOS_FILTRO = [
    "mulher narrando",
    "narradora",
    "renata silveira"
]

# Limiar para classificação de sexismo (0-1)
LIMIAR_SEXISMO = 0.20

# Diretório de saída dos resultados
OUTPUT_DIR = "output"

# Configurações de análise
ANALISE_CONFIG = {
    "sentiment": {
        "task": "sentiment",
        "lang": "pt"
    },
    "hate_speech": {
        "task": "hate_speech",
        "lang": "pt"
    },
    "emotion": {
        "task": "emotion",
        "lang": "pt"
    }
}

# Configurações de visualização
CORES = {
    "sentimento": {
        "POS": "#22c55e",  # Verde
        "NEG": "#ef4444",  # Vermelho
        "NEU": "#94a3b8"   # Cinza
    },
    "sexismo": {
        "sexista": "#ef4444",      # Vermelho
        "nao_sexista": "#22c55e"   # Verde
    }
}

# Configurações de gráficos
GRAFICO_CONFIG = {
    "dpi": 300,
    "figsize_pizza": (10, 8),
    "figsize_barras": (10, 6),
    "fontsize_titulo": 16,
    "fontsize_label": 12
}
