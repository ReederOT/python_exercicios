print('='*30)
print('Exercicio - 42')
print('''
Refaça o DESAFIO 035 dos triângulos,
acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes ''')
print('='*30)

a1 = float(input('Primeiro segmento: '))
a2 = float(input('Segundo segmento: '))
a3 = float(input('Terceiro segmento: '))

if a1 < a2 + a3 and a2 < a1 + a3 and a3 < a1 + a2:
    print('Os segmentos acima, PODEM formar um triangulo.', end=" ")
    if a1 == a2 and a2 == a3:
        print('EQUILATERO\n')
    elif a1 != a2 and a2 != a3 and a1 != a3:
        print('ESCALENO\n')
    else:
        print('ISOCELES')

else:
    print('Os segmentos acima, NÃO PODEM formar um triangulo.')
