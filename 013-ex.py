print('='*30)
print('Exercicio - 13')
print('\nCrie um programa que leia o salário\nde um funcionario, e mostre seu novo salário,\ncom aumento de 15%.')
print('='*30)

s1 = float(input('Qual o salários do funcionario? R$'))
s2 = s1+(s1*15/100)
print(f'O Funcionário que ganhava R${s1:.2f},\ncom o aumento de 15%\npassa a receber R${s2:.2f}.\n')
print('='*30)