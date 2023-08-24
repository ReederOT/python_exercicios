print('='*30)
print('Exercicio - 18')
print('\nCrie um programa que leia um angulo qualquer\ne mostre os valores do SENO, COSSENO e TANGENTE.')
print('='*30)

a1 = float(input('Digite o valor do angulo: '))

import math

print(f'O angulo {a1}, o seno vale {math.sin(math.radians(a1)):.2f}')
print(f'O angulo {a1}, o cosseno vale {math.cos(math.radians(a1)):.2f}')
print(f'O angulo {a1}, a tangente vale {math.tan(math.radians(a1)):.2f}')

