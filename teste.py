t = int(input())
caractere = 0
n = 0
n_lista = [0]

while True:
    while n <= t:  
        print(f'N {n_lista} = {n}')
        n += 1
        caractere += 1
        n_lista.clear()
        n_lista.append(caractere)
        if n == t:
            n = 0


