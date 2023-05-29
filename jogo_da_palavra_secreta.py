"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.

- Você vai propor uma palavra secreta qualquer e vai dar possivilidade para o usuário digitar apenas uma letra.

- Quando o usuário digitar a letra, você vai conferir se a letra digitada está na palavra secreta
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta, exiba *.

Faça a contagem de tentativas para o usuário
"""

"""

contador = 0
palavra_secreta = 'Circo'
case = ''
print('Esse é o jogo da Palavra Secreta')
print()

while contador < len(palavra_secreta):
    contador += 1

    testativa = print(f'Tentativa N° {contador}')
    quest = input('Digite uma letra: ').upper().lower() 
    
    if quest in palavra_secreta:
        print(quest)
    else:
        print('*')
    
"""

palavra_secreta = 'perfume'
letras_acertadas = ''
contador = 0

while True:
    contador += 1
    print(f'Tentativa N° {contador}')
    letra_digitada = input('Digite uma letra: ')
    
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
        
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta 
        else:
            palavra_formada += '*'
            
    print(f'Palavra formada: {palavra_formada}')
 
    if palavra_formada == palavra_secreta:
        print('EBAA Temos um Sherlok Homes aqui!!') 
        print(f'A palavra era {palavra_secreta}')  
    
    