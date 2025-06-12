idade = 21

# > < >= <=
# != diferente
# == igual querendo comparar
# = é atribuição, a variável receber um valor
maior = idade != 18
igual = idade == 21
print(maior)

numero =  6
estadoNoIntervalo = numero >= 1 and numero <= 10
print(estadoNoIntervalo)

numero = 50
expressao2 = numero >= 5 or numero != 10
print(expressão2)

expressão3 = numero == 100 or numero < 0
print(expressão3)
      
invertendo = not(expressao2)
print(invertendo) 