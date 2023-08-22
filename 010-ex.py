print('='*30)
print('Exercicio - 10')
print('\nCrie um programa que leia quanto\ndinheiro uma pessoa tem na carteira,\ne mostre quandos dolares ela pode comprar.')
print('='*30)

real = float(input('Quanto você tem na carteira? R$ '))
dolar = float(input('Qual a cotação do dolar hoje? R$ '))
conv = real/dolar

print(f'Com R${real:.2f}, você pode comprar US${conv:.2f}.\n')

