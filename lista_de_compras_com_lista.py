"""
Faça uma lista de compras com listas
o usuário deve ter possibilidade de inserir,
apagar e listar valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista
"""

# 1 - Iniciar uma compra
# 2 - Adicionar itens de uma lista, ex: 1 - tomate, 2 - sereja
# 3 - Após cada item adicionado pergintar se o usuário deseja Sair ou continuar
# 4 - Fazer a soma dos produtos com base em seu valor

lista_obj_produtos = ['Macarrão', 'Feijão', 'Arroz', 'Batata']
lista_preco_produtos = [1.5, 2.0, 2.5, 3.5]
produtos_adc = 0

while True:
    entrada = input('Iniciar uma compra? [S]im ou [N]ao: ')
    if entrada == 'n'.upper().lower():
        break
    if entrada == 's'.upper().lower():
        entrada_produtos = int(input(
            'Adicione produtos em seu carrinho de compras.\n' 
              'Macarrão - R$ 1.50\n'
              'Feijão   - R$ 2.00\n'
              'Arroz    - R$ 2.50\n'
              'Batata   - R$ 3.50\n'
              'Adicionar: '))
        if entrada_produtos == 'Macarrão'.startswith('M').upper().lower():
            produtos_adc += 1.5
        elif entrada_produtos == 'Feijão'.startswith('F').upper().lower():
            produtos_adc += 2.0
        elif entrada_produtos == 'Arroz'.startswith('A').upper().lower():
            produtos_adc += 2.5
        elif entrada_produtos == 'Batata'.startswith('B').upper().lower():
            produtos_adc += 3.5
        else:
            print('12')
        
        finalizar_compras = input('Deseja finalizar o carrinho? [S]im ou [N]ao: ')
        if finalizar_compras == 'n'.upper().lower():
            entrada = 's'

            
        
        
        
        
        