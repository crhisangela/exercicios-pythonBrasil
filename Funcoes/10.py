'''10. Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.'''

from random import randint
k = 0

def craps():
    k = randint(1,12)
    if k == 7 or k == 11:
        print('Você é o mestre!! Ganhou!!', k)
    elif k == 2 or k == 3 or k == 12:
        print('Craps!!! Você perdeu!', k)
    elif k in range(4,6) or k in range(8,10):
        print('Esse é o seu numero vamos jogar!! Numero:', k)
        print('Digite D para jogar o dado: ')
        z = 0
        while k != z:
            print('Digite D para jogar o dado:')
            s = input()
            if s == 'D' or s == 'd':
                z = randint(2,13)
                print('Seu numero foi: ', z)
                if z == 7:
                    print('Voce Perdeu!!!')
                    break
        if  z != 7:
            print('Voce Ganhou!!!')
craps()