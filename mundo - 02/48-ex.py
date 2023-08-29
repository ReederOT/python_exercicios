print('='*30)
print('Exercicio 48')
print('''Faça um programa que calcul
      a soma entre todos os números que
      são múltiplos de três e que se 
      encontram no intervalo de 1 até 500.
         ''')
print('='*30)

soma = 0 
cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1

print(f'A soma de todos os valores solicitados é {soma}.')
print(f'Foram somados o total de {cont} valores.')
        