from enum import Enum
from typing import Dict

# Modelos de Dados
class Marca:
    codigo: str
    nome: str

    def __init__(self, data: Dict[str, str]):
        self.codigo = data["code"]
        self.nome = data["name"]

class Modelo:
    codigo: str
    nome: str

    def __init__(self, data: Dict[str, str]):
        self.codigo = data["code"]
        self.nome = data["name"]

class Ano:
    codigo: str
    nome: str

    def __init__(self, data: Dict[str, str]):
        self.codigo = data["code"]
        self.nome = data["name"]
        
class DetalhesVeiculo:
    tipo_veiculo: int
    valor: str
    marca: str
    modelo: str
    ano_modelo: int
    combustivel: str
    codigo_fipe: str
    mes_referencia: str

    def __init__(self, data: Dict):
        self.tipo_veiculo = data["vehicleType"]
        self.valor = data["price"]
        self.marca = data["brand"]
        self.modelo =data["model"]
        self.ano_modelo = data["modelYear"]
        self.combustivel = data["fuel"]
        self.codigo_fipe = data["codeFipe"]
        self.mes_referencia = data["referenceMonth"]

class Tabela:
    codigo: int
    mes: str

    def __init__(self, data: Dict[str, str]):
        self.codigo = data["code"]
        self.mes = data["month"]
        
class TipoVeiculo:
    tipo: str
    descricao: str
    
    def __init__(self, data: Dict[str, str]):
        self.tipo = data["tipo"]
        self.descricao = data["descricao"]