"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
try:
    numero_inteiro = int(input('Digite um número inteiro '))
    numero_par = numero_inteiro % 2 == 0 

    if numero_par :
        print('Este número é par!')
    else:
        print('Este número é impar')
except:
    print('não é um numero inteiro')

