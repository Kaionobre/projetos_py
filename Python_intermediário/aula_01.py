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

def soma_dois():
    num_1 = int(input('Digite um número: '))
    num_2 = int(input('Digite um outro número: '))
    soma = num_1 + num_2
    print(soma)
    
soma_dois()
