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
    


adicionar_empresa("SpaceX", "EUA")

adicionar_empresa("AstroScale", "JP")

adicionar_empresa("NASA", "EUA")
empresas[1].score = 30
empresas[2].score = 67
empresas[0].score = 40

adicionar_satelite("ORBITS-12352", "NASA", "MEO", "Ativo")
adicionar_satelite("Stratlink-2367", "SpaceX", "LEO", "Ativo")