print('=================================')
print('Exercicio - 06')
print('\nCrie um programa que leia um numero \n e mostre na tela seu dobro, \n e triplo, e o valor de sua raiz quadrada.')
print('=================================\n')

n = float(input('Digite um número: '))
print('=================================\n')
print('Resolução versão com 4 variaveis')
d = n*2
t = n*3
rq= n*(1/2)
print(f'O dobro de {n} é {d}')
print(f'O triplo de {n} é {t}')
print(f'A raiz quadrada de {n} é {rq}')

print('=================================\n')
print('Resolução versão com 1 variavel')
print(f'O dobro de {n} é {n*2}')
print(f'O triplo de {n} é {n*3}')
print(f'A raiz quadrada de {n} é {n*(1/2)}')
