print('='*30)
print('Exercicio - 22')
print('''
Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
      ''')
print('='*30)

nome = str(input('Insira seu nome completo: ')).strip()

print(f'Seu nome em maiusculo é {nome.upper()}.')
print(f'Seu nome em minusculo é {nome.lower()}.')
print(f'Seu nome tem {len(nome.replace(" ", ""))} letras ao todo.')
print(f'Seu primeiro nome tem {nome.find(" ")} letras.')