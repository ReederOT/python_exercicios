print('='*30)
print('Exercicio - 20')
print('\nCrie um programa que leia quatro nomes, e mostre a ordem dos ganhadores')
print('='*30)

from random import shuffle

n1 = str(input('Aluno 1: '))
n2 = str(input('Aluno 2: '))
n3 = str(input('Aluno 3: '))
n4 = str(input('Aluno 4: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem de apresentação será {lista}')

