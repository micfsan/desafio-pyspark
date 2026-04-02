# 🚀 PySpark Data Pipeline - Desafio Vendas 2025
Este projeto consiste em um pipeline de dados desenvolvido em PySpark para processamento de grandes volumes de transações. O objetivo é identificar pedidos de 2025 que foram recusados pelo gateway de pagamento, mas classificados como legítimos pelo sistema de antifraude.

🏗️ Arquitetura e Padrões (S.O.L.I.D.)
O projeto foi construído seguindo rigorosos padrões de engenharia de software:

POO (Orientação a Objetos): Toda a lógica encapsulada em classes modulares.

Injeção de Dependências: O main.py atua como Aggregation Root, instanciando e injetando dependências.

Schemas Explícitos: Definição manual de StructType para todos os DataFrames (Zero inferência).

Agnóstico: Configurações centralizadas em YAML, permitindo execução em qualquer ambiente.
---

# 📋 Pré-requisitos
Antes de iniciar, certifique-se de que seu ambiente possui:

Python: Versão 3.8 ou superior.

Java (JDK): Versão 11 ou 17 (Obrigatório para o funcionamento do Apache Spark).

Apache Spark: Versão 3.3.0 ou superior instalada e configurada no PATH.

Datasets: Arquivos de entrada localizados em ./data/input/ (Pedidos em CSV.gz e Pagamentos em JSON.gz).


## 📂 Estrutura de Pastas

```text
.
├── config/             # Configurações centralizadas (settings.yaml)
├── data/               # Camadas de dados (Input/Output)
├── src/                # Código-fonte organizado em pacotes
│   ├── config/         # Classe de carregamento de YAML
│   ├── io_utils/       # I/O com Schemas e Escrita em Parquet
│   ├── processing/     # Lógica de Negócio (Transformações)
│   ├── session/        # Gerenciamento da SparkSession
│   └── main.py         # Ponto de entrada da aplicação
├── tests/              # Testes unitários com Pytest
└── pyproject.toml      # Configuração de empacotamento (.whl)

````

# 🚀 Como Executar
1. Instalar Dependências
```
pip install -r requirements.txt
```

2. Gerar o Pacote (Build)
Transforme o código em um pacote distribuível profissional:
```
python3 -m build
```

3. Executar o Pipeline (Spark-Submit)
Rode o processamento utilizando o pacote gerado:
```
spark-submit --master "local[*]" \--py-files dist/*.whl \src/main.py
```

# 🧪 Qualidade e Testes
Para validar as regras de negócio e a integridade dos dados:
```
export PYTHONPATH=$PYTHONPATH:$(pwd)/src
pytest tests/test_transformations.py
```

📊 Entrega Técnica
Formato de Saída: Parquet (Colunar).

Ordenação: UF, Forma de Pagamento e Data do Pedido.

Logging: Monitoramento completo via logging.INFO.

Tratamento de Erros: Blocos try/except em todas as camadas críticas.
