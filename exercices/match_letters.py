# Jogo de palavras

player1 = str(input('Olá Jogador 1 , Insira a sua Palavra : '))
match = ''
pontos = 0

for i in range(len(player1)):

    player2 = input('Reconstrua a string to seu oponente letra-por-letra: ')

    if player1[i] in player2.split():
        match += player1[i]
        pontos += 1

print('Ponto Máximo: ', len(player1) )
print('A string do Jogador 1 é: ', player1)
print('Match do Jogador 2 é: ', match)
print('Classificação do Jogador 2: ', pontos, 'pontos')



