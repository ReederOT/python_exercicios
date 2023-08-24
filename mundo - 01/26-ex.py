print('='*30)
print('Exercicio - 26')
print('''
Faça um programa que leia uma frase pelo 
teclado e mostre quantas vezes aparece a letra "A",
em que posição ela aparece a primeira vez e em que
posição ela aparece a última vez.
      ''')
print('='*30)

frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}.'.format(frase.rfind('A')+1))