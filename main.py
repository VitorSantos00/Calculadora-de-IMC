altura = float(input('Qual sua altura em metros? '))
peso = float(input('Qual seu peso em kg? '))
imc = peso / (altura ** 2)
print('Seu imc é {:.1f}'.format(imc))
if imc < 18.5:
  print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
  print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
  print('Você está em SOBRE PESO')
elif 30 <= imc < 40:
  print('Você está em OBESIDADE')
elif imc >= 40:
  print('Você está em OBESIDADE MÓRBIDA, cuidado!')