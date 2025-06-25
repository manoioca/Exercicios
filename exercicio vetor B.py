A = []

for i in range(10):
    num = int(input(f"digite o {i + 1}º número: "))
    A.append(num)

B = []

for valor in A:
    if valor % 2 == 0:
        B.append(valor * 5)
    else:
        B.append(valor + 5)


for i, valor in enumerate(B):
    print(f"B[{i}] = {valor}")

