import os
import utils.funcs as funcs
os.system("cls")

while True:
    print("1. Cadastrar empresa")
    print("2. Cadastrar satélite")
    print("3. Consultar empresa")
    print("4. Top 3 empresas")
    print("5. Registro geral")
    print("\t0 - Sair")

    escolha = input("Input:")
    match escolha:
        case '1' : funcs.cadastrar_empresa()
        case '2' : funcs.cadastrar_satelite()
        case '3' : funcs.consultar_empresa()
        case '4' : funcs.ranking_score()
        case '5' : funcs.registro_geral()
        case '0' : break
        case _: print("Opção Inválida!!!")