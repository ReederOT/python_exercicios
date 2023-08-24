print('=================================')
print('Exercicio - 08')
print('\nCrie um programa que leia um valor em metros,\n e mostre na tela a suas converções em km, hm, dam, dm, cm, mm')
print('=================================\n')

m1 = float(input('Digite um valor em metros: '))

km = m1/1000
hm = m1/100
dam = m1/10
dm = m1*10
cm = m1*100
mm = m1*1000

print(f'A medida de {m1}m, corresponde a:')
print(f'{km}km')
print(f'{hm}hm')
print(f'{dam}dam')
print(f'{dm:.0f}dm')
print(f'{cm:.0f}cm')
print(f'{mm:.0f}mm')

