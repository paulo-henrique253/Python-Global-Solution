import sys
import os

sys.path.append(
    os.path.abspath("./app")
)
import utils.data as data
from models.empresa import Empresa
from models.satelite import Satelite

# Pegar uma empresa cadastrada pelo nome
def obter_empresa(nome_empresa: str) -> Empresa:
    # Percorrer a lista
    for empresa in data.empresas:
        if empresa.nome == nome_empresa:
            return empresa #caso ache uma empresa com esse nome, retorna ela
    return None # Se não encontrar, retorna nulo


def consultar_empresa() -> None:
    nome_empresa = input("Nome: ")

    empresa = obter_empresa(nome_empresa)
    if empresa == None:
        print("Empresa não existe")
        return
    print(f"{empresa.nome} - {empresa.pontos}")
    resp = input("Gostaria de ver os satélites registrados(s/n): ").lower()
    if resp == 's' or resp == "sim":
        if len(empresa.satelites) == 0:
            print("Essa empresa não tem satélites cadastrados!")
            return
        for satelite in empresa.satelites:
            print(f"{satelite.nome} - Status: {satelite.status}")
        

# Cadastrar uma empresa
def cadastrar_empresa() -> None:
    nome_empresa = input("Nome: ")
    # Forçar o input de uma empresa válida
    while nome_empresa == "" or obter_empresa(nome_empresa) != None:
        if nome_empresa == "":
            print("ERRO!!! Insira um nome")
        else:
            print("ERRO!!! empresa ja cadastrada")
        nome_empresa = input("Nome: ")

    pais_empresa = input("Pais: ")

    while pais_empresa == "":
        print("ERRO!!! Insira uma empresa")
        pais_empresa = input("Pais: ")
    
    num_satelites = input("numero de Satelites: ")
    sat_valido = True if num_satelites.isnumeric() and int(num_satelites) >= 0 else False
    while not sat_valido:
        num_satelites = input("numero de Satelites: ")
        sat_valido = True if num_satelites.isnumeric() and int(num_satelites) >= 0 else False
    
    doc_empresa = input("Documentaçao: ")
    # verificar_doc(doc_empresa)
    data.adicionar_empresa(nome_empresa, pais_empresa, int(num_satelites), doc_empresa)


def cadastrar_satelite() -> None:
    nome_satelite = input("Nome: ")
    while nome_satelite == "":
        print("ERRO!!! Insira um nome")
        nome_satelite = input("Nome: ")
    
    nome_empresa = input("Empresa: ")

    while obter_empresa(nome_empresa) == None:
        print("ERRO!!! Insira uma empresa cadastrada")
        nome_empresa = input("Empresa: ")
    
    orbita = input("Orbita: ")
    #if not eh_orbita

    status = input("status: ")

    data.adicionar_satelite(nome_satelite, nome_empresa, orbita, status)

def ranking_score() -> None:
    m1 = {
        "nome": "",
        "pts": -1 
    }
    m2 = {
        "nome": "",
        "pts": -1 
    }
    m3 = {
        "nome": "",
        "pts": -1 
    }
    for empresa in data.empresas:
        if empresa.pontos > m1["pts"]:
            m3 = m2.copy()
            m2 = m1.copy()
            m1 = {
                "nome": empresa.nome,
                "pts" : empresa.pontos
            }
        elif empresa.pontos > m2["pts"]:
            m3 = m2.copy()
            m2 = {
                "nome": empresa.nome,
                "pts" : empresa.pontos
            }
        elif empresa.pontos > m3["pts"]:
            m3 = {
                "nome": empresa.nome,
                "pts" : empresa.pontos
            }
    if (m1['nome'] != ""):
        print(f"1. {m1['nome']} - {m1["pts"]}")

    if (m2['nome'] != ""):
        print(f"2. {m2['nome']} - {m2["pts"]}")

    if (m3['nome'] != ""):
        print(f"3. {m3['nome']} - {m3["pts"]}")
