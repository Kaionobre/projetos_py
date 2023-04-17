'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''

"""

nome_usuario = input('Digite seu nome de usuário: ')
senha = input('Digite sua senha: ')

while nome_usuario == senha:
    print('FatalError')
    nome_usuario = input('Digite novamente seu nome de usuário: ')
    senha = input('Digite novamente sua senha: ')
else:
    print('Login aceito')
    
"""


'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
Use a função len(string) para saber o tamanho de um texto (número de caracteres).
'''

"""nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
salario = float(input('Digite o seu salário: '))
sexo = input('Digite seu sexo => [f] [m]: ')
estado_civil = input('Digite seu estado civil [s]olteiro, [c]asado, [v]iuvo, [d]ivorciado: ')


while len(nome) < 3:
    print('Seu nome é inválido, repita todo o processo de novo!! ')
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    salario = float(input('Digite o seu salário: '))
    sexo = input('Digite seu sexo => [f] [m]: ')
    estado_civil = input('Digite seu estado civil [s]olteiro, [c]asado, [v]iuvo, [d]ivorciado: ')
while idade < 0 or idade > 150:
    print('Sua idade é inválida, repita todo o processo de novo!! ')
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    salario = float(input('Digite o seu salário: '))
    sexo = input('Digite seu sexo => [f] [m]: ')
    estado_civil = input('Digite seu estado civil [s]olteiro, [c]asado, [v]iuvo, [d]ivorciado: ')
while salario <= 0:
    print('Você provavelmente passa fome, repita todo o processo de novo!! ')
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    salario = float(input('Digite o seu salário: '))
    sexo = input('Digite seu sexo => [f] [m]: ')
    estado_civil = input('Digite seu estado civil [s]olteiro, [c]asado, [v]iuvo, [d]ivorciado: ')
while sexo != 'f' and sexo != 'm':
    print('Você só pode ser xx ou xy, repita o processo de novo!! ')
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    salario = float(input('Digite o seu salário: '))
    sexo = input('Digite seu sexo => [f] [m]: ')
    estado_civil = input('Digite seu estado civil [s]olteiro, [c]asado, [v]iuvo, [d]ivorciado: ')
while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v'  and estado_civil != 'd':
    print('Você selecionou um estado civil inválido, repita o processo de novo!! ')
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    salario = float(input('Digite o seu salário: '))
    sexo = input('Digite seu sexo => [f] [m]: ')
    estado_civil = input('Digite seu estado civil [s]olteiro, [c]asado, [v]iuvo, [d]ivorciado: ')
"""
             
'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
'''
