print('='*30)
print('Exercicio 49')
print('''Refaça o DESAFIO 009, 
      mostrando a tabuada de um 
      número que o usuário escolher,
      só que agora utilizando um laço for..
         ''')
print('='*30)

tab = int(input('Digite um número para ver sua tabuada: '))

print('='*30)
print(f'TABUADA SOLICITADA É A DO {tab}.')
print('='*30)
for c in range(0, 11):
    print(f'{tab} x {c:2} = {tab * c}')

print('='*30)