print('='*30)
print('Exercicio - 33')
print('''
Faça um programa que 
leia três números 
e mostre qual é o 
maior e qual é o menor.
            ''')
print('='*30)

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

#Verificando o menor numero digitado
menor = n1
if n2 < n1 and n2 < n3 :
    menor = n2
if n3 < n1 and n3 < n2 :
    menor = n3
print(f'O menor número digitado foi {menor}.')

#Verificando o maior numero digitado
maior = n1
if n2 > n1 and n2 > n3 :
    maior = n2
if n3 > n1 and n3 > n2 :
    maior = n3

print(f'O maior número digitado foi {maior}.')