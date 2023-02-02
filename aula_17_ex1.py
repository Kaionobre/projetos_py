"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# Abaixo o que eu fiz

try:
    numero_inteiro = int(input('Digite um número inteiro '))
    numero_par = numero_inteiro % 2 == 0 

    if numero_par :
        print('Este número é par!')
    else:
        print('Este número é impar')
except:
    print('não é um numero inteiro')

# Abaixo o que o professor fez

""" 
entrada = input('Digite um número: ')

 if entrada.isdigit():
     entrada_int = int(entrada)
     par_impar = entrada_int % 2 == 0
     par_impar_texto = 'ímpar'

     if par_impar:
         par_impar_texto = 'par'

     print(f'O número {entrada_int} é {par_impar_texto}')
 else:
     print('Você não digitou um número inteiro')

 try:
     entrada_int = float(entrada)
     par_impar = entrada_int % 2 == 0
     par_impar_texto = 'ímpar'

     if par_impar:
         par_impar_texto = 'par'

     print(f'O número {entrada_int} é {par_impar_texto}')
 except:
     print('Você não digitou um número inteiro')
     
"""
