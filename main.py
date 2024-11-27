import streamlit as st
from app.repository import get_marcas, get_modelos, get_anos, get_detalhes_ano, get_tabelas, get_variacao_preco
import plotly.express as px

st.set_page_config(layout="wide")


# Título da Aplicação
st.title("Consulta de Preços da Tabela FIPE")

st.sidebar.header("Filtros")

# Etapa 1: Seleção da Tabela de Referência
tabelas = get_tabelas()
tabela_nomes = [tabela.mes for tabela in tabelas] 
tabela_selecionada = st.sidebar.selectbox("Selecione o mês de referência:", options=tabela_nomes)
tabela = next(tabela for tabela in tabelas if tabela.mes == tabela_selecionada)

# Etapa 2: Seleção de Marca
marcas = get_marcas()
marca_nomes = [marca.nome for marca in marcas]
marca_selecionada = st.sidebar.selectbox("Selecione uma marca:", options=marca_nomes)
marca = next(marca for marca in marcas if marca.nome == marca_selecionada)

# Etapa 3: Seleção de Modelo
modelos = get_modelos(marca.codigo)
modelo_nomes = [modelo.nome for modelo in modelos]
modelo_selecionado = st.sidebar.selectbox("Selecione um modelo:", options=modelo_nomes)
modelo = next(modelo for modelo in modelos if modelo.nome == modelo_selecionado)

# Etapa 4: Seleção de Ano
anos = get_anos(marca.codigo, modelo.codigo)
ano_nomes = [ano.nome for ano in anos]
ano_selecionado = st.sidebar.selectbox("Selecione o ano:", options=ano_nomes)
ano = next(ano for ano in anos if ano.nome == ano_selecionado)

# Etapa 5: Consulta e Exibição de Detalhes
detalhes = get_detalhes_ano(marca.codigo, modelo.codigo, ano.codigo, tabela.codigo)


# Layout da Aplicação
c1, c2 = st.columns([0.3, 0.5])

# Exibir detalhes do veículo
c1.subheader("Informações do Veículo")
c1.write(f"**Valor:** {detalhes.valor}")
c1.write(f"**Marca:** {detalhes.marca}")
c1.write(f"**Modelo:** {detalhes.modelo}")
c1.write(f"**Ano:** {detalhes.ano_modelo}")
c1.write(f"**Combustível:** {detalhes.combustivel}")
c1.write(f"**Código FIPE:** {detalhes.codigo_fipe}")
c1.write(f"**Mês de Referência:** {detalhes.mes_referencia}")


# Exibir gráfico de variação de preço
c2.subheader("Variação de Preço")
df_precos = get_variacao_preco(marca.codigo, modelo.codigo, ano.codigo, tabelas[:5])

if not df_precos.empty:
    fig = px.line(df_precos, x="mes_referencia", y="preco", title="Variação de Preço")
    c2.plotly_chart(fig, use_container_width=True)