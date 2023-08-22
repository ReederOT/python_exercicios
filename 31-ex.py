print('='*30)
print('Exercicio - 31')
print('''
Desenvolva um programa que pergunte
a distância de uma viagem em Km. 
Calcule o preço da passagem, 
cobrando R$0,50 por Km para viagens de até 200Km
e R$0,45 parta viagens mais longas.
            ''')
print('='*30)

viagem = float(input('Qual é a distancia da sua viagem? '))

if viagem <= 200:
    custo = viagem * 0.50
else:
    custo = viagem * 0.45

print(f'Você está prestes a começar uma viagem de {viagem}km.')
print(f'O custo dessa viagem será de R${custo:.2f}.')
print('\n')


