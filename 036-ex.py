print('='*30)
print('Exercicio - 3')
print('='*30)

print('''Escreva um programa para 
      aprovar o empréstimo bancário
      para a compra de uma casa. 
      Pergunte o valor da casa, 
      o salário do comprador e  em quantos
      anos ele vai pagar. 
      A prestação mensal não pode exceder
      30% do salário ou então 
      o empréstimo será negado.

''')
print('='*30)

casa = float(input('Valor da casa? R$'))
salario = float(input('Salario mensal? R$'))
anos = int(input('Quantos anos de financiamento? '))
parcela = casa / (anos * 12)
min = salario * 30 / 100

print(f'''Para pagar uma casa no valor de R${casa:.2f} em {anos} anos,
a prestação será de R${parcela:.2f}.''')

if parcela <= min:
    print('Empréstimo pode ser \33[1;32mCONCEDIDO\33[m.')
else:
    print('Emprestimo \33[1;31mNEGADO\33[m.')