#!/bin/bash

# Nome do arquivo .env a ser criado
ENV_FILE=".env"
ENV_DIST_FILE=".env-dist"

# Verifica se o arquivo .env já existe
if [[ -f $ENV_FILE ]]; then
    echo "$ENV_FILE já existe. Não será sobrescrito."
else
    # Copia o .env-dist para criar o .env
    if [[ -f $ENV_DIST_FILE ]]; then
        cp $ENV_DIST_FILE $ENV_FILE
        echo "$ENV_FILE foi criado a partir de $ENV_DIST_FILE."
    else
        echo "Erro: O arquivo $ENV_DIST_FILE não foi encontrado."
        exit 1
    fi
fi

# Criação do ambiente virtual
VENV_DIR=".venv"

if [[ -d $VENV_DIR ]]; then
    echo "O ambiente virtual $VENV_DIR já existe."
else
    python3 -m venv $VENV_DIR
    echo "Ambiente virtual $VENV_DIR criado."
fi

# Ativar o ambiente virtual
source $VENV_DIR/bin/activate

# Instalar as dependências
if [[ -f "requirements.txt" ]]; then
    pip install --upgrade pip
    pip install -r requirements.txt
    echo "As dependências foram instaladas."
else
    echo "Erro: O arquivo requirements.txt não foi encontrado."
    deactivate
    exit 1
fi

# Finaliza o script
echo "Configuração concluída. Ambiente virtual configurado e dependências instaladas."
