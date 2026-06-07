import os
import utils.funcs as funcs
os.system("cls")

while True:
    print("""=== Seja bem vindo(a) ao sistema da Orbits ===
          
          1. Conhecer a Orbits
          2. Cadastrar empresa
          3. Cadastrar satélite
          4. Consultar empresa
          5. Top 3 empresas
          6. Registro geral
          7. Bonificar empresa
          8. Penalizar empresa
          -----------------------
          0. Sair
          
          """)
    
    escolha = input("Input:")
    match escolha:
        case '1' : funcs.descricao_solucao()
        case '2' : funcs.cadastrar_empresa()
        case '3' : funcs.cadastrar_satelite()
        case '4' : funcs.consultar_empresa()
        case '5' : funcs.ranking_score()
        case '6' : funcs.relatorio_geral()
        case '7' : funcs.bonificar_empresa()
        case '8' : funcs.penalizar_empresa()
        case '0' : break
        case _: print("Opção Inválida!!!")