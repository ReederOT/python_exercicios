print('='*30)
print('Exercicio 53')
print(''' Crie um programa que leia
       uma frase qualquer e diga se 
      ela é um palíndromo, 
      desconsiderando os espaços.
         ''')
print('='*30)

frase = str(input('Digite uma frase: ')).strip().upper()
palvras = frase.split()
juntar = ''.join(palvras)
inverso = ''

for letra in range(len(juntar) - 1, -1, -1 ):
    inverso += juntar[letra]
print(f'O inverso de {juntar} é {inverso}.')
if inverso == juntar:
    print('Temos um palindromo')
else:
    print('Não é um palindromo')