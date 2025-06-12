#1) ler o valor da hora aula
horaaula = float(input("Informe o valor da hora aula: "))
#2) ler o número de horas trabalhadas
numeroHoras = float(input("Informe o número de horas: "))
#3) ler o percentual do desconto
percentual = float(input("Informe o percentual: "))
#4) calcular o salário bruto
salariobruto = horaaula * numeroHoras
#5) Calcular o valor do desconto
valorDesconto = salariobruto * percentual / 100
#6)Calcular o salário líquido
salarioLiquido = salariobruto - valorDesconto
#7) Exibir o valor do salário líquido
#print('O salário líquido é ' + salarioLiquido )
print(f'O salário líquido é {salarioLiquido}')