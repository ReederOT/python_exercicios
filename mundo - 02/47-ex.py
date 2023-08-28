print('='*30)
print('Exercicio 47')
print('''Crie um programa 
    que mostre na tela 
    todos os números pares
    que estão no intervalo entre 1 e 50.
         ''')
print('='*30)

for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=" ")
print('Acabou')