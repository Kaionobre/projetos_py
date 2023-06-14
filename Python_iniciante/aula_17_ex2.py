"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# Abaixo o que eu fiz

hora = float(input('Que horas são? '))

if hora >= 0 and hora <= 11:
    print('Bom dia')
if hora >= 12 and hora <= 17:
    print('Boa tarde')
if hora >= 18 and hora <= 23:
    print('Boa noite')

# Abaixo o que o professor fez

"""
 entrada = input('Digite a hora em números inteiros: ')

 try:
     hora = int(entrada)

     if hora >= 0 and hora <= 11:
         print('Bom dia')
     elif hora >= 12 and hora <= 17:
         print('Bom tarde')
     elif hora >= 18 and hora <= 23:
         print('Bom noite')
     else:
         print('Não conheço essa hora')
 except:
     print('Por favor, digite apenas números inteiros')

"""