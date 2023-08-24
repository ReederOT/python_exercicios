print('='*30)
print('Exercicio - 29')
print('''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
que ele foi multado. A multa vai custar R$7,00 por cada 
Km acima do limite.
      ''')
print('='*30)

radar = float(input('Digite a velocidade do carro: '))
multa = (radar-80)*7
if radar > 80:
 
    print('MULTADO! Você execeu o limite de velocidade que é 80Km/h')
    print(f'Você deve pagar uma multa de R${multa:.2f}!')

print('Tenha um bom dia, dirija com segurança.')