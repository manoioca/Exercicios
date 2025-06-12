# descobrir qtd de praias
numero_praias = int(input('Insira o número de praias: '))
#nome_praia = ''
# receber informações das praias
contador_praias_15km = 0
for i in range(1,numero_praias + 1):
    nome_praia = input(f'Qual o nome da {i}a. praia: ')
    distancia_centro = float(input(f'Qual a distancia do centro da {i}a. praia: '))
    numero_medio = int(input(f'Qual o numero medio de varanistas da ultima temporada {i}a. praias'))
    tipo_acesso = int(input(f'Qual o tipo de caesso da {i}a. praia (0 - Nao asfaltado /  1 - asfaltado)'))
   

# calcular numero praias +15 km do centro
    if distancia_centro > 15:
        contador_praias_15km = contador_praias_15km + 1

print(f'Contador de praias: {contador_praias_15km}')