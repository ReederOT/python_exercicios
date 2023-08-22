print('='*30)
print('Exercicio - 17')
print('\nCrie um programa que leia o comprimento do cateto oposto\ne do catero adjacente do triangulo retangulo,\ne mostre o valor da hipotenusa')
print('='*30)

from math import hypot
a1 = float(input('Digite o valor do cateto oposto: '))
a2 = float(input('Digite o valor do cateto adjacente: '))

print(f'A hipotenusa vai medir {hypot(a1, a2):.2f}')

