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
          7. Ver empresas cadastradas
          8. Bonificar empresa
          9. Penalizar empresa
          -----------------------
          0. Sair
          
          """)
    
    escolha = input("Input:")
    match escolha:
        case '1' : 
            funcs.descricao_solucao()

        case '2' : 
            funcs.cadastrar_empresa()

        case '3' : 
            funcs.cadastrar_satelite()

        case '4' : 
            #obter empresa
            nome_empresa = funcs.ler_nome_empresa_cadastrada()
            funcs.consultar_empresa(nome_empresa)

        case '5' : 
            funcs.ranking_score()

        case '6' : 
            funcs.relatorio_geral()

        case '7' :
            #obter a resposta
            resp = input("deseja exibir os satélites?(s/n): ").lower()
            exibir_sat = True if resp == 's' or resp == 'sim' else False
            
            funcs.exibir_empresas(exibir_sat)

        case '8' : 
            #obtem a empresa
            empresa = funcs.ler_nome_empresa_cadastrada()
            funcs.bonificar_empresa(empresa)

        case '9' : 
            #obtem a empresa
            empresa = funcs.ler_nome_empresa_cadastrada()
            funcs.penalizar_empresa(empresa)

        case '0' : break
        case _: print("Opção Inválida!!!")
    #funcao para aguardar o input
    funcs.esperar_input()