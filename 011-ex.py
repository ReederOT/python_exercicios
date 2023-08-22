print('='*30)
print('Exercicio - 11')
print('\nCrie um programa que leia a largura e a altura\nde uma parede em metros, calcule sua area\ne a quantidade de tinta necessaria para pintá-la.\nSabendo que cada litro de tinta pinta uma area de 2m².')
print('='*30)

larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
area = larg*alt
tinta = area/2

print(f'A parede tem a dimensão de {larg}x{alt}\nsua área é de {area}m².')
print(f'Para pintar essa parede será necessario {tinta}L de tinta.\n')
print('='*30)