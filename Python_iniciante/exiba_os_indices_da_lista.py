"""
Exercício

Exiba os indices da lista
"""

lista = ['Kaio', 'Eliana', 'Ricardo', 'Ricardinho']
lista.append('Pandora')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))