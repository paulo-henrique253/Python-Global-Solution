import sys
import os

sys.path.append(
    os.path.abspath("./app")
)
from models.empresa import Empresa

#from models.satelite import Satelite
import models.satelite as sat
empresas = list()

#Adiciona uma empresa na lista de empresas
def adicionar_empresa(nome: str, pais: str) -> None:
    empresa = Empresa(nome, pais)
    empresas.append(empresa)

#adiciona um satélite na lista de satélites
def adicionar_satelite(nome: str, nome_empresa: str, orbita: sat.TipoOrbita, status: sat.StatusOperacao) -> None:
    #cria o satélite
    satelite = sat.Satelite(nome, nome_empresa, orbita, status)

    #percorre todas as emrpesas
    for empresa in empresas:
        #adiciona na lista da empresa designida
        if empresa.nome.lower() == satelite.empresa.lower():
            satelite.empresa = empresa.nome
            empresa.satelites.append(satelite)
            return
    #caso não encontre, da erro
    print("ERRO!!! EMPRESA NÃO ENCONTRADA!!!")
    

#criação de empresas para base de dados
adicionar_empresa("SpaceX", "EUA")

adicionar_empresa("AstroScale", "JP")

adicionar_empresa("NASA", "EUA")
empresas[1].score = 30
empresas[2].score = 67
empresas[0].score = 40


#criação de satelites para base de dados
adicionar_satelite("ORBITS-12352", "NASA", sat.TipoOrbita.MEDIA, sat.StatusOperacao.ATIVO)

adicionar_satelite("STARLINK-4421", "SpaceX", sat.TipoOrbita.MEDIA, sat.StatusOperacao.ATIVO)
adicionar_satelite("STARLINK-6740", "SpaceX", sat.TipoOrbita.BAIXA, sat.StatusOperacao.INATIVO)
adicionar_satelite("STARLINK-2367", "SpaceX", sat.TipoOrbita.BAIXA, sat.StatusOperacao.ATIVO)