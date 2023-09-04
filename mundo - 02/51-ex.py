print('='*30)
print('Exercicio 51')
print(''' Desenvolva um programa que leia
      o primeiro termo e a razão de uma PA. 
      No final, mostre os 10 primeiros termos dessa progressão.
         ''')
print('='*30)

termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
dec = termo + (11-1) * razao

for c in range(termo, dec , razao ):
    print(f'{c}', end=' → ')

print('Acabou')
