tempogasto = float(input("Informe o tempo gasto: "))
velocidade = float(input("Informe a velocidade: "))

distancia = tempogasto * velocidade

litros_usados = distancia / 12

print(f'A velocidade é: {velocidade}')
print(f'o tempo é: {tempogasto}')
print(f'distancia percorrida é: {distancia}')
print(f'Quantidade de litros usados é de: {litros_usados:.3f}')