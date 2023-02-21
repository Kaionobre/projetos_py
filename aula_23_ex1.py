"""
Iterando strings com while
"""

"""
Basicamente eu teria que criar uma estrutura de repetição usando o whiler e em cara iteração na string do nome teria que se colocar um caractere especial. EX: #$%&*. Abaixo foi a minha tentativa, infelizmente não saí do looping infinito. 
"""

"""
nome = 'Kaio Nóbrega'

tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])

i = nome
while len(nome) <= 12:
    print(i)
    i += '#'
"""



    
"""
Abaixo o que o professor fez
"""

nome = 'Kaio Nóbrega'

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome [indice]
    novo_nome += letra
    indice += 1
    
print(novo_nome)


