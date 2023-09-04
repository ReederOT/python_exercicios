print('='*30)
print('Exercicio 52')
print(''' Faça um programa que leia 
      um número inteiro e diga 
      se ele é ou não um número primo.
         ''')
print('='*30)

total = 0
num = int(input('Digite um numero: '))

for c in range(1, num + 1):
        if num % c == 0:
            total = total + 1
            print('\033[33m', end=' ')
        else:
            print('\033[31m', end=' ')

        print(f'{c} \033[m', end=' ')
print(f'\nO número {num}, foi divisivel {total} vezes.')

if total == 2:
     print('Portanto é um número \033[32mPRIMO\033[m.')
else:
     print('\033[31mNÃO\033[m é um número primo')