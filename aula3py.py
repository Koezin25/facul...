# Pedra - Papel - Tesoura
# Entrada com letras minúsculas
jog1 = input('Opção do jogador 1:')
jog2 = input('Opção do jogador 2:')

if jog1 == jog2:
    print('Empate!')
elif (jog1 == 'pedra' and jog2 == 'tesoura') or \
    (jog1 == 'tesoura' and jog2 == 'papel') or \
    (jog1 == 'papel' and jog2 == 'pedra'):
        print('Jogador 1 venceu!')
else:
    print('Jogador 2 venceu')