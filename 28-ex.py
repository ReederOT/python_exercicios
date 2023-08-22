print('='*30)
print('Exercicio - 28')
print('''
Escreva um programa que faça o computador "pensar"
em um número inteiro entre 0 e 5 e peça para o 
usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
      ''')
print('='*30)
print('\n')

from random import randint
from time import sleep
num = randint(0, 5)
print('=-'*12)
print('Vou pensar em um número.')
print('=-'*12)
palpite = int(input('Em qual numero pensei? '))
print('PROCESSANDO...')
sleep(3)

if num == palpite:
    print(f'Eu pensei no numero {num}')
    print('Parabéns você acertou!!!')
else:
    print(f'Eu pensei no numero {num}')
    print('E você errou.')







