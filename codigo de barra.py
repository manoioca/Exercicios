codigo = int(input("informe o código: "))

if codigo == 1:
    print("alimento nao-perecível")
          
elif codigo == 2 or codigo == 3 or codigo == 4:
    print("alimento perecível")
elif codigo == 5 or codigo == 6:
    print("vestuário")
elif codigo == 7:
    print("higiene pessoal")
elif codigo == 8 or codigo == 9 or codigo == 10:
    print("Utensílios domésticos")
else:
    print("inválido!!!")