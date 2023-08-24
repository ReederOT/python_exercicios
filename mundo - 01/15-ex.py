print('='*30)
print('Exercicio - 15')
print('\nCrie um programa que que pergunte a quantidade de Km\npercorridos por um carro alugado e a quantidade de dias\n')
print('pelos quais ele foi alugado.\nCalcule o preço a pagar,\nsabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.')
print('='*30)

dias = int(input('O foi alugado por quantos dias? '))
km = float(input("Quantos km's foram rodados? "))
total = (dias*60)+(0.15*km)

print(f'O total a pagar pelo aluguel do carro é R${total:.2f}.')
print('='*30)
