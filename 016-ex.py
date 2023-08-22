print('='*30)
print('Exercicio - 16')
print('\nCrie um programa que leia um numero real qualquer\ndigitado pelo teclado e mostra tela, a sua porção inteira')
print('='*30)

print('\nUtilizando a importação')

from math import trunc
n1 = float(input('Digite um numero real: '))
print(f'O valor digitado foi {n1}, sua porção inteira é {trunc(n1)}')


print('\nUtilizando o INT, sem importação')
print(f'O valor digitado foi {n1}, sua porção inteira é {int(n1)}\n')
