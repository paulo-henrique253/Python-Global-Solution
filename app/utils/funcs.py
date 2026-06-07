import sys
import os

sys.path.append(
    os.path.abspath("./app")
)
import utils.data as data
from models.empresa import Empresa
from models.satelite import TipoOrbita
from models.satelite import StatusOperacao
from models.satelite import Satelite

#Funcao para pegar uma empresa cadastrada pelo nome
def obter_empresa(nome_empresa: str) -> Empresa:
    # Percorrer a lista
    for empresa in data.empresas:
        if empresa.nome.lower() == nome_empresa.lower():
            return empresa #caso ache uma empresa com esse nome, retorna ela
    return None # Se não encontrar, retorna None

#obter um satélite de uma empresa
def obter_satelite(nome_satelite: str, nome_empresa: str) -> Satelite:
    #Obter o objeto empresa
    empresa = obter_empresa(nome_empresa)

    #percorrer a lista
    for satelite in empresa.satelites:

        #se o nome do satélite for o nome passado como parametro, retorna o objeto
        if satelite.nome.lower() == nome_satelite.lower():
            return satelite
    return None # se não encontrar nada


#procedimento para alterar os pontos de uma empresa de forma segura
def mudar_pontos(empresa: Empresa, pontos: int) -> None:
    empresa.score += pontos

    #Não permite o score de uma empresa ser maior que 100 ou menor que 0
    if empresa.score < 0: empresa.score = 0
    if empresa.score > 100: empresa.score = 100    


#procedimento para permitir que o usuário encontre uma empresa e veja suas informações
def consultar_empresa() -> None:
    #Pega o input do usuário
    nome_empresa = input("Nome: ")

    #Obtem a empresa com esse nome
    empresa = obter_empresa(nome_empresa)

    #Se não obter nenhuma empresa, a empresa digitada não existe no sistema
    if empresa == None:
        print("Empresa não existe")
        return #Interrompe o procedimento
    
    #Exibe o nome e os pontos da empresa
    print(f"{empresa.nome} - score: {empresa.score}")

    #Obtem a resposto usuário 
    resp = input("Gostaria de ver os satélites registrados(s/n): ").lower()
    if resp == 's' or resp == "sim":

        if len(empresa.satelites) == 0: #Se o tamanho do array é 0, empresa não tem nenhum satélite
            print("Essa empresa não tem satélites cadastrados!")
            return #interrompe o procedimento
        
        #Percorre a lista de satélites
        for satelite in empresa.satelites:
            #exibe o satélite e seu status
            print(f"{satelite.nome} - Status: {satelite.status}")
        

# Cadastrar uma empresa
def cadastrar_empresa() -> None:
    #Inpu do nome
    nome_empresa = input("Nome: ")
    # Forçar o input de uma empresa válida
    while nome_empresa == "" or obter_empresa(nome_empresa) != None:
        if nome_empresa == "":
            print("ERRO!!! Insira um nome")
        else:
            print("ERRO!!! Empresa ja cadastrada")
        nome_empresa = input("Nome: ")

    #input do pais
    pais_empresa = input("Pais: ")

    #Força o input de um pais não nulo
    while pais_empresa == "":
        print("ERRO!!! Insira um país")
        pais_empresa = input("Pais: ")
    
    #adiciona a empresa com as informacoes
    data.adicionar_empresa(nome_empresa, pais_empresa)

#Função que verifica se um dado é(eh) uma orbita valida
def eh_orbita(info) -> bool:
    #Se esta na lista de valores do enum TipoOrbita, retorna True
    if info in [tipo.value for tipo in TipoOrbita]:
        return True
    return False

#Função que verifica se um dado é(eh) um status valido para satelite
def eh_status(info) -> bool:
    #Se esta na lista de valores do enum StatusOperacao, retorna True
    if info in [status.value for status in StatusOperacao]:
        return True
    return False


#Procedimento para cadastrar satélite
def cadastrar_satelite() -> None:

    #input para a empresa do satélite
    nome_empresa = input("Empresa: ")

    #força o input a ser uma empresa cadastrada
    while obter_empresa(nome_empresa) == None:
        print("ERRO!!! Insira uma empresa cadastrada")
        nome_empresa = input("Empresa: ")

    #input para o nome do satélite
    nome_satelite = input("Nome: ")

    #força o nome a ser diferente de uma string vazia
    while nome_satelite == "" or obter_satelite(nome_satelite, nome_empresa) != None:
        if nome_satelite == "":
            print("ERRO!!! Insira um nome")
        else:
            print("ERRO!!! Satélite já cadastrado nessa emrpesa!")
        nome_satelite = input("Nome: ")
    
    
    
    #Declara a variavel da orbita
    orbita_satelite = ""

    #até o usuário digitar uma órbita válida..
    while not eh_orbita(orbita_satelite):
        #mostra as órbitas na tela
        print("\nInsira o tipo de órbita(uma dentre as seguintes)")
        for orb in TipoOrbita:
            print('\n' + orb.value, end="")
        print()
        #obtem o input da orbita
        orbita_satelite = input("Órbita(insira o valor completo): ").lower()
    
    #Declara a variavel do status
    status_satelite = ""

    #até o usuário digitar um status valido...
    while not eh_status(status_satelite):
        #mostra os status na tela
        print("Insira o tipo de status:")
        for status in StatusOperacao:
            print( '\n' + status.value, end="")
        print()
        #obtem o input do status
        status_satelite = input("Status(Insira o valor completo): ").lower()

    #adiciona o satelite na lista
    data.adicionar_satelite(nome_satelite, nome_empresa, orbita_satelite, status_satelite)

#Procedimento para exibir as 3 empresas mais bem rankeadas
def ranking_score() -> None:
    #Declara 3 objetos que guardaram as 3 maiores informações
    m1 = {
        "Nome": "",
        "pts": -1 
    }
    m2 = {
        "Nome": "",
        "pts": -1 
    }
    m3 = {
        "Nome": "",
        "pts": -1 
    }
    #percorre a lista de empresas
    for empresa in data.empresas:
        #se o score da empresa atual for maior que da variavel m1
        #Guarda a empresa em m1, e guarda as informacoes de m1(antiga maior)
        #em m2, e de m2 em m3
        if empresa.score > m1["pts"]:
            m3 = m2.copy()
            m2 = m1.copy()
            m1 = {
                "Nome": empresa.nome,
                "pts" : empresa.score
            }
        #Se não, verifica se é maior que m2, e se sim,
        #guarda as informacoes em m2, e o que estavam em m2 guarda em m3
        elif empresa.score > m2["pts"]:
            m3 = m2.copy()
            m2 = {
                "Nome": empresa.nome,
                "pts" : empresa.score
            }
        #se não, verifica se é maior que me, e se for, guarda as informacoes em m3
        elif empresa.score > m3["pts"]:
            m3 = {
                "Nome": empresa.nome,
                "pts" : empresa.score
            }
    
    #se não for vazio, exibe na tela
    if (m1['Nome'] != ""):
        print(f"1. {m1['Nome']} - {m1['pts']}")

    #se não for vazio, exibe na tela
    if (m2['Nome'] != ""):
        print(f"2. {m2['Nome']} - {m2['pts']}")

    #se não for vazio, exibe na tela
    if (m3['Nome'] != ""):
        print(f"3. {m3['Nome']} - {m3['pts']}")


#procedimento para mostrar informacoes gerais
def relatorio_geral()-> None:
    #declara as variaveis
    num_empresas = len(data.empresas)
    num_sat = 0
    empresas_sus = 0

    #percorre todas as empresas
    for empresa in data.empresas:
        #adiciona o numero de satelites
        num_sat += len(empresa.satelites)

        #se a empresa for suspeita(score menor que 50), conta um em empresas_sus
        if empresa.score <= 50:
            empresas_sus +=1

    #Exibe as informações
    print(f"Número de empresas: {num_empresas}")
    print(f"Número de satelites: {num_sat}")
    print(f"Empresas suspeitas: {empresas_sus}")

#procedimento para penalizar uma empresa
def penalizar_empresa()-> None:
    #obtem a empresa
    empresa = input("Empresa: ")

    #força o usuário a digitar uma empreswa cadastrada
    while obter_empresa(empresa) == None:
        print("ERRO!!! Empresa não existe")
        empresa = input("Empresa: ")
    
    #declara a variável pontos(será usada mais tarde)
    pontos = 0
    while True:
        #mostra na tela as penalidades
        print("""
                1. Alto risco de colisao                   - 15pts
                2. Geração de lixo espacial                - 15pts
                3. Satélite sem plano de desorbitação      - 15pts
                4. Registro orbital irregular              - 20pts
                5. Falta de transparência                  - 25pts
                6. Geração de fragmentos orbitais          - 20pts
                7. Descumprimento regulatório              - 40pts
                8. Uso suspeito da infraestrutura espacial - 40pts
                9. Satélite inativo em órbita              - 10pts
              """)
        #verifica qual foi a penalidade escolhida
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
            case _: print("Opção invalida")
    
    #obrem o objeto empresa com esse nome
    empresa_obj = obter_empresa(empresa)

    #muda os pontos do objeto
    mudar_pontos(empresa_obj, pontos)

    #exibe as informações na tela
    print(f"A empresa {empresa} perdeu {abs(pontos)} pontos. Agora tem {empresa_obj.score}")

#procedimento para bonificar uma empresa
def bonificar_empresa()-> None:
    #obtem o nome da empresa
    empresa = input("Empresa: ")

    #força a empresa a ser uma cadastrada
    while obter_empresa(empresa) == None:
        print("ERRO!!! Empresa não existe")
        empresa = input("Empresa: ")
    
    #declara a variavel pontos
    pontos = 0
    while True:
        #exibe as opções na tela
        print("""
                1. Desorbitação resonsável                - 20pts
                2. Baixo risco de colisão                 - 15pts
                3. Satélite ativo e regularizado          - 10pts
                4. Plano de mitigação aprovado            - 25pts
                5. Baixa geração de lixo espacial         - 20pts
                6. Registro orbital regular               - 10pts
                7. Transparencia de dados                 - 15pts
                8. Participação em iniciativa sustentável - 30pts
                9. Conformidade regulatória               - 10pts
            """)

        #obtem a escolha do usuário
        escolha = input("Escolha: ")

        #Verifica qual foi a opção escolhida de muda os pontos 
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
            case _: print("Opção invalida")
    #obtem o objeto empresa cadastrado com esse nome
    empresa_obj = obter_empresa(empresa)

    #muda os pontos do objeto
    mudar_pontos(empresa_obj , pontos)

    #exibe as informações na tela
    print(f"A empresa {empresa} ganhou {pontos} pontos. Agora tem {empresa_obj.score} pontos")


def descricao_solucao() -> None:
    print("""
===== CONHEÇA A ORBITS =====
          
A Orbits é uma plataforma pública de transparência e governança da economia espacial que centraliza informações sobre o espaço. Utilizamos os dados das diversas empresas do ecossistema espacial para criar um ambiente de monitoramento de suas ações, tornando capaz que monitore satélites ativos e empresas cadastradas. Utilizamos um score para as empresas que pode varias caso suas ações sejam positivas ou negativas para o meio ambiente. Nosso objetivo é tornar o espaço um lugar seguro e com impactos positivos no futuro da humanidade, livre da exploração indevida.

          
          """)