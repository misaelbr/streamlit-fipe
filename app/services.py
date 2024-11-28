import os
from dotenv import load_dotenv

from app.cache_proxy import fetch_with_cache

load_dotenv()

API_URL=os.getenv("API_URL")

# Funções para comunicar com APIs
def fetch_marcas(tipo_veiculo: str = "cars") -> list:
    url = f"{API_URL}/{tipo_veiculo}/brands"
    
    return fetch_with_cache(f"marcas_{tipo_veiculo}", url)

def fetch_modelos(codigo_marca: str, tipo_veiculo: str = "cars") -> dict:
    url = f"{API_URL}/{tipo_veiculo}/brands/{codigo_marca}/models"

    return fetch_with_cache(f"modelos_{tipo_veiculo}_{codigo_marca}", url)

def fetch_anos(codigo_marca: str, codigo_modelo: str, tipo_veiculo: str = "cars") -> list:
    url = f"{API_URL}/{tipo_veiculo}/brands/{codigo_marca}/models/{codigo_modelo}/years"
    
    return fetch_with_cache(f"anos_{tipo_veiculo}_{codigo_marca}_{codigo_modelo}", url)

def fetch_detalhes_ano(codigo_marca: str, codigo_modelo: str, codigo_ano: str, mes_referencia: str | None, tipo_veiculo:str = "cars") -> dict:
    query = ""
    if mes_referencia is not None:
        query = f"?reference={mes_referencia}"
    
    url=f"{API_URL}/{tipo_veiculo}/brands/{codigo_marca}/models/{codigo_modelo}/years/{codigo_ano}{query}"

    return fetch_with_cache(f"detalhes_{tipo_veiculo}_{codigo_marca}_{codigo_modelo}_{codigo_ano}_{mes_referencia}", url)

def fetch_tabelas() -> list:
    url = f"{API_URL}/references"

    return fetch_with_cache(f"tabelas", url)