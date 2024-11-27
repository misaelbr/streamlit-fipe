# Streamlit FIPE

## Descrição

Este projeto permite a consulta de preços de veículos a partir da tabela FIPE.
![Ferramenta em execução](data/app.jpg)

## Funcionamento

O projeto foi desenvolvido em Python e utiliza a biblioteca Streamlit para a criação rápida de interface web. 
Os dados são obtidos a partir de requisições REST na API não oficial da FIPE disponível neste [link](https://deividfortuna.github.io/fipe/v2/).

## Requisitos

Este projeto foi desenvolvido utilizando Python 3.11.6 e as seguintes bibliotecas:

- requests
- streamlit
- pandas
- plotly
- python-dotenv
- diskcache

## Instalação

### 1. Crie um ambiente virtual

#### 1.1 Para isolar as dependências do projeto, crie um ambiente virtual:

```bash
$ python3 -m venv venv
```

#### 1.2 Ative o ambiente virtual

```bash
$ source venv/bin/activate
```

Se o nome do prompt mudar para (venv), o ambiente virtual foi ativado com sucesso.

#### 1.3 Configure o arquivo .env

Mova o arquivo .env-dist para .env e preencha as variáveis de ambiente com os valores corretos.

```bash
$ mv .env-dist .env
```

#### 1.4 Instale as dependências

```bash
$ pip install -r requirements.txt
```

#### Observação final

Sempre ative o ambiente virtual antes de executar o projeto.

Para desativar o ambiente virtual ativo, execute:

```bash
$ deactivate
```

## Executar o projeto

Após a instalação das dependências, execute o comando abaixo para iniciar a aplicação:

```bash
$ streamlit run main.py
```
