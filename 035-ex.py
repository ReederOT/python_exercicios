print('='*30)
print('Exercicio - 35')
print('='*30)
print('Analizando se as retas podem formar um triangulo')
a1 = float(input('Primeiro segmento: '))
a2 = float(input('Segundo segmento: '))
a3 = float(input('Terceiro segmento: '))

if a1 < a2 + a3 and a2 < a1 + a3 and a3 < a1 + a2 :
    print('Estes segmentos \33[0;34mPODEM\33[m formar um triangulo.')

else:
    print('Estes segmentos \33[0;31mNÃO PODEM\33[m formar um triangulo.')