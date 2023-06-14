"""
enumerate - enumerate iteráveis (índices)
"""

lista = ['Kaio', 'Maira', 'joão']
lista.append('Roger')

lista_enumerada = list(enumerate(lista, start= 8))
print(lista_enumerada)

#for indice, nome in enumerate(lista):
#    print(indice, nome)

#for item in enumerate(lista):
#    indice, nome = item 
#    print(indice, nome)

#for tupla_enumeratede in enumerate(lista):
#    for valor in tupla_enumeratede:
#        print(valor)
    
    
    