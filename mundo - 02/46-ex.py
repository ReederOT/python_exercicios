print('='*30)
print('Exercicio 46')
print('''Faça um programa que mostre na tela
      uma contagem regressiva o ano novo,
      indo de 10 até 0, 
      com uma pausa de 1 segundo entre eles.
         ''')
print('='*30)

from time import sleep
print('Contagem regressiva para o ano novo')

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('Feliz Ano Novo!!!')