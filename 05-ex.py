print('=================================')
print('Exercicio - 05')
print('\nCrie um programa que leia um numero numero inteiro\n e mostre na tela seu sucessor \n e seu antecessor.')
print('=================================')


n = int(input('Digite um número: '))
print('=================================\n')
print('Resolução versão com 3 variaveis')
a = n-1
s = n+1
print(f'Analizando o numero {n}, o seu antecessor é {a}, e seu sucessor é {s}')

print('=================================\n')
print('Resolução versão com 1 variavel')
print(f'Analizando o numero {n}, o seu antecessor é {n-1}, e seu sucessor é {n+1}')