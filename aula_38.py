# Desempacotamento em chamadas
# De métodos e funções

str = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'Bichado'

a, b, c, *_ = lista

print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
print(*lista)
print(*str)
print(*tupla)
