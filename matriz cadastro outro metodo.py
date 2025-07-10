matriz = []

while True:

    op = int(input('1 - cadastro \n2 - listar\n9 - sair\ninforme opção: '))

    match op:
        case 1:
            print("cadastro")
            aluno = {}
            aluno['nome'] = input("informe o nome: ")
            aluno["nota1"] = float(input("informe a nota1: "))
            aluno['nota2'] = float(input("informe a nota2: "))
            matriz.append(aluno)
        case 2:
            print("Listagem")
            for aluno in matriz:
                media = (aluno['nota1'] + aluno['nota2']) / 2
                situacao = ""
                if media >= 7:
                    situacao = "aprovado"
                else:
                    situacao = "reprovado"
                print(f'''{aluno['nome']} - {aluno['nota1']} - {aluno['nota2']} - {media} - {situacao}''')
        case 9:
            print("Obrigado")
            break
        case _:
            print("opção invalida")