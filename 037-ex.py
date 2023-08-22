print('='*30)
print('Exercicio -  37')
print(''' Escreva um programa 
      que leia um número inteiro qualquer
      e peça para o usuario qual será 
      a base de conversão:

      - 1 = Binario
      - 2 = octal
      - 3 = hexadecial
      
    ''')
print('='*30)

n1 = int(input('Insira um número: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] conversão para BINARIO.')
print('[ 2 ] conversão para OCTAL.')
print('[ 3 ] conversão para HEXADECIMAL.')
op = int(input('Sua opção:'))
if op == 1:
    print(f'{n1} convertido em BINÁRIO é {bin(n1)[2:]}')
elif op == 2:
    print(f'{n1} convertido em OCTAL é {oct(n1)[2:]}')
elif op == 3:
    print(f'{n1} convertido em HEXADECIMAL é {hex(n1)[2:]}')
else:
    print('Opção selecionada invalida.')

