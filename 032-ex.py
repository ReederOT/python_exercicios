print('='*30)
print('Exercicio - 32')
print('''
Faça um programa que leia
um ano qualquer e mostre 
se ele é bissexto.
            ''')
print('='*30)

from datetime import date #Import realizado para usara função date, para pegar data atual da maquina.

ano = int(input('Digite um ano? Digite 0, se quiser analisar o ano atual: '))

#Esse comando pega o ano atual registrado na maquina
if ano == 0:
    ano = date.today().year 

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print(f'O ano {ano} é Bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')

print('\n')