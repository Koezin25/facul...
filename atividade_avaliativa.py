# Entrda de dados

numero_de_aulas = int(input('Quantas aulas foram feitas'))
aulas_aluno = int(input('Quantas aulas o aluno estáva presente'))
nota = float(input('Qual foi a nota do aluno?'))

frequencia = aulas_aluno / numero_de_aulas

if frequencia <= 0.75:
    print('F')
elif nota < 6:
    print('R')
else:
    print('A')