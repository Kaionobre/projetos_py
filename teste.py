tipo_1 = input()
tipo_2 = input()
tipo_3 = input()

if tipo_1 == 'vertebrado':
    if tipo_2 == 'ave':
        if tipo_3 == 'carnivoro':
            print('aguia')
        elif tipo_3 == 'onivoro':
            print('pomba')
            
    elif tipo_2 == 'mamifero': 
        if tipo_3 == 'onivoro':
            print('homem')
        elif tipo_3 == 'herbivoro':
            print('vaca')
            
elif tipo_1 == 'invertebrado':
    if tipo_2 == 'inseto':
        if tipo_3 == 'hematofago':
            print('pulga')
        elif tipo_3 == 'herbiro':
            print('lagarta')
            
    elif tipo_2 == 'anelideo':
        if tipo_3 == 'hematofago':
            print('sanguessuga')
        elif tipo_3 == 'onivoro':
            print('minhoca')
                





