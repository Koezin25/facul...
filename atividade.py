qts_numeros = int(input('Quantos valores vai digitar?' ))

contador = 0
soma = 0
negativos = 0 


while contador < qts_numeros:
    valor = int(input('Digite um número inteiro:  '))
    contador += 1 
    soma += valor
    if valor < 0:
       negativos += 1

print(f'A soma vale {soma}')
print(f'Foram inseridos {contador} números inteiros')
print(f'Foram inseridos {negativos} números inteiros negativos')