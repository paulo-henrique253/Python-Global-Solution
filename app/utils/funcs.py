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
        if empresa.nome.lower() == nome_empresa.lower():
            return empresa #caso ache uma empresa com esse nome, retorna ela
    return None # Se não encontrar, retorna nulo

def mudar_pontos(empresa: Empresa, pontos: int) -> None:
    empresa.score += pontos
    if empresa.score < 0: empresa.score = 0
    if empresa.score > 100: empresa.score = 100    

def consultar_empresa() -> None:
    nome_empresa = input("Nome: ")

    empresa = obter_empresa(nome_empresa)
    if empresa == None:
        print("Empresa não existe")
        return
    print(f"{empresa.nome} - {empresa.score}")
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
        if empresa.score > m1["pts"]:
            m3 = m2.copy()
            m2 = m1.copy()
            m1 = {
                "nome": empresa.nome,
                "pts" : empresa.score
            }
        elif empresa.score > m2["pts"]:
            m3 = m2.copy()
            m2 = {
                "nome": empresa.nome,
                "pts" : empresa.score
            }
        elif empresa.score > m3["pts"]:
            m3 = {
                "nome": empresa.nome,
                "pts" : empresa.score
            }
    if (m1['nome'] != ""):
        print(f"1. {m1['nome']} - {m1["pts"]}")

    if (m2['nome'] != ""):
        print(f"2. {m2['nome']} - {m2["pts"]}")

    if (m3['nome'] != ""):
        print(f"3. {m3['nome']} - {m3["pts"]}")


def relatorio_geral()-> None:
    num_empresas = len(data.empresas)
    num_sat = 0
    empresas_sus = 0
    for empresa in data.empresas:
        num_sat += empresa.num_satelites
        if empresa.score <= 50:
            empresas_sus +=1
    print(f"Numero de empresas: {num_empresas}")
    print(f"Numero de satelites: {num_sat}")
    print(f"Empresas suspeitas: {empresas_sus}")

def penalizar_empresa()-> None:
    empresa = input("empresa: ")

    while obter_empresa(empresa) == None:
        print("ERRO!!! empresa não existe")
        empresa = input("Empresa: ")
    
    pontos = 0
    while True:
        print("1. Alto risco de colisao                   - 15pts")
        print("2. Geração de lixo espacial                - 15pts")
        print("3. Satelite sem plano de desorbitação      - 15pts")
        print("4. Registro orbital irregular              - 20pts")
        print("5. Falta de transparência                  - 25pts")
        print("6. Geração de fragmentos orbitais          - 20pts")
        print("7. Descumprimento regulatório              - 40pts")
        print("8. Uso suspeito da infraestrutura espacial - 40pts")
        print("9. Satelite inativo em órbita              - 10pts")
        escolha = input("Escolha: ")
        match escolha:
            case '1': 
                pontos = -15
                break
            case '2': 
                pontos = -15
                break
            case '3': 
                pontos = -15
                break
            case '4': 
                pontos = -20
                break
            case '5': 
                pontos = -25
                break
            case '6': 
                pontos = -20
                break
            case '7': 
                pontos = -40
                break
            case '8': 
                pontos = -40
                break
            case '9': 
                pontos = -10
                break
            case _: print("Opçao invalida")
    empresa_obj = obter_empresa(empresa)
    mudar_pontos(empresa_obj, pontos)
    print(f"A empresa {empresa} perdeu {abs(pontos)} pontos. Agora tem {empresa_obj.score}")


def bonificar_empresa()-> None:
    empresa = input("empresa: ")

    while obter_empresa(empresa) == None:
        print("ERRO!!! empresa não existe")
        empresa = input("Empresa: ")
    
    pontos = 0
    while True:
        print("1. Desorbitação resonsável                - 20pts")
        print("2. Baixo risco de colisão                 - 15pts")
        print("3. Satélite ativo e regularizado          - 10pts")
        print("4. Plano de mitigação aprovado            - 25pts")
        print("5. Baixa geração de lixo espacial         - 20pts")
        print("6. Registro orbital regular               - 10pts")
        print("7. Transparencia de dados                 - 15pts")
        print("8. Participação em iniciativa sustentável - 30pts")
        print("9. Conformidade regulatória               - 10pts")
        escolha = input("Escolha: ")
        match escolha:
            case '1': 
                pontos = 20
                break
            case '2': 
                pontos = 15
                break
            case '3': 
                pontos = 10
                break
            case '4': 
                pontos = 25
                break
            case '5': 
                pontos = 20
                break
            case '6': 
                pontos = 10
                break
            case '7': 
                pontos = 15
                break
            case '8': 
                pontos = 30
                break
            case '9': 
                pontos = 10
                break
            case _: print("Opçao invalida")
    empresa_obj = obter_empresa(empresa)
    mudar_pontos(empresa_obj , pontos)
    print(f"A empresa {empresa} ganhou {pontos} pontos. Agora tem {empresa_obj.score} pontos")


def descricao_solucao() -> None:
    print("""
===== CONHEÇA A ORBITS =====
          
          blablablablablablabla
          blablablablablablabla
          blablablablablablabla
          blablablablablablabla
          blablablablablablabla
          
          """)