from app.services import fetch_marcas, fetch_modelos, fetch_anos, fetch_detalhes_ano, fetch_tabelas
from app.models import Marca, Modelo, Ano, DetalhesVeiculo, Tabela, TipoVeiculo
import pandas as pd

def get_marcas(tipo_veiculo: str = 'cars') -> list[Marca]:
    data = fetch_marcas(tipo_veiculo)
    return [Marca(item) for item in data]

def get_modelos(codigo_marca: str, tipo_veiculo: str = 'cars') -> list[Modelo]:
    data = fetch_modelos(codigo_marca, tipo_veiculo=tipo_veiculo)
    return [Modelo(item) for item in data]

def get_anos(codigo_marca: str, codigo_modelo: str, tipo_veiculo: str = 'cars') -> list[Ano]:
    data = fetch_anos(codigo_marca, codigo_modelo, tipo_veiculo)
    return [Ano(item) for item in data]

def get_detalhes_ano(codigo_marca: str, codigo_modelo: str, codigo_ano: str, mes_referencia: str | None = None, tipo_veiculo: str = 'cars') -> DetalhesVeiculo:
    data = fetch_detalhes_ano(codigo_marca, codigo_modelo, codigo_ano, mes_referencia, tipo_veiculo)
    return DetalhesVeiculo(data)

def get_tabelas() -> list[Tabela]:
    data = fetch_tabelas()
    tabelas = [Tabela(item) for item in data]
    
    return tabelas

def get_variacao_preco(codigo_marca: str, codigo_modelo: str, codigo_ano: str, tabela_referencia: list[Tabela], tipo_veiculo: str='cars') ->pd.DataFrame:
    
    precos = []

    for tabela in tabela_referencia:
        detalhes = get_detalhes_ano(codigo_marca, codigo_modelo, codigo_ano, tabela.codigo, tipo_veiculo)        
        preco = detalhes.valor
        if preco is not None:
            precos.append({"mes_referencia": tabela.mes, "preco": preco})
            
    precos.reverse()
    
    df = pd.DataFrame(precos)
    df["preco"] = df["preco"].str.replace("R$", "").str.replace(".", "").str.replace(",", ".").astype(float)
    
    return df
    
def get_tipos_veiculos() -> list[TipoVeiculo]:
    tipos = {}  
    tipos["cars"] = "Carros"
    tipos["motorcycles"] = "Motos"
    tipos["trucks"] = "Caminhões"    
    
    return [TipoVeiculo({"tipo": tipo, "descricao": descricao}) for tipo, descricao in tipos.items()]
