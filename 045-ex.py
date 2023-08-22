print('='*30)
print('Desafio 45')
print('''Crie um programa que 
      faça o computador jogar
      Jokenpô com você
         ''')
print('='*30)

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura      
''')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print('=-'*12)
print(f'O computador jogou {itens[computador]}.')
print(f'O jogador jogou {itens[jogador]}.')
print('-='*12)

if computador == 0: #Computador jogou pedra
    if jogador == 0: #Jogador jogou pedra
        print('EMPATE.')
    elif jogador == 1: #Jogador jogou papel
        print('Jogador VENCEU.')
    elif jogador == 2: #Jogador jogou tesoura
        print('Computador VENCEU')
    else:
        print('Jogada invalida.')

elif computador == 1: #Computador jogou papel
    if jogador == 0 :#Jogador jogou pedra
        print('Computador VENCEU')
    elif jogador == 1: #Jogador jogou papel
        print('EMPATE.')
    elif jogador == 2: #Jogador jogou tesoura
        print('Jogador VENCEU.')
    else:
        print('Jogada invalida')


elif computador == 2: #Computador jogou tesoura
    if jogador == 0: #Jogador jogou pedra
        print('Jogador VENCEU.')
    elif jogador == 1 : #Jogador jogou papel
        print('Computador VENCEU')
    elif jogador == 2: #Jogador jogou tesoura
        print('EMPATE.')
    else:
        print('Jogada invalida')
else:
    print('Jogada Invalida')