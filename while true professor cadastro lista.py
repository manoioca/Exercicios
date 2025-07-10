
while True:
    op = int(input('1 - Cadastro\n2 - Listar\n9 - Sair\nInforme opção: '))
    
    if op == 1:
        print ("Cadastro")
    elif op ==2:
        print("Listagem")
    elif op == 9:
        print("Obrigado por utilizar nosso programa")
        break
    else:
        print("Opção inválida")