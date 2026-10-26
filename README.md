# Pipeline ETL com Python

Análise exploratória e validação de dados de campanhas publicitárias em CSV com **Pandas**, **Pydantic**, **YData Profiling** e **Streamlit**.

O projeto lê arquivos locais, valida registros e permite exportar um CSV validado. Também gera um relatório HTML com estatísticas, valores ausentes e correlações.

## Instalação

Ambiente utilizado: **Python 3.12**. Execute na raiz do projeto:

```bash
git clone https://github.com/arthurjuancontato/pipeline-etl-python.git
cd pipeline-etl-python
python -m venv .venv
```

Ative o ambiente no Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

No Linux ou macOS:

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

## Relatório exploratório

```bash
python main.py
```

O script lê `data.csv` e gera ou substitui `output.html` na raiz do projeto. Abra o HTML no navegador para consultar o relatório. A geração pode levar alguns minutos.

## Interface de validação

```bash
python -m streamlit run src/aplicacao.py
```

Abra o endereço exibido no terminal, envie um CSV e clique em **Validar Dados**. A interface apresenta os erros por linha ou, quando todos os registros são válidos, oferece o download de `dados_validados.csv`.

## Formato dos dados

Use arquivos UTF-8 separados por vírgula, com estas colunas:

| Coluna | Regra atual |
| --- | --- |
| `Organizador` | Inteiro obrigatório |
| `Ano_Mes` | Texto obrigatório |
| `Dia_da_Semana` | Texto obrigatório |
| `Tipo_Dia` | Texto obrigatório |
| `Objetivo` | Texto obrigatório |
| `Date` | Texto obrigatório; o formato de data ainda não é validado |
| `AdSet_name` | Texto opcional |
| `Amount_spent` | Número entre 0 e 1.200; padrão 0 quando a coluna está ausente |
| `Link_clicks` | Inteiro opcional |
| `Impressions` | Inteiro; padrão 0 quando a coluna está ausente |
| `Conversions` | Inteiro opcional |
| `Segmentação` | Texto opcional |
| `Tipo_de_Anúncio` | Texto obrigatório |
| `Fase` | Texto obrigatório |

A interface também aceita `Segmentacao` e `Tipo_de_Anuncio`, nomes internos do modelo. Células vazias são convertidas para `None` e podem gerar erros em campos não opcionais. `data_2025.csv` não contém a coluna opcional de segmentação.

## Estrutura

```text
pipeline-etl-python/
├── src/
│   ├── aplicacao.py       # Interface web e validação dos registros
│   └── validador.py       # Modelo Pydantic
├── .env.example          # Orientações de configuração sem segredos
├── .gitignore
├── data.csv
├── data_2025.csv
├── main.py               # Geração do relatório exploratório
├── output.html           # Relatório gerado
├── requirements.txt
└── README.md
```

## Configuração e publicação

A versão atual não exige credenciais, não lê variáveis de ambiente e não carrega `.env`. Nenhuma configuração é necessária para executar o projeto. O `.env.example` documenta essa situação.

O `.env` é reservado para configurações privadas futuras e fica fora do Git. Se adicionar integrações, implemente a leitura dessas variáveis e documente somente exemplos sem valores reais em `.env.example`. Nunca publique tokens ou senhas.

Os CSVs e o relatório HTML já são versionados. O relatório contém amostras dos dados de entrada: utilize apenas dados autorizados para divulgação pública e anonimize informações privadas antes de substituir esses arquivos.

## Escopo atual

O processamento usa arquivos locais e exportação pelo navegador. Ainda não há integração com banco de dados, agendamento ou orquestração. A geração do relatório e a interface de validação são executadas separadamente.
