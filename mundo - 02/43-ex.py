print('='*30)
print('Exercicio - 43')
print('''
Desenvolva uma lógica que leia o peso
e a altura de uma pessoa, calcule seu Índice
de Massa Corporal (IMC) e mostre seu status,
de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida ''')
print('='*30)

peso = float(input('Qual seu peso(Kg)? '))
altura = float(input('Qual sua altura(m)? '))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}.')
if imc < 18.5:
    print('Você esta abaixo do peso ideal.')
elif imc >= 18.5 and imc < 25:
    print('Você esta com peso ideal.')
elif imc >= 25 and imc < 30:
    print('Você esta com sobrepeso.')
elif imc >= 30 and imc < 40:
    print('Você esta com obesidade.')
else:
    print('Você esta com obesidade mórbida.')
