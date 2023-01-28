primeiro_valor = int(input('Digite um valor '))
segundo_valor = int(input('Digite outro valor '))


if primeiro_valor > segundo_valor:
    print (f'O valor {primeiro_valor} é maior do que o valor {segundo_valor}')
elif primeiro_valor == segundo_valor:
    print(f'O valor {primeiro_valor} é igual ao {segundo_valor}')
else:
    print(f'O valor {primeiro_valor} é menor do que o {segundo_valor}')
