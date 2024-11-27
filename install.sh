#!/bin/bash

# Definir cores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # Sem cor

# Nome do arquivo .env a ser criado
ENV_FILE=".env"
ENV_DIST_FILE=".env-dist"

echo -e "${CYAN}Iniciando configuração do ambiente...${NC}"

# Verifica se o arquivo .env já existe
if [[ -f $ENV_FILE ]]; then
    echo -e "${YELLOW}$ENV_FILE já existe. Não será sobrescrito.${NC}"
else
    # Copia o .env-dist para criar o .env
    if [[ -f $ENV_DIST_FILE ]]; then
        cp $ENV_DIST_FILE $ENV_FILE
        echo -e "${GREEN}$ENV_FILE foi criado a partir de $ENV_DIST_FILE.${NC}"
    else
        echo -e "${RED}Erro: O arquivo $ENV_DIST_FILE não foi encontrado.${NC}"
        exit 1
    fi
fi

# Criação do ambiente virtual
VENV_DIR=".venv"

if [[ -d $VENV_DIR ]]; then
    echo -e "${YELLOW}O ambiente virtual $VENV_DIR já existe.${NC}"
else
    python3 -m venv $VENV_DIR
    if [[ $? -eq 0 ]]; then
        echo -e "${GREEN}Ambiente virtual $VENV_DIR criado com sucesso.${NC}"
    else
        echo -e "${RED}Erro ao criar o ambiente virtual $VENV_DIR.${NC}"
        exit 1
    fi
fi

# Ativar o ambiente virtual
echo -e "${CYAN}Ativando o ambiente virtual...${NC}"
source $VENV_DIR/bin/activate

# Instalar as dependências
if [[ -f "requirements.txt" ]]; then
    echo -e "${CYAN}Instalando dependências a partir de requirements.txt...${NC}"
    pip install --upgrade pip
    pip install -r requirements.txt
    if [[ $? -eq 0 ]]; then
        echo -e "${GREEN}As dependências foram instaladas com sucesso.${NC}"
    else
        echo -e "${RED}Erro ao instalar as dependências.${NC}"
        deactivate
        exit 1
    fi
else
    echo -e "${RED}Erro: O arquivo requirements.txt não foi encontrado.${NC}"
    deactivate
    exit 1
fi

# Finaliza o script
echo -e "${BLUE}Configuração concluída.${NC} ${GREEN}Ambiente virtual configurado e dependências instaladas.${NC}"
