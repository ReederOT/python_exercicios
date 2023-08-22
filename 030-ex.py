print('='*30)
print('Exercicio - 30')
print('''
Crie um programa que leia
um número inteiro e mostre na 
tela se ele é PAR ou ÍMPAR.
      ''')
print('='*30)

num = int(input('Digite um valor: '))

if num % 2 == 1: #faz a comparação se o resto da divisão é igual a 1
    print(f'O número {num} é impar') #se for igual a 1, o numero é impar
else:
    print(f'O número {num} é par') #se não for igual a 1, o numero é par
