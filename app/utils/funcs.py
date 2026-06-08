import sys
import os

sys.path.append(
    os.path.abspath("./app")
)
import utils.data as data
from models.empresa import Empresa
from models.empresa import AcaoPontuada
from models.empresa import Penalidade
from models.empresa import Bonificacao

from models.satelite import TipoOrbita

from models.satelite import StatusOperacao
from models.satelite import Satelite





#region input
# =====================
# SUBALGS INPUT
# =====================


#Procedimento para aguardar o input e permitir a leitura dos prints
def esperar_input() -> None:
    input("\naperte enter para continuar")

#le o nome da empresa e garante valores validos
def ler_input_obrigatorio(mensagem: str) -> str:
    linha = input(mensagem)
    while linha == "":
        print("ERRO!!! O campo não pode estar vazio!")
        linha = input(mensagem)
    return linha

#funcao para ler uma empresa que não exista ainda (cadastro)
def ler_nome_empresa_nova() -> str:

    #input ja é diferente de "" (string vazia)
    nome_empresa = ler_input_obrigatorio("Nome: ")

    # Forçar o input de uma empresa válida
    while obter_empresa(nome_empresa) is not None:

        #exibe o erro
        print("ERRO!!! Empresa ja cadastrada")
            
        nome_empresa = ler_input_obrigatorio("Nome: ")

    #retorna o nome válido
    return nome_empresa

#funcao para ler uma empresa ja cadastrada (consulta)
def ler_nome_empresa_cadastrada() -> str:
    #ve o input de uma emrpesa
    nome_empresa = input("Empresa: ")

    #força o input a ser uma empresa cadastrada
    while obter_empresa(nome_empresa) is None:
        #exibe o erro
        print("ERRO!!! Empresa não cadastrada")
        nome_empresa = input("Empresa: ")
    #retorna o nome válido
    return nome_empresa

#funcao para ler um satélite  que não exista ainda (cadastro)
def ler_nome_satelite_novo(nome_empresa : str) -> str:
    nome_satelite = ler_input_obrigatorio("Satélite: ")
    while obter_satelite(nome_satelite, nome_empresa) is not None:
        print("ERRO!!! Satélite ja cadastrado para essa empresa!")
        nome_satelite = ler_input_obrigatorio("Satélite: ")
    return nome_satelite


def ler_orbita() -> str:

    #inicializa a variavel vazia
    orbita = ""

    #até o usuário digitar uma órbita válida..
    while not eh_orbita(orbita):

        #mostra as órbitas na tela
        print("\nInsira o tipo de órbita(uma dentre as seguintes)\n")
        for orb in TipoOrbita:
            print(orb.value)

        #obtem o input da orbita
        orbita = input("Órbita(insira o valor completo): ").lower()
    return orbita

def ler_status_satelite() -> str:
    #inicializa a variavel
    status = ""

    #até o usuário digitar um status valido...
    while not eh_status(status):

        #mostra os status na tela
        print("Insira o tipo de status:")
        for status in StatusOperacao:
            print( '\n' + status.value, end="")
        print()

        #obtem o input do status
        status = input("Status(Insira o valor completo): ").lower()
    return status


def ler_opcao_enum(enum_class: AcaoPontuada) -> int:
    opcoes = list(enum_class)

    while True:
        print()

        exibir_opcao_enum(enum_class)

        escolha = input("\nEscolha: ")

        if escolha.isdigit():
            indice = int(escolha) - 1

            if 0 <= indice < len(opcoes):
                return opcoes[indice].pontos
        elif escolha.lower() in [opcao.descricao.lower() for opcao in opcoes]:
            for opcao in opcoes:
                if escolha.lower() == opcao.descricao.lower():
                    return opcao.pontos
        print("Opção inválida")
#endregion input

#region print
# =====================
# SUBALGS PRINT
# =====================

#exibe um unico sátelite formatadinho
def exibir_satelite(satelite: Satelite) -> None:
        print(f"\t{satelite.nome:>21} | Tipo de órbita: {satelite.orbita.value:15} | Status: {satelite.status}")

#exibe TODOS os satelites de uma empresa
def exibir_satelites(empresa: Empresa) -> None:

    if len(empresa.satelites) == 0: #Se o tamanho do array é 0, empresa não tem nenhum satélite
        print("\tEssa empresa não tem satélites cadastrados!")
        return #interrompe o procedimento
    
    #percorre a lista
    for satelite in empresa.satelites:

        #Mostra cada satélite
        exibir_satelite(satelite)

#exibe uma empresa formatada
def exibir_empresa(empresa : Empresa, exibir_sat: bool = False) -> None:
    print(f"{empresa.nome:-^12}: {empresa.score} pontos | Pais: {empresa.pais}")

    #caso exibir satélite seja verdade, exibir todos os satélites
    if exibir_sat:
        print("\tsatélites:")
        for satelite in empresa.satelites:
            exibir_satelite(satelite)

#Procedimento para mostrar as empresas cadastradas
def exibir_empresas(exibir_sat: bool = False) -> None:

    #copia a lista com os nomes das empresas
    lista_empresas = [empresa.nome for empresa in data.empresas]

    #ordena a lista
    lista_empresas.sort()

    #percorre a lista
    for empresa_nome in lista_empresas:
        #obtem o objeto empresa para cada nome
        empresa = obter_empresa(empresa_nome)

        #Exibe as informações da empresa
        exibir_empresa(empresa, exibir_sat)
        
def exibir_opcao_enum(enum_class: AcaoPontuada):
    opcoes = list(enum_class)
    for i, opcao in enumerate(opcoes, start=1):
            print(
                f"{i}. {opcao.descricao:<40}"
                f"{opcao.pontos:+} pts"
            )
#endregion print

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
def consultar_empresa(nome_empresa: str) -> None:

    #Obtem a empresa com esse nome
    empresa = obter_empresa(nome_empresa)

    #Se não obter nenhuma empresa, a empresa digitada não existe no sistema
    if empresa == None:
        print("Empresa não existe")
        return #Interrompe o procedimento
    
    #Exibe o nome e os pontos da empresa
    exibir_empresa(empresa)

    #Obtem a resposto usuário 
    resp = input("Gostaria de ver os satélites registrados(s/n): ").lower()
    if resp == 's' or resp == "sim":     
        exibir_satelites(empresa)
        

# Cadastrar uma empresa
def cadastrar_empresa() -> None:
    #Input do nome
    nome_empresa = ler_nome_empresa_nova()

    #input do pais (não nulo)
    pais_empresa = ler_input_obrigatorio("Pais: ")
    
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
    nome_empresa = ler_nome_empresa_cadastrada()

    #input para o nome do satélite
    nome_satelite = ler_nome_satelite_novo(nome_empresa)

    #Declara a variavel da orbita
    orbita_satelite = ler_orbita()
    
    #Declara a variavel do status
    status_satelite = ler_status_satelite()

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
def penalizar_empresa(empresa: Empresa)-> None:
    
    #declara a variável pontos(será usada mais tarde)
    pontos = ler_opcao_enum(Penalidade)
    
    #obrem o objeto empresa com esse nome
    empresa_obj = obter_empresa(empresa)

    #muda os pontos do objeto
    mudar_pontos(empresa_obj, pontos)

    #exibe as informações na tela
    print(f"A empresa {empresa} perdeu {abs(pontos)} pontos. Agora tem {empresa_obj.score}")

#procedimento para bonificar uma empresa
def bonificar_empresa(empresa: Empresa)-> None:

    #declara a variavel pontos
    pontos = ler_opcao_enum(Bonificacao)
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