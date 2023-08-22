print('=================================')
print('Exercicio - 04')
print('Crie um programa que leia\n algo pelo teclado e mostre na tela\n o seu tipo primitivo e todas as informações\n possiveis sobre ela.')
print('=================================')

a = input('Digite algo aqui: ')

print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços?', a.isspace())
print('É apenas número? ', a.isnumeric())
print('É alfabetico? ', a.isalpha())
print('É alfanumerico? ', a.isalnum())
print('Esta em maiusculo? ', a.isupper())
print('Esta em minusculo', a.islower())
print('Esta capitalizado? ', a.istitle())









