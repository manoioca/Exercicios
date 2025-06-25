A = []
soma_ímpares = 0

for i in range(10): 
    num = int(input(f"digite o {i + 1}º número: "))
    A.append(num)

    if num % 2 != 0:
        soma_ímpares; soma_ímpares = soma_ímpares + num

print("soma dos números ímpares", soma_ímpares)