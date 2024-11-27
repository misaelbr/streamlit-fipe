from app.services import fetch_marcas, fetch_modelos, fetch_anos, fetch_detalhes_ano, fetch_tabelas
from app.models import Marca, Modelo, Ano, DetalhesVeiculo, Tabela

def get_marcas() -> list[Marca]:
    data = fetch_marcas()
    return [Marca(item) for item in data]

def get_modelos(codigo_marca: str) -> list[Modelo]:
    data = fetch_modelos(codigo_marca)
    return [Modelo(item) for item in data["modelos"]]

def get_anos(codigo_marca: str, codigo_modelo: str) -> list[Ano]:
    data = fetch_anos(codigo_marca, codigo_modelo)
    return [Ano(item) for item in data]

def get_detalhes_ano(codigo_marca: str, codigo_modelo: str, codigo_ano: str, mes_referencia: str | None = None) -> DetalhesVeiculo:
    data = fetch_detalhes_ano(codigo_marca, codigo_modelo, codigo_ano, mes_referencia)
    return DetalhesVeiculo(data)

def get_tabelas() -> list[Tabela]:
    data = fetch_tabelas()
    return [Tabela(item) for item in data]