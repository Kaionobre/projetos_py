"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

number_1 = 0.1
number_2 = 0.7
number_3 = number_1 + number_2

print(number_3)
print(f'{number_3:.2f}')
print(round(number_3, 2))

