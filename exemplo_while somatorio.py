# um programa que fará a leitura de número que representará a idade de pessoas ao final do programa o mesmo deverá informar 
# o somatório das idades, o numero de pessoas e a média das idades.

soma = 0
numeroPessoas = 0
media = 0

while True:
    idade = int(input("informe a sua idade: ")) 
    soma = soma + idade
    numeroPessoas = numeroPessoas + 1
    resp = input("Deseja continuar? (s/n) ")
    if resp == 'n' or resp == 'N':
        break


media = soma / numeroPessoas
print(f'O somatório das idades é {soma}')
print(f'O numero de pessoas é {numeroPessoas}')
print(f'A média das idades é {media:.2f}')