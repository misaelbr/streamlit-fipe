import requests
import os
from dotenv import load_dotenv

load_dotenv()

headers = {
    "X-Subscription-Token": os.getenv("API_KEY")
}


# Funções para comunicar com APIs
def fetch_marcas() -> list:
    url = "https://parallelum.com.br/fipe/api/v1/carros/marcas"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def fetch_modelos(codigo_marca: str) -> dict:
    url = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{codigo_marca}/modelos"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def fetch_anos(codigo_marca: str, codigo_modelo: str) -> list:
    url = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{codigo_marca}/modelos/{codigo_modelo}/anos"
    response = requests.get(url,headers=headers)
    response.raise_for_status()
    return response.json()

def fetch_detalhes_ano(codigo_marca: str, codigo_modelo: str, codigo_ano: str, mes_referencia: str | None) -> dict:
    query = ""
    if mes_referencia is not None:
        query = f"?reference={mes_referencia}"
        
    
    url=f"https://fipe.parallelum.com.br/api/v2/cars/brands/{codigo_marca}/models/{codigo_modelo}/years/{codigo_ano}{query}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    return response.json()

def fetch_tabelas() -> list:
    url = "https://fipe.parallelum.com.br/api/v2/references"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
