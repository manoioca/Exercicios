matriz = []

while True:
    codigo = int(input("informe o código: "))
    match codigo:  
        case 1:
            print ("cadastro")
            nome = input ("Informe o nome: ")
            nota1 = float(input("informe a nota 1: "))
            nota2 = float(input("informe a nota2: "))
            matriz.append([nome, nota1, nota2,])

        case 2:
            print ("Listagem")
            for a in matriz:
                media = (a[1] + a[2]) / 2
                situaçao = ""
                if media >= 7:
                    situacao = "aprovado"
                else:
                    situacao = "Reprovado"
                print(f"{a[0]} - {a[1]} - {a[2]} - {media} - {situacao}")
        case 9:
            print ("Obrigado por utilizar nosso programa")
            break
        case _:
            print ("Opção inválida") 

    #if codigo != 1 or codigo != 2 or codigo != 9:
        


#if codigo == 1,2,9
#    else: ("opção inválida")