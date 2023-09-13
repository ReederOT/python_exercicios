print('='*30)
print('Exercicio 54')
print(''' Crie um programa que leia 
      o ano de nascimento de sete pessoas.
      No final, mostre quantas pessoas ainda
      não atingiram a maioridade e quantas já são maiores.
         ''')
print('='*30)


from datetime import date

maior = 0
menor = 0
atual = date.today().year

for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}º pessoa nasceu? '))

    if atual - ano < 18:
        menor = menor + 1
    else:
        maior = maior + 1

print(f'Ao todo tivemos {maior} pessoas maiores de idade,')
print(f'e também tivemos {menor} pessoas menores de idade. ')

