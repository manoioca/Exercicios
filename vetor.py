nome = 'luis'
print(nome)

nome2 = 'renato'
print(nome2)

#criando um vetor
vetor = [] #Iniciando vazio
#com valores pré-cadastrados
frutas = ['banana', 'maca', 'pera']

#adicionando valores
vetor.append('Paulo')
frutas.append("mamão")

print(vetor)
print(frutas)

print(frutas[1])


frutas[0] = 'Banana da terra'
frutas.append(nome)
frutas.append(45)
frutas.append(4.70)
frutas.insert(1, "Açaí")

entrada = input("Informe a fruta: ")
frutas.append(entrada)
frutas.remove("luis")
frutas.remove(45)
frutas.remove(4.7)
frutas.pop()
frutas.pop(0)

try:
    frutas.remove("joão")
except:
    print("informação não encontrada")
#ordenar em ordem crescente alfabetica
#ordenar em ordem decrescente
frutas.reverse()

for f in frutas:
    print(f)

frutas.sort()
#frutas.clear()
print("fim")
