"""
Faça uma lista de compras com listas
o usuário deve ter possibilidade de inserir,
apagar e listar valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista
"""
# Abaixo o código que fiz
"""
# 1 - Iniciar uma compra
# 2 - Adicionar itens de uma lista, ex: 1 - tomate, 2 - sereja
# 3 - Após cada item adicionado pergintar se o usuário deseja Sair ou continuar
# 4 - Fazer a soma dos produtos com base em seu valor

produtos = ['Macarrão', 'Feijão', 'Arroz', 'Batata']
lista_preco_produtos = [1.5, 2.0, 2.5, 3.5]
lista_cliente = []
produtos_adc = 0
iniciar_compra = True
prod = ''

while iniciar_compra:
    entrada = input('Iniciar uma compra? [S]im ou [N]ao: ')
    if entrada == 'n'.upper().lower():
        iniciar_compra = False
    elif entrada == 's'.upper().lower():
        while True:
            entrada_produtos = input(
                'Adicione produtos em seu carrinho de compras.\n' 
                '[1] Macarrão - R$ 1.50\n'
                '[2] Feijão   - R$ 2.00\n'
                '[3] Arroz    - R$ 2.50\n'
                '[4] Batata   - R$ 3.50\n'
                'Selecione: ')
            quantidade = int(input('Quantidade: '))

            if entrada_produtos == '1':
                produtos_adc += 1.5 * quantidade
            elif entrada_produtos == '2':
                produtos_adc += 2.0 * quantidade
            elif entrada_produtos == '3':
                produtos_adc += 2.5 * quantidade
            elif entrada_produtos == '4':
                produtos_adc += 3.5 * quantidade
            else:
                print('Você só pode digitar números')
                continue
            
            finalizar_compras = input('Deseja finalizar o carrinho? [S]im ou [N]ao: ')
            if finalizar_compras == 's'.upper().lower():

                print(f'O valor final deu R${produtos_adc:.2f}')
                iniciar_compra = False
                break
        if finalizar_compras == 'n'.upper().lower():
            entrada = 's'

    else:
        print('Opção inválida. Digite "s" para iniciar a compra ou "n" para sair.')

"""            

# Abaixo o código que o professor fez

"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')
                
        
        
    
        