print('='*30)
print('Exercicio - 40')
print('''
Crie um programa que leia duas notas
de um aluno e calcule sua média, 
mostrando uma mensagem no final, 
de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
      ''')
print('='*30)

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
med = (n1 + n2) / 2

print(f'Com as notas {n1} e {n2} a média foi {med:.1f}.') 
if med >= 5  and med < 7:
    print('O aluno esta em \33[1;33mRECUPERAÇÃO\33[m.')
elif med < 5:
    print('O aluno esta \33[1;31mREPROVADO\33[m.')
elif med >= 7:
    print('O aluno esta \33[1;32mAPROVADO\33[m.')