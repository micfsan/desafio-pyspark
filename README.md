# 🚀 Data Engineering PySpark - Desafio de Vendas 2025

Este projeto é um pipeline de dados robusto desenvolvido em **PySpark**, utilizando as melhores práticas de **Engenharia de Software**, como Programação Orientada a Objetos (POO), Injeção de Dependências, Logging profissional e Testes Unitários.

O objetivo principal é gerar um relatório de pedidos de venda de **2025** cujos pagamentos foram **recusados**, mas que a avaliação de fraude classificou como **legítimos**.

---

## 🛠️ Estrutura do Projeto

```text
.
├── config/
│   └── settings.yaml          # Configurações de caminhos e Spark
├── data/
│   └── input/                 # Datasets de Pedidos e Pagamentos
├── dist/                      # Pacote distribuível (.whl)
├── src/
│   ├── config/                # Carregamento de configurações
│   ├── io_utils/              # Leitura (CSV/JSON) e Escrita (Parquet)
│   ├── pipeline/              # Orquestrador (Fluxo de execução)
│   ├── processing/            # Regras de Negócio e Transformações
│   ├── session/               # Gerenciamento da SparkSession
│   └── main.py                # Ponto de entrada (Aggregation Root)
├── tests/                     # Testes automatizados com Pytest
├── pyproject.toml             # Metadados de empacotamento
└── requirements.txt           # Dependências do projeto

````

# ⚙️ Pré-requisitos
Python: 3.8+

Java: 8 ou 11 (necessário para o PySpark)

Datasets: Clonados na pasta data/input/

# 🚀 Como Executar
1. Instalar Dependências

```
pip install -r requirements.txt
```

2. Rodar o Pipeline

Para executar o processamento e gerar o relatório final:
```
export PYTHONPATH=$PYTHONPATH:$(pwd)/src
    python3 src/main.py 
```

# 🧪 Testes Automatizados
Para garantir que a lógica de negócio está correta, execute:

```
export PYTHONPATH=$PYTHONPATH:$(pwd)
pytest tests/test_transformations.py
```

# 📦 Empacotamento
Para gerar o arquivo distribuível .whl:

Limpar builds antigos: ```rm -rf dist/ build/ *.egg-info```

Gerar o pacote: ```python3 -m build```

# 📋 Requisitos Atendidos
[x] Schemas Explícitos: StructTypes definidos manualmente.

[x] POO & Injeção de Dependência: Estrutura modular e testável.

[x] Logging & Erros: Monitoramento completo do pipeline.
