print('='*30)
print('Exercicio - 44')
print('''
Elabore um programa que calcule
o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros ''')
print('='*30)

print('\n=========== LOJINHA ===========')
preco = float(input('Preço das compras:R$'))
print('FORMAS DE PAGAMENTO:')
print('''
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão''')
fpagto = int(input('Qual é a opção? '))
if fpagto == 1:
    preconovo = preco - (preco * 10 / 100 )
elif fpagto == 2:
    preconovo = preco - (preco * 5 / 100)
elif fpagto == 3:
    preconovo = preco
    parc = preco / 2
    print(f'Sua será parcelada em 2x com parcelas de R${parc:.2f} sem juros.')
elif fpagto == 4:
    preconovo = preco + (preco * 20 / 100)
    totalparc = int(input('Qual o total de parcelas? '))
    parc = preconovo / totalparc
    print(f'Sua compra será parcelada em {totalparc}x de R${parc:.2f} com juros.')
else: 
    print('Opção invalida, tente novamente')
    preconovo = preco
print(f'Sua compra de R${preco:.2f}, vai custar R${preconovo:.2f} no final.')

