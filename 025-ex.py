print('='*30)
print('Exercicio - 25')
print('''
Crie um programa que leia o nome de 
uma pessoa e diga se ela tem "SILVA" no nome.
      ''')
print('='*30)

nome = str(input('Qual seu nome completo? ')).strip()
print('Seu nome tem SILVA? {}'.format('silva' in nome.lower()))
