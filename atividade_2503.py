qnt_temp = int(input('Quantas temperaturas serão avaliadas?' ))

contador = 0
temp_fora = 0

while contador < qnt_temp:
    temp = int(input('Temperatura atual: '))
    contador += 1
    if not 26 <= temp <= 30:
        temp_fora += 1

porcentagem = temp_fora / qnt_temp * 100
print(f'Porcentagem de temperaturas fora da faixa = {porcentagem:.2f}%')