import sys
import os

sys.path.append(
    os.path.abspath("./app")
)
from models.empresa import Empresa

#from models.satelite import Satelite
import models.satelite as sat
empresas = list()

def adicionar_empresa(nome: str, pais: str) -> None:
    empresa = Empresa(nome, pais)
    empresas.append(empresa)

def adicionar_satelite(nome: str, nome_empresa: str, orbita: sat.TipoOrbita, status: sat.StatusOperacao) -> None:
    satelite = sat.Satelite(nome, nome_empresa, orbita, status)
    for empresa in empresas:
        if empresa.nome == satelite.empresa:
            empresa.satelites.append(satelite)
            return
    print("ERRO!!! EMPRESA NÃO ENCONTRADA!!!")
    


adicionar_empresa("SpaceX", "States")

adicionar_empresa("Goon space", "Br")

adicionar_empresa("Zeni", "Brasil")
empresas[1].score = 30
empresas[2].score = 67
empresas[0].score = 40

adicionar_satelite("Zeni-télite 1", "Zeni", "Ali", "Voando")
adicionar_satelite("Zeni-télite 2", "Zeni", "lá", "orbitando")