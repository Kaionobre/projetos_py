i = 1
j = 7
jota = 7
i_rep = 1

# criar uma variavel em que toda vez que o j < 5 o J = + 2  ==> 7 + 2 = 9 ////

while i <= 9:
    while j > 4:
        i_rep += 1
        if j == 11:
            j = jota
            j = j + 8
        print(f'I={i} J={j}')
        
        if i_rep > 3 and i % 2 == 1:
            i += 2
            i_rep = 1
            
        if i > 9:
            break
        
        if j > 4:
            j = j - 1
            

        if j < 5:
            j = jota
            j = j + 2
            jota = j    

               