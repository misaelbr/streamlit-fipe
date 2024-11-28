import os
import logging
from datetime import datetime
from diskcache import Cache
import requests
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configurar cache
CACHE_PATH = os.getenv("CACHE_DIR", "data/cache")
CACHE_EXPIRATION = os.getenv("CACHE_EXPIRATION", 3600)
cache = Cache(CACHE_PATH)

# Configurar cabeçalhos para as requisições
headers = {
    "X-Subscription-Token": os.getenv("API_KEY")
}

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),    # Arquivo de log
        logging.StreamHandler()                 # Console
    ]
)
logger = logging.getLogger(__name__)

def isNewMonth() -> bool:
    try:
        last_update = cache.get("last_cache_update")
        now = datetime.now()
        current_month = now.strftime("%Y-%m")
        
        if now.day == 1 and now.hour >= 6:
            if last_update != current_month:
                logger.info(f"Novo mês detectado após 06h: {current_month}. Revalidando cache.")
                cache.set("last_cache_update", current_month)
                return True
    except Exception as e:
        logger.error(f"Erro ao verificar se é um novo mês: {e}", exc_info=True)
    return False

def cache_revalidate():
    try:
        if isNewMonth():
            logger.info("Limpando o cache para revalidação mensal.")
            cache.clear()
    except Exception as e:
        logger.error(f"Erro ao revalidar o cache: {e}", exc_info=True)

def fetch_with_cache(key: str, url: str, ttl: int = int(CACHE_EXPIRATION) * 24 * 7) -> dict:
    try:
        cache_revalidate()
        
        if key in cache:
            logger.info(f"Cache hit: {key}")
            return cache[key]
        
        logger.info(f"Cache miss: {key}. Fetch API: {url}")
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        cache.set(key, response.json(), expire=ttl)
        return response.json()
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Erro na requisição para {url}: {req_err}", exc_info=True)
        raise
    except Exception as e:
        logger.error(f"Erro ao buscar dados para a chave {key}: {e}", exc_info=True)
        raise
