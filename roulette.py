import random
import numpy

#Beginner code of the casino game Roulette in french Version. Code review by PhG

def roulette_number (bet_user, money): #loop to repeat if the user get out from [1,36] 
    choices_user = int(input("Sur quel numéro voulez-vous poser votre jeton de 1 à 36 :"))#security tips : never use "eval" again
    while choices_user <1 or choices_user >36: 
        choices_user = int(input("Sur quel numéro voulez-vous poser votre jeton de 1 à 36 :"))
    result = random.randrange(0, 36)
    print("La bille est tombée sur le", result)
    if result==0 :
        print("la bille est tombée sur le 0, vous avez perdu")
        return money
    if choices_user == result :
            bet_user = bet_user * 36
            money = money + bet_user
            print(f"vous avez gagné {bet_user} €") #tips : print(f"blabla {fct} blabla")
            return money
    else:
            print(f"vous avez perdu {bet_user} €")
            return money

def ask_bet_amount(): #ask the bet
    print("faites vos jeux !")
    bet_user = int(input("Entrer la mise en € : "))
    return bet_user

def roulette_peer_odd(bet_user, money): #game peer/odd
    PI = ["Pair","impair"]
    choices_user = int(input("Précisez votre choix : Pair=0, Impair=1 : "))
    result = random.randrange(0,36)
    print(f"la bille est tombée sur le :{result}")
    if result == 0:
        print("la bille est tombée sur le 0, vous avez perdu")
        return money
    result = result % 2
    print(f"Le résultat est {PI[result]}")
    if result == choices_user :
        bet_user = bet_user * 2
        money = money + bet_user
        print(f"vous avez gagné {bet_user} €")
        return money
    else:
        print(f"Vous avez perdu {bet_user} €")
        return money

def roulette_color(bet_user, money) : #game color
    choices_user = input("Précisez votre choix rouge ou noir ? : ")
    result = numpy.random.choice(["vert", "rouge", "noir"], p = [1/37, 18/37, 18/37]) #using numpy to simplify
    print(f"La bille est tombée sur {result}")
    if result == 0 :
        print("la bille est tombée sur le 0, vous avez perdu")
        return money
    if result == choices_user:
        bet_user = bet_user * 2
        money = money + bet_user
        print(f"vous avez gagné {bet_user} €")
        return money
    else:
        print(f"Vous avez perdu {bet_user} €")
        return money

def roulette(bet_user, money) :
    ROULETTE_CHOICES = { #Using dictionnary to avoid "if forest"
    0 : roulette_color,
    1 : roulette_peer_odd,
    2 : roulette_number,
    }
    choice_game = int(input("Sur quels jeux voulez-vous placer votre mise ? Couleur=0 Pair/Impair=1 Nombres=2 :"))
    return ROULETTE_CHOICES[choice_game](bet_user,money)



#lancement du code
nameUser = input("Bienvenue dans les casinos en lignes de JBG !! Entrez votre prénom/nom : ") 
print("Nous espérons que le sort vous soit favorable", nameUser, ";)")
money = eval(input("Combiens désirez vous mettre dans votre bourse en € : "))
print("c'est parti !!")
replay = 0
while replay == 0:
    bet_user = ask_bet_amount()
    money = money - bet_user
    money = roulette(bet_user,money)
    print(f"Il vous reste {money} € dans votre bourse")
    if money <= 0 :
        replay = 1
        print("Vous n'avez plus de sous dans votre bourse :(, revenez au début du mois prochain ;)")
    else:
        replay = int(input("Souhaitez-vous rejouer ? oui=0 non=1 :"))





