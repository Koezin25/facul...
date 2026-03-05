#Doação de sangue
idade = int(input('Digite sua idade: '))
# Critério para doação
if 16 <= idade <= 69:
    print('apto a doar sangue!')
    if idade < 18:
        print('Você precisa da autorização dos pais.')
    elif idade > 60:
        print('Você precisa de um cadastro prévio.')
else:
    print('Não pode fazer a doação de sangue.')