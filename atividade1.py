N = int(input())

valores = []

for _ in range(N):
    numero = float(input())
    valores.append(numero)

print(valores)

if N > 0:
    media = sum(valores) / N
else:
    media = 0.0

print(media)