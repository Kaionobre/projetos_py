"""Calculadora com While"""

#startswith - começa com
#endswith   - termina com
"""
while True:
    sair = input('Quer sair? [s]im: ').lower().startswith('s' or 'S')
    print(sair)

    if sair is True:
        break
"""

while True:
    numero_1 = input('Digite um número: ') 
    numero_2 = input('Digite outro número: ') 
    operador = input('Digite o operador (+-/*): ') 
    
    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print('Um ou ambos os números digitados não são válidos')
        continue
    
    operadores_permitidos = '+-*/'
    
    if operador not in operadores_permitidos:
        print('Operador inválidos')
        continue
        
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue  
    
    print('Realizando sua conta. Confira o resultado abaixo:')
    
    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    elif operador == '/':
        print(num_1_float / num_2_float)
    elif operador == '*':
        print(num_1_float * num_2_float)
    else:
        print('Nunca deveria chegar aqui')
    
    sair = input('Quer sair? [S]im: ').lower().startswith('s')
    
    if sair is True:
        break