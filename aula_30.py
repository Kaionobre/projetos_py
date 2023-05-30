"""
Cuidado com dados mutáveis 
= - copia o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
"""
nome = "Luiz"
noutra_variavel = nome
nome = "Jõao"

print(nome)
print(noutra_variavel)
"""

lista_a = ['Luiz', 'Maria']
lista_b = lista_a.copy()

lista_a[0] = 'Oi eu sou o Goku'
print(lista_a)
print(lista_b)

