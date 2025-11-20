# analise-narracao-futebol

# Análise de Sentimentos - Narração Feminina de Futebol

Projeto de análise de sentimentos em tweets sobre narração feminina de futebol, utilizando o modelo BERTabaporu através da biblioteca pysentimiento. Esse projeto é fruto do projeto extensionista para a disciplina CBD0318 - Método Digitais, ministrada pelo Prof. Dr. Alan César Belo Angeluci, no segundo semestre de 2025, na Escola de Comunicação e Artes da Universidade de São Paulo (ECA-USP). Agradecemos ao professor e aos monitores da disciplina.

## Sobre o Projeto

Este projeto analisa tweets coletados via [Zeeschuimer](https://github.com/digitalmethodsinitiative/zeeschuimer) para identificar:
- **Sentimentos** (positivo, negativo, neutro)
- **Sexismo** (probabilidade e classificação)
- **Padrões de engajamento** relacionados à narração feminina

### Modelos Utilizados

- **BERTabaporu**: Modelo RoBERTa treinado com tweets em português
- **pysentimiento**: Biblioteca para análise de sentimentos e detecção de discurso de ódio

## Instalação

### Requisitos
- Python 3.7+
- pip

### Passo a passo

```bash
# Clone o repositório
git clone https://github.com/xcolacique/analise-narracao-futebol.git
cd analise-narracao-futebol

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instale as dependências
pip install -r requirements.txt
```

## Uso

### Análise básica

```bash
python main.py <caminho/arquivo.ndjson>
```

### Saída

O script gera automaticamente:

**Arquivos CSV** (pasta `output/`):
- `tweets_filtrados.csv` - Tweets que contêm os termos buscados
- `analise_sentimentos.csv` - Resultados da análise de sentimentos
- `analise_sexismo.csv` - Resultados da análise de sexismo

**Gráficos** (pasta `output/`):
- `sentimentos_pizza.png` - Distribuição de sentimentos (pizza)
- `sentimentos_barras.png` - Distribuição de sentimentos (barras)
- `sexismo_classificacao.png` - Classificação de sexismo

## Termos Filtrados

O script filtra tweets que contenham (case-insensitive):
- "mulher narrando"
- "narradora"
- "renata silveira"

*Para modificar os termos, edite a variável `termos_procurados` no arquivo `main.py`*

## Estrutura do Projeto

```
.
├── main.py                      # Script principal
├── requirements.txt             # Dependências
├── README.md                    # Este arquivo
├── .gitignore                   # Arquivos ignorados pelo Git
├── src/                         # Código-fonte modularizado
│   ├── __init__.py             # Inicialização do pacote
│   ├── config.py               # Configurações do projeto
│   ├── data_loader.py          # Carregamento e filtro de dados
│   ├── analyzer.py             # Análise de sentimentos e sexismo
│   ├── visualizer.py           # Geração de gráficos
│   └── utils.py                # Funções utilitárias
├── data/                        # Seus arquivos NDJSON (não versionados)
│   └── .gitkeep
└── output/                      # Resultados (não versionados)
    ├── tweets_filtrados.csv
    ├── analise_sentimentos.csv
    ├── analise_sexismo.csv
    ├── relatorio_resumo.txt
    └── *.png
```

## Funcionalidades

### 1. Extração de Dados
- Leitura de arquivos NDJSON do Zeeschuimer
- Extração de texto, métricas de engajamento e metadados

### 2. Filtragem
- Busca por termos específicos (case-insensitive)
- Contagem e estatísticas de filtros aplicados

### 3. Análise de Sentimentos
- Classificação: Positivo (POS), Negativo (NEG), Neutro (NEU)
- Probabilidades para cada categoria
- Visualizações em pizza e barras

### 4. Análise de Sexismo
- Detecção via modelo de hate speech
- Limiar configurável (padrão: 20%)
- Classificação por faixas de probabilidade

### 5. Visualizações
- Gráficos salvos em alta resolução
- Cores consistentes e profissionais
- Exportação automática

## Referências

### BERT
- Devlin et al. (2018). [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)

### RoBERTa
- Liu et al. (2019). [RoBERTa: A Robustly Optimized BERT Pretraining Approach](https://arxiv.org/abs/1907.11692)

### BERTabaporu
- BERTabaporu: Assessing a Genre-Specific Language Model for Portuguese NLP [ACL Anthology](https://aclanthology.org/2023.ranlp-1.24/)

### pysentimiento
- Pérez et al. (2021). [pysentimiento: A Python Toolkit for Opinion Mining and Social NLP tasks](https://arxiv.org/abs/2106.09462)

### Zeeschuimer
- [GitHub - Digital Methods Initiative](https://github.com/digitalmethodsinitiative/zeeschuimer)

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## Autores

- Mônica Colacique - [@xcolacique](https://github.com/xcolacique)
- Lucas de Lima Coelho
