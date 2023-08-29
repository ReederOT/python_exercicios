print('='*30)
print('Exercicio 50')
print(''' Desenvolva um programa
      que leia seis números inteiros
      e mostre a soma apenas daqueles
      que forem pares. Se o valor digitado for ímpar,
      desconsidere-o.
         ''')
print('='*30)

soma = 0
cont = 0

for c in range(1, 7):
    num = int(input(f'Digite o {c}º numero inteiro: '))

    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
if soma == 0:
    print('Não foram digitados numeros pares.')
else:
    print(f'Foi informado {cont} numeros pares.')
    print(f'A soma dos numeros pares é {soma}.')