from typing import List, Dict

# Modelos de Dados
class Marca:
    codigo: str
    nome: str

    def __init__(self, data: Dict[str, str]):
        self.codigo = data["codigo"]
        self.nome = data["nome"]

class Modelo:
    codigo: str
    nome: str

    def __init__(self, data: Dict[str, str]):
        self.codigo = data["codigo"]
        self.nome = data["nome"]

class Ano:
    codigo: str
    nome: str

    def __init__(self, data: Dict[str, str]):
        self.codigo = data["codigo"]
        self.nome = data["nome"]
        
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