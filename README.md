# Desculpas de Programador

Uma (tentativa de) tradução do conteúdo publicado em [programmingexcuses.com](http://programmingexcuses.com/).

Publicado em [desculpasdeprogramador.com.br](https://www.desculpasdeprogramador.com.br/).

## Setup

Antes de mais nada, crie o ambiente virtual e instale as dependências!

Depois, configure o arquivo `.env` (use o arquivo `.env.template` como modelo).

Nele devem ser especificados:

* O nome do arquivo CSV onde ficarão guardadas as desculpas baixadas do site original;
* A chave para usar a API da OpenAI (usada para traduzir as desculpas); e
* Os dados de conexão com o banco PostgreSQL.

Para subir um banco PostgreSQL rapidamente para testes, use o Docker:

```shell
docker run --name desculpas_db \
  -e POSTGRES_DB=desculpas_db \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=senha123 \
  -p 5432:5432 \
  -d postgres:16
```

Obviamente, para este caso, coloque os seguintes valores no arquivo `.env`:

```dotenv
DB_NAME="desculpas_db"
DB_USER="admin"
DB_PASSWORD="senha123"
DB_HOST="localhost"
DB_PORT="5432"
```

## Programas

### `scraping.py`

O programa `scraping.py` é usado para:

* Pegar as desculpas do site original;
* Traduzi-las (usando a API da OpenAI); e
* Armazená-las em um arquivo CSV.

### `db_create.py`

Usado para criar a tabela `desculpas` no banco PostgreSQL e, depois, carregá-la com o conteúdo do arquivo CSV.

### `app.py`

Este é o programa principal, que "sobe" um servidor Web para que você possa acessar a página que mostra as desculpas (normalmente, no endereço padrão do Flask: [127.0.0.1:5000](http://127.0.0.1:5000/)).
