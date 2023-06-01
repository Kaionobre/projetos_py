
lista_obj_produtos = ['Macarrão', 'Feijão', 'Arroz', 'Batata']
lista_preco_produtos = [1.5, 2.0, 2.5, 3.5]
produtos_adc = 0
iniciar_compra = True


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
            quantidade = int(input(f'Quantidade: '))

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
            elif finalizar_compras == 'n'.upper().lower():
                break
    else:
        print('Opção inválida. Digite "s" para iniciar a compra ou "n" para sair.')