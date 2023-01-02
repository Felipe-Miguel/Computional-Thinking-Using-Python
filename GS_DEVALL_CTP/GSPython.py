# Caio Henrique Martins    RM 93935
# Carolina Puig            RM 95078
# Felipe Miguel de Souza   RM 94921
# Guilherme Costa          RM 93642
# Isadora Antunes          RM 94785

def imprime_menu():
    print("\nMENU PRINCIPAL\n")
    print("1 – Cadastrar mês de referência")
    print("2 – Exibir dados do mês de referência [pesquisa por mês]")
    print("3 – Relatório comparativo – Referência 2019")
    print("4 – Listar todos os meses cadastrados")
    print("5 - Sair")
    return input("\nDigite a opção desejada: ")
    
def coleta_registro(tabela):
    print("\nCADASTRANDO MÊS-ANO DE REFERÊNCIA\n")
    registro = {}
    registro['mes_ano_referencia'] = input("Mês-ano..............: ")
    registro['total_habitantes'] = int(input("Total de Habitantes..: "))
    registro['total_obitos'] = int(input("Total de óbitos......: "))
    tabela.append(registro)
    print("\n***** Gravado com sucesso *****")
    return tabela

# def ordena_registros(tabela):
#     for i in range(len(tabela)):
#         registro = tabela[i]
#         while i > 0 and tabela[i - 1]['mes_ano_referencia'][-4:] > registro['mes_ano_referencia'][-4:]:
#             tabela[i] = tabela[i - 1]
#             i -= 1
#         while i > 0 and tabela[i - 1]['mes_ano_referencia'][:2] > registro['mes_ano_referencia'][:2]:
#             tabela[i] = tabela[i - 1]
#             i -= 1
#         tabela[i] = registro
#     return tabela

def imprime_registro(registro):
    print("\nMês-ano..............:",registro['mes_ano_referencia'])
    print("Total de Habitantes..:",registro['total_habitantes'])
    print("Total de óbitos......:",registro['total_obitos'])
    return

def busca_registro(tabela):
    print("\nCONSULTANDO MÊS-ANO DE REFERÊNCIA\n")
    busca = input("Digite o mês-ano desejado.....: ")
    for registro in tabela:
        if registro['mes_ano_referencia'] == busca:
            imprime_registro(registro)
            print("\n***** Registro encontrado *****")
            return
    print("\n***** Mês-ano não cadastrado! *****")
    return

def compara_dados(tabela):
    print("\nRELATÓRIO COMPARATIVO DE TAXA DE MORTALIDADE ANUAL\n")
    ano = input("Digite ano a ser comparado........: ")
    soma_habitantes = 0
    soma_obitos = 0
    for registro in tabela:
        if registro['mes_ano_referencia'][-4:] == ano:
            soma_habitantes += registro['total_habitantes']
            soma_obitos += registro['total_obitos']
    if soma_habitantes == 0:
        print("\n***** Ano não encontrado! *****")
    else:
        taxa = round(soma_obitos/(soma_habitantes/100000),2)
        diferenca = round((taxa-15)*100/15,1)
        print(f"\nTotal de Habitantes...............: {soma_habitantes}")
        print(f"Total de óbitos...................: {soma_obitos}")
        print(f"Taxa por 100k habitantes - {ano}...: {taxa}")
        print("Taxa por 100k habitantes - 2019...: 15.00")
        print(f"\nComparativo % entre {ano}-2019.....:",f"+{diferenca}%" if diferenca>0 else f"{diferenca}%")
    return

def lista_registros(tabela):
    print("\nLISTA DE REGISTROS\n")
    for registro in tabela:
        imprime_registro(registro)
    return

def principal():
    tabela = []
    while True:
        opt = imprime_menu()
        if opt == "1":
            tabela = coleta_registro(tabela)
        elif opt == "2":
            busca_registro(tabela)
        elif opt == "3":
            compara_dados(tabela)
        elif opt == "4":
            # tabela = ordena_registros(tabela)
            lista_registros(tabela)
        elif opt == "5":
            break
        else:
            print("***** Opção inválida! *****")

principal()