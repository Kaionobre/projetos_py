
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito rande". 
"""

# Abaixo o que eu fiz

nome = input('Digite seu nome ')

if len(nome) <= 4:
    print('Seu nome é curto')
    
elif len(nome) >=5 and len(nome) <= 6:
    print('Seu nome é normal')

else:
    print('Seu nome é muito grande')
    
# Abaixo o que o professor fez

"""
nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')
    
"""