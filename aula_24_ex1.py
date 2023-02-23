"""Calculadora com While"""

#startswith - começa com
#endswith   - termina com

while True:
    sair = input('Quer sair? [s]im: ').lower().startswith('s' or 'S')
    print(sair)

    if sair is True:
        ...
