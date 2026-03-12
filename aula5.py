# Entrada de dados
consumo1 = int(input('qual foi o valor da sua conta do mês passado?'))
consumo2 = int (input('qual foi o valor atual da sua conta?'))

#kwh consumido no mês
valor_mensal = consumo2 - consumo1

# Calculo do valor da conta

if valor_mensal <= 100:
    conta = 0.5*valor_mensal
elif valor_mensal <= 200:
    conta = 50 + 1*(valor_mensal - 100)
elif valor_mensal <= 300:
    conta = 150 + 1.5*(valor_mensal - 200)
else:
    conta = 300 + 2*(valor_mensal - 300)

#Exibição dos resultados

print(f'khw gasto do mês = {valor_mensal}')
print(f'Valor da conta = {conta}')
