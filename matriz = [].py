matriz = []

matriz.append("Luis")
matriz.append(43)

matriz.append("Rodrigo")
matriz.append(40)

matriz.append( ['Renato', 25] )
matriz.append( ['Paula', 20])

matriz.append( ['Feliciano', 50, 'feliciano@gmail.com'])

for i in matriz
    for j in i:
        print(j)

    for i in matriz
    try:
        print(f'{i[0]} - {i[1]} - {i[2]}')
    except:
        print(f'{i[0]} - {i[1]} -')

    print("fim")