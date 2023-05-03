#beecrowd
"""
#1059

numero = 0

while numero < 100:  
    numero = numero + 2
    print(numero)
"""
    
"""
#1064

contador = 0
positivo = 0
media = 0

while contador < 6:
    entrada = float(input())
    if entrada >= 0:
        media = entrada + media
        positivo += 1
    contador += 1

media_final = media / positivo

print(f'{positivo} valores positivos')
print(f'{media_final}') 

"""

"""
#1067

x = int(input())
qtd = 1
    
while qtd <= x:
    if qtd % 2 == 1:
        print(qtd)
    qtd = qtd + 1
        
""" 





"""
#1072

n = int(input())
qtd = 0
variante_in = 0
variante_out = 0

while qtd < n:
    m = int(input())
    qtd += 1
    
    
    if m >= 10 and m <= 20:
        variante_in = variante_in + 1      
    else:
        variante_out = variante_out + 1    
        
print(f'{variante_in} in')
print(f'{variante_out} out')  

"""

"""
#1115
    
while True:
    x, y = input().split()
    x = int(x)
    y = int(y)
    
    if x == 0 or y == 0:
        break    
    elif x > 0 and y > 0:
        print('primeiro')
    elif x < 0 and y > 0:
        print('segundo')
    elif x < 0 and y < 0:
        print('terceiro')
    elif x > 0 and y < 0:
        print('quarto')
"""
"""
# 1080 



qtd = 0
maior = 0
linha = 0
    
while qtd <= 100:  
    valor = int(input())
    if valor >= maior:
        maior = valor
        linha = linha + 1
    qtd += 1

print(maior)
print(linha)


"""


"""
#

i = 1
j = 60
print(f'I={i} J={j}')

while j > 0:
    i += 3
    j -= 5
    print(f'I={i} J={j}')
    
"""







