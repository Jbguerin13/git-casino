import random

def rouletteNombre (betUser,money): #boucle pour répétition si user sort de l'intervalle [1,36]   
    choiceUser=eval(input("Sur quel numéro voulez-vous poser votre jeton de 1 à 36 :"))
    while choiceUser <1 or choiceUser >36: 
        choiceUser=eval(input("Sur quel numéro voulez-vous poser votre jeton de 1 à 36 :"))
    result=random.randrange(0,36)
    print("La bille est tombée sur le", result)
    if result==0:
        print("la bille est tombée sur le 0, vous avez perdu")
        return money
    if choiceUser==result:
            betUser=betUser*36
            money=money+betUser
            print("vous avez gagné",betUser,"€")
            return money
    else:
            print("vous avez perdu", betUser, "€")
            return money

def rouletteStart(): #demande la mise
    print("faites vos jeux !")
    betUser=eval(input("Entrer la mise en € : "))
    return betUser

def roulettePair(betUser,money): #jeu pair/impair
    PI=["Pair","impair"]
    choiceUser=eval(input("Précisez votre choix : Pair=0, Impair=1 : "))
    result=random.randrange(0,36)
    print("la bille est tombée sur le :",result)
    if result==0:
        print("la bille est tombée sur le 0, vous avez perdu")
        return money
    result=result%2
    print("Le résultat est",PI[result])
    if result==choiceUser:
        betUser=betUser*2
        money=money+betUser
        print("vous avez gagné", betUser,"€")
        return money
    else:
        print("Vous avez perdu", betUser,"€")
        return money

def rouletteCouleur(betUser,money): #Jeu couleur
    couleur=["vert","rouge","noir","rouge","noir","rouge","noir","rouge","noir","rouge","noir","noir","rouge","noir","rouge","noir","rouge","noir","rouge","rouge","noir","rouge","noir","rouge","noir","rouge","noir","rouge","noir","noir","rouge","noir","rouge","noir","rouge","noir","rouge"]
    choiceUser=input("Précisez votre choix rouge ou noir ? : ")
    result=random.randrange(0,36)
    print("La bille est tombée sur", result,"de couleur",couleur[result])
    if result==0:
        print("la bille est tombée sur le 0, vous avez perdu")
        return money
    if couleur[result]==choiceUser:
        betUser=betUser*2
        money=money+betUser
        print("vous avez gagné",betUser,"€")
        return money
    else:
        print("Vous avez perdu", betUser,"€")
        return money

def roulette(betUser,money): 
    choiceGame=eval(input("Sur quels jeux voulez-vous placer votre mise ? Couleur=0 Pair/Impair=1 Nombres=2 :"))
    if choiceGame==0:
        return rouletteCouleur(betUser,money)
    elif choiceGame==1:
        return roulettePair(betUser,money)
    elif choiceGame==2:
        return rouletteNombre(betUser,money)


#lancement du code
nameUser=input("Bienvenue dans les casinos en lignes de JBG !! Entrez votre prénom/nom : ") 
print("Nous espérons que le sort vous soit favorable", nameUser, ";)")
money=eval(input("Combiens désirez vous mettre dans votre bourse en € : "))
print("c'est parti !!")
replay=0
while replay==0:
    betUser=rouletteStart()
    money=money-betUser
    money=roulette(betUser,money)
    print("Il vous reste", money," € dans votre bourse")
    if money<=0:
        replay=1
        print("Vous n'avez plus de sous dans votre bourse :(, revenez au début du mois prochain ;)")
    else:
        replay=eval(input("Souhaitez-vous rejouer ? oui=0 non=1 :"))





