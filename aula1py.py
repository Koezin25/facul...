print('Qual é seu ano de nascimento')
ano_nascimento = int(input())
idade = 2026 - ano_nascimento
print('Sua idade é', idade, 'anos.')

if idade < 18:
    print('Você é menor de idade.')
    print('Você precisa de uma autorização do responsável')
else:
    print('Você é menor de idade.')
print('Tchau.')        