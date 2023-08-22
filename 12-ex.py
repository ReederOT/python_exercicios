print('='*30)
print('Exercicio - 12')
print('\nCrie um programa que leia o preço\nde um produto, e mostre seu novo preço,\ncom desconto de 5%.')
print('='*30)

p1 = float(input('Qual é preço do prouto? R$ '))
p2 = p1-(p1*5/100)

print(f'O produto que custava R${p1:.2f},\nna promoção com desconto de 5%\nvai custar R${p2:.2f}.')
print('='*30)