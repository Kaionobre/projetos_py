"""
Introdução ao desmenbramento + tupla (tupla)
"""

nome_1, *_ = ['Kaio', 'Eliana', 'Ricardo', 'Ricardinho']
_, nome_2, *_ = ['Kaio', 'Eliana', 'Ricardo', 'Ricardinho']

print(nome_2, _)
print(nome_1, _)