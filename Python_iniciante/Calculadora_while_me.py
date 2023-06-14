start = input('Esta é a sua calculadora, vamos começar? [s]im ou [n]ao? ').upper().lower()

while start == 'n':
    break
while start == 's':
    entrada_1 = int(input('Digite o primeiro número: '))
    entrada_1 = float(entrada_1)

    entrada_2 = int(input('Digite o segundo número: '))
    entrada_2 = float(entrada_2)

    caracteres_aceitos = ['+', '-' , '*', '/']
    entrada_3 = input('Agora digite a operação desejada.  [+] [-] [*] [/] ')
    
    if entrada_3 == '+':
        soma = entrada_1 + entrada_2
        print(f'O resultado de {entrada_1} + {entrada_2} é igual a {soma}')
    elif entrada_3 == '-':
        soma = entrada_1 - entrada_2
        print(f'O resultado de {entrada_1} - {entrada_2} é igual a {soma}')
    elif entrada_3 == '*':
        soma = entrada_1 * entrada_2
        print(f'O resultado de {entrada_1} * {entrada_2} é igual a {soma}')
    elif entrada_3 == '/':
        soma = entrada_1 / entrada_2
        print(f'O resultado de {entrada_1} / {entrada_2} é igual a {soma}')

    final = input('Deseja continuar? [s]im ou [n]ao ').upper().lower()

    if final == 's':
        start = 's'
    else:
        break




    
    




























