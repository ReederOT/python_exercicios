print('='*30)
print('Exercicio - 34')
print('''
Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
            ''')
print('='*30)
from time import sleep

salario = float(input('Digite o valor do salário:R$'))

if salario <= 1250 :
    nsalario = salario + (salario * (15/100))
else: 
    nsalario = salario + (salario * (10/100))
    
print(f'Quem ganhava o salario \33[0;31mR${salario:.2f}'f'\33[m, com o aumento passa a ganhar \33[0;32mR${nsalario:.2f}\33[m.')
    

