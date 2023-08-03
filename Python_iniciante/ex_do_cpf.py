"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""



cont = 10
soma = 0

cpf = [0 ,6 ,8 ,2 ,6 ,4 ,1 ,5 ,4]
cpf_multi = []

for i in cpf:
    cpf_multi.append(i * cont) 
    cont -= 1
print(cpf_multi)
    
for indice in cpf_multi:
    soma += indice
print(f'A soma eh: {soma}')

multi_soma = soma * 10
print(multi_soma)

resto_divisao = multi_soma % 11
print(resto_divisao)

if resto_divisao > 9:
    primeiro_digito = 0
    print(f'Primeiro dígito comecou com {primeiro_digito}')
else:
    primeiro_digito = resto_divisao
    print(f'Primeiro digito comeca com {primeiro_digito}')





