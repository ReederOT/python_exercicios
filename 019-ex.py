print('='*30)
print('Exercicio - 19')
print('\nCrie um programa que leia quatro nomes, e sorteie um dos nomes')
print('='*30)

import random

n1 = str(input('Aluno 1: '))
n2 = str(input('Aluno 2: '))
n3 = str(input('Aluno 3: '))
n4 = str(input('Aluno 4: '))
lista = [n1, n2, n3, n4]

print(f'Aluno sorteado foi {random.choice(lista)}')

