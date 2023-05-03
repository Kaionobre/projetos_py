"""
I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=9
I=3 J=8
I=3 J=7
I=5 J=11
I=5 J=10
I=5 J=9
I=7 J=13
I=7 J=12
I=7 J=11
I=9 J=15
I=9 J=14
I=9 J=13

"""

i = 1
i_rep = 1
j = 7
j_rep = 1




while i_rep < 5:
    while j_rep < 5:
        i_rep += 1
        j_rep += 1
        
        print(f'I={i} J={j}')
        
        if i_rep > 4:
            i += 2
            i_rep = 1
        if i > 9:
            break
        
    
    