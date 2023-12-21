import random
from unittest import case

def title():
    print('==================================================')
    print('========Bem vindo ao jogo da Advinhação===========')
    print('==================================================')

def selectDificult():
    dificult = int(input('Selecione a sua dificuldade: (1) hard, (2) medium, (3) easy, (4) babykid  '))

    match dificult:
        case 1:
            secretNumber = random.randrange(1,200)
            print('Você escolheu a dificuldade difícil')
        case 2:
            secretNumber = random.randrange(1, 150)
            print('Você escolheu a dificuldade média')
        case 3:
            secretNumber = random.randrange(1, 100)
            print('Você escolheu a dificuldade fácil')
        case 4: 
            secretNumber = random.randrange(1 ,50)
            print('Bebe da mamãe')
    
    return secretNumber


title()
selectDificult()


def verificationAcert():
    list = []
    
    








    

    

