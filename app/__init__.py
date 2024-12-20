# Reexportando os módulos principais
from .services import fetch_marcas, fetch_modelos, fetch_anos, fetch_detalhes_ano, fetch_tabelas
from .repository import get_marcas, get_modelos, get_anos, get_detalhes_ano, get_tabelas, get_variacao_preco, get_tipos_veiculos
from .models import Marca, Modelo, Ano, DetalhesVeiculo, Tabela, TipoVeiculo
from .cache_proxy import fetch_with_cache