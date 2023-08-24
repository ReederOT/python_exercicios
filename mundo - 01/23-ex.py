print('='*30)
print('Exercicio - 23')
print('''
Faça um programa que leia um número de 0 a 9999
e mostre na tela cada um dos dígitos separados.
      ''')
print('='*30)

n1 = int(input('Insira um numero de 0 a 9999: '))
m = n1 // 1000 % 10
c = n1 // 100 % 10
d = n1 // 10 % 10
u = n1 // 1 % 10

print(f'\nAnalizando o número {n1}.')
print(f' Milhar:{m}') 
print(f'Centena:{c}')
print(f' Dezena:{d}')
print(f'Unidade:{u}')

print('\n')