nome = 'Saulo Pereira'
altura = 1.75
peso = 76
imc = peso / altura ** 2

linha1 = f'{nome} tem {altura}m de altura,'
linha2 = f'pesa {peso} quilos e seu IMC é {imc:.2f}'

print(nome + ' tem ' + str(altura) + 'm de altura,')
print('pesa ' + str(peso) + ' quilos e seu IMC é '+ str(imc))
print()

print(nome, 'tem', altura, 'de altura,')
print('pesa', peso, 'quilos e seu IMC é', imc)
print()

print(linha1)
print(linha2)