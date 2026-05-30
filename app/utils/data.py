import sys
import os

sys.path.append(
    os.path.abspath("./app")
)
from models.empresa import Empresa
from models.satelite import Satelite
empresas = list()

def adicionar_empresa(nome: str, pais: str, num_sateliets: int,  documentacao) -> None:
    empresa = Empresa(nome, pais, num_sateliets, documentacao)
    empresas.append(empresa)

def adicionar_satelite(nome: str, nome_empresa: str, orbita: str, status: str) -> None:
    satelite = Satelite(nome, nome_empresa, orbita, status)
    for empresa in empresas:
        if empresa.nome == satelite.empresa:
            empresa.satelites.append(satelite)


adicionar_empresa("SpaceX", "States", 67, "")

adicionar_empresa("Goon space", "Br", 69, "")

adicionar_empresa("Zeni", "Brasil", 2, "")
empresas[1].pontos = 30
empresas[2].pontos = 67
empresas[0].pontos = 40

adicionar_satelite("Zeni-télite 1", "Zeni", "Ali", "Voando")
adicionar_satelite("Zeni-télite 2", "Zeni", "lá", "orbitando")