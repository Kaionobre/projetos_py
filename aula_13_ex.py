nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
nome_invertido = nome[::-1]
nome_caractere = len(nome)
primeira_letra_nome = nome[0]
ultima_letra_nome = nome[-1]


if len(nome or idade) == 0:
    print('Você não digitou nada!!')
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome_invertido}')
    if ' ' in nome:
            print(f'O seu nome possui espaço ')
    else:
        print('O seu nome não possui espaço ')
        
    print(f'O seu nome tem {nome_caractere} caracteres')
    print(f'A primeira letra do seu nome é: {primeira_letra_nome}')
    print(f'A ultima letra do seu nome é: {ultima_letra_nome}')




    








"""
 0123456789
 kaio nobrega
-87654321
"""