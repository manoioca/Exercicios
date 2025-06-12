valor = 0.0
total = 0.0
#if codigo == 100
    #print("Cachorro quente") and valor == 12
#if codigo == 103
    #print("Hamburger") and valor == 12
#if codigo == 104 == valor == 13
    #print("cheeseburguer") and valor == 13
#if codigo == 105 == valor == 8
    #print("Refrigerante") and valor == 8

quantidade = 0.0



while True:
    codigo = input("informe o código : ") 
    quantidade = int(input("Informe a quantidade: "))
    if codigo == '100' or codigo == '103':
        valor = 12 * quantidade
    elif codigo == '104':
        valor = 13
    elif codigo == '105':
        valor = 8
    else:
        print("código inválido")
        continue
    resp = input("deseja continuar ? (Y/N)")
    if resp == 'n' or resp == 'N':
        break

total = total + (valor * quantidade)

print(f'O somatório total da conta é: {total:.2f}')