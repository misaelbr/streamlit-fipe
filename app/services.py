import requests
import os
import logging
from diskcache import Cache
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),  # Arquivo de log
        logging.StreamHandler()          # Console
    ]
)

logger = logging.getLogger(__name__)

# configura cache
CACHE_PATH = os.getenv("CACHE_DIR", "data/cache")
CACHE_EXPIRATION = os.getenv("CACHE_EXPIRATION", 3600)
cache = Cache(CACHE_PATH)

load_dotenv()

headers = {
    "X-Subscription-Token": os.getenv("API_KEY")
}


def fetch_with_cache(key: str, url: str, ttl: int = int(CACHE_EXPIRATION) * 24 * 7) -> dict:
    if key in cache:
        logger.info(f"Cache hit: {key}")
        return cache[key]
    
    logger.info(f"Cache miss: {key}. Consultando a api: {url}")
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    cache.set(key, response.json(), expire=ttl)
    return response.json()


# Funções para comunicar com APIs
def fetch_marcas() -> list:
    url = "https://parallelum.com.br/fipe/api/v1/carros/marcas"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    return fetch_with_cache("marcas", url)

def fetch_modelos(codigo_marca: str) -> dict:
    url = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{codigo_marca}/modelos"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    return fetch_with_cache(f"modelos_{codigo_marca}", url)

def fetch_anos(codigo_marca: str, codigo_modelo: str) -> list:
    url = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{codigo_marca}/modelos/{codigo_modelo}/anos"
    response = requests.get(url,headers=headers)
    response.raise_for_status()
    
    return fetch_with_cache(f"anos_{codigo_marca}_{codigo_modelo}", url)

def fetch_detalhes_ano(codigo_marca: str, codigo_modelo: str, codigo_ano: str, mes_referencia: str | None) -> dict:
    query = ""
    if mes_referencia is not None:
        query = f"?reference={mes_referencia}"
        
    
    url=f"https://fipe.parallelum.com.br/api/v2/cars/brands/{codigo_marca}/models/{codigo_modelo}/years/{codigo_ano}{query}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    return fetch_with_cache(f"detalhes_{codigo_marca}_{codigo_modelo}_{codigo_ano}_{mes_referencia}", url)

def fetch_tabelas() -> list:
    url = "https://fipe.parallelum.com.br/api/v2/references"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    return fetch_with_cache("tabelas", url)
