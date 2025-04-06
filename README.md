# Desculpas de Programador

Uma (tentativa de) tradução do conteúdo publicado em [programmingexcuses.com](http://programmingexcuses.com/).

Publicado em [desculpasdeprogramador.com.br](https://www.desculpasdeprogramador.com.br/)

## Programas

### `scraping.py`

O programa `scraping.py` é usado para:

* Pegar as desculpas do site original;
* Traduzi-las (usando a API da OpenAI);
* Armazená-las em um arquivo CSV.

O nome do arquivo CSV e a chave para usar a API da OpenAI devem ser especificados em um arquivo `.env` (use o arquivo `.env.template` como modelo).

### `app.py`

Este é o programa principal, que "sobe" um servidor Web para que você possa acessar a página que mostra as desculpas (normalmente, no endereço padrão do Flask: [127.0.0.1:5000](http://127.0.0.1:5000/)).
