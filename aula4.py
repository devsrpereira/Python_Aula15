primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if primeiro_valor > segundo_valor:
    print(f'primeiro_valor = {primeiro_valor} e ele é maior do que o segundo_valor = {segundo_valor}')
elif primeiro_valor == segundo_valor:
    print(f'primeiro_valor = {primeiro_valor} e ele é igual ao segundo_valor = {segundo_valor}')
else:
    print(f'segundo_valor = {segundo_valor} e ele é maior do que o primeiro_valor = {primeiro_valor}')