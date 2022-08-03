import random

def pileFace():
    PF=["pile","face"]
    inputUser=eval(input("pile ou face ? met 0 pour pile ou 1 pour face: ")) #demande à user pile ou face
    result=random.randint(0,1) #choisi entre pile ou face
    print("le résultat est", PF[result])
    if inputUser==result:
        print("gagné !!")
    else :
        print("perdu, bouuuuh")
continueGame=0
while continueGame==0:
    pileFace()
    continueGame=eval(input("voulez vous rejouer ? 1=Non, Oui=0 :"))

