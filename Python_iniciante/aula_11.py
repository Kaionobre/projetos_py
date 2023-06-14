"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')       #Ficou 10 caracteres pra direita 
print(f'{variavel: <10}')       #Ficou 10 caracteres pra esquerda
print(f'{variavel: ^10}')       #Ficou no centro com 10 caracteres entre ele
print(f'{variavel:$^10}')       #Preenche com o caractere que desejar
print(f'{1000.45468421:.2f}')   #Coloca o valor decimal desejado, pode ser , ou .

