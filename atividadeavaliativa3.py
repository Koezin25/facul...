turma = int(input('Qual o tamanho da turma: ' ))

contador = 0
aprovados = 0
reprovados = 0 

while turma > contador:
    nota = float(input('Digite a nota do aluno: '))
    contador += 1 
    
    if nota > 6.0:
        aprovados = aprovados + 1
    if nota < 6.0:
        reprovados = reprovados + 1
       

print(f'A quantidade de aprovados foram {aprovados}')
print(f'A quantidade de reprovados foram {reprovados}')    