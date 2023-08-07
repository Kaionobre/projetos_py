"""
Introdução ao (def) em Python.

São trechos de códigos usados para 
replicar determinada ação ao longo
do seu código. 

Elas podem receber valores para pa-
râmetros (argumentos) e retornar um
valor específico.

Por padão, funções retornam None(nada)
"""

# def Print(a, b, c):
#     print('Várias1')
#     print('Várias2')
#     print('Várias3')
#     print('Várias4')

# def imprimir(a, b, c):
#     print(a, b, c)


# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')


saudacao('Luiz Otávio')
saudacao('Maria')
saudacao('Helena')
saudacao()
