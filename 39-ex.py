print('='*30)
print('Exercicio - 39')
print('''
Faça um programa que leia 
o ano de nascimento de um jovem e informe,
de acordo com a sua idade, 
se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar ou se já passou do tempo
do alistamento.
Seu programa também deverá mostrar 
o tempo que falta ou que passou do prazo.
      ''')
print('='*30)

from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

print(f'Quem nasceu em {nasc}, tem {idade} anos em {atual}.')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE.')
elif idade < 18:
    saldo = 18 - idade 
    ano = atual + saldo
    print(f'Ainda falta {saldo} anos para o alistamento.')
    print(f'Seu alistamento será em {ano}.')
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print(f'Você ja deveria ter se alistado há {saldo} anos')
    print(f'Seu alistamento foi no ano {ano}.')