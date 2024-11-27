import streamlit as st
from app.repository import get_marcas, get_modelos, get_anos, get_detalhes_ano, get_tabelas

# Título da Aplicação
st.title("Consulta FIPE de Veículos")

# Etapa 1: Seleção da Tabela de Referência
st.header("Tabela de Referência")
tabelas = get_tabelas()
tabela_nomes = [tabela.mes for tabela in tabelas] 
tabela_selecionada = st.selectbox("Selecione o mês de referência:", options=tabela_nomes)
tabela = next(tabela for tabela in tabelas if tabela.mes == tabela_selecionada)

# Etapa 2: Seleção de Marca
st.header("Seleção de Marca")
marcas = get_marcas()
marca_nomes = [marca.nome for marca in marcas]
marca_selecionada = st.selectbox("Selecione uma marca:", options=marca_nomes)
marca = next(marca for marca in marcas if marca.nome == marca_selecionada)

# Etapa 3: Seleção de Modelo
st.header("Seleção de Modelo")
modelos = get_modelos(marca.codigo)
modelo_nomes = [modelo.nome for modelo in modelos]
modelo_selecionado = st.selectbox("Selecione um modelo:", options=modelo_nomes)
modelo = next(modelo for modelo in modelos if modelo.nome == modelo_selecionado)

# Etapa 4: Seleção de Ano
st.header("Seleção de Ano")
anos = get_anos(marca.codigo, modelo.codigo)
ano_nomes = [ano.nome for ano in anos]
ano_selecionado = st.selectbox("Selecione o ano:", options=ano_nomes)
ano = next(ano for ano in anos if ano.nome == ano_selecionado)

# Etapa 5: Consulta e Exibição de Detalhes
st.header("Detalhes do Veículo")
detalhes = get_detalhes_ano(marca.codigo, modelo.codigo, ano.codigo, tabela.codigo)


# Exibir detalhes do veículo
st.subheader("Informações do Veículo")
st.write(f"**Valor:** {detalhes.valor}")
st.write(f"**Marca:** {detalhes.marca}")
st.write(f"**Modelo:** {detalhes.modelo}")
st.write(f"**Ano:** {detalhes.ano_modelo}")
st.write(f"**Combustível:** {detalhes.combustivel}")
st.write(f"**Código FIPE:** {detalhes.codigo_fipe}")
st.write(f"**Mês de Referência:** {detalhes.mes_referencia}")
