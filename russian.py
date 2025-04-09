import random

def addrounds ():
    global rounds
    for i in range(0,random.randint(1,4),1):
        rounds.append(1)
        #print(rounds)
        print("İ add a live round.")
    print("-------------------------")
    for i in range(0,random.randint(1,4),1):
        print("İ add a blank round.")
        rounds.append(0)
    print("-------------------------")
    random.shuffle(rounds)
    print("İ shuffle.")
    #print(rounds)

def checkliverounds ():
    global rounds
    x = 0
    for i in rounds:
        if i == 1:
            x += 1
    return (x)

def checkblankrounds ():
    global rounds
    x = 0
    for i in rounds:
        if i == 0:
            x += 1
    return (x)
def dealerturn():
    global rounds
    item_ai()
    print("My turn.")
    print("-------------------------")
    if checkliverounds() <= checkblankrounds():
        print("İ shoot you.")
        shootplayer()
    else:
        print("İ shoot myself")
        dealerblank()
        
def shootplayer():
    global rounds
    global playerlife
    if rounds[0] == 1:
        playerlife -= 1
        print("İt wasnt a blank round.")
    else:
        print("İt was a blank round.")
    rounds.pop(0)
    
def dealerblank():
    global rounds
    global dealerlife
    if rounds[0] == 1:
        dealerlife -= 1
        rounds.pop(0)
        print("ouch")
    else:
        print("İ skip your turn.")
        rounds.pop(0)
        dealerturn()
        
def playerturn():
    global rounds
    global playerlife
    global dealerlife
    while True:
        try:
            x = int(input("0 to 7 to use an item. 8 to shoot me. any other value to shoot yourself."))
        except ValueError:
            continue
        break
    if x == 8:
        if rounds[0] == 1:
            if one_is_cut_two_is_normal == 1:
                dealerlife -= 2
            dealerlife -= 1
            print("ouch")
        else:
            print("İt was a blank round.")
    elif x == 0 or x == 1 or x == 2 or x == 3 or x == 4 or x == 5 or x == 6 or x == 7:
        if items[x] == 1:
            cut_P(x)
        elif items[x] == 2:
            alchohol_P(x)
        elif items[x] == 3:
            investigate_P(x)
        elif items[x] == 4:
            jail_P(x)
        else:
            smoking_P(x)
        playerturn()
        
    else:
        if rounds[0] == 0:
            x = "cheatblank"
            print("You skip my turn.")
        else:
            playerlife -= 1
            if one_is_cut_two_is_normal == 1:
                print("you're dumb.")
                exit()
            print("That's gonna leave a mark.")
        
            
    rounds.pop(0)
    if x == "cheatblank":
        playerturn()
        
def give_items():
    global a
    a = random.randint(1, 4)
    for i in range(0, a, 1):
        items.append(random.randint(1,5))
        print("You have got a")
        if items[i] == 1:
            print("Saw")
        elif items[i] == 2:
            print("Beer")
        elif items[i] == 3:
            print("Spyglass")
        elif items[i] == 4:
            print("Handcuffs")
        else:
            print("Cigarettes")
    print("-------------------------------------")
            
def give_items_dealer():
    global a
    for i in range(0, a, 1):
        dealer_items.append(random.randint(1,5))
        print("Dealer has got a")
        if dealer_items[i] == 1:
            print("Saw")
        elif dealer_items[i] == 2:
            print("Beer")
        elif dealer_items[i] == 3:
            print("Spyglass")
        elif dealer_items[i] == 4:
            print("Handcuffs")
        else:
            print("Cigarettes")
    print("-------------------------------------")

def smoking_P(a):
    global playerlife
    if playerlife != 4:
        playerlife += 1
    items.pop(a)

def jail_P(a):
    global dealer_jail
    dealer_jail = 1
    items.pop(a)

def investigate_P(a):
    if rounds[0] == 1:
        print("Live round.")
    else:
        print("Blank round.")
    items.pop(a)

def alchohol_P(a):
    if rounds[0] == 1:
        print("Live round ejected.")
    else:
        print("Blank round ejected.")
    items.pop(a)
    rounds.pop(0)
    
def cut_P(a):
    global one_is_cut_two_is_normal
    items.pop(a)
    one_is_cut_two_is_normal = 1
    print("The gun has been cut.")
    
def smoking_D():
    global dealerlife
    dealer_items.remove(5)
    dealerlife += 1
    print("The dealer has healed.")

def jail_D():
    dealer_items.remove(4)
    player_jail = 1
    print("You have been handcuffed.")
    
def investigate_D():
    dealer_items.remove(3)
    print("Very interasting...")

def alchohol_D():
    dealer_items.remove(2)
    if rounds[0] == 1:
        print("Live round ejected.")
    else:
        print("Blank round ejected.")
    rounds.pop(0)

def cut_D():
    global one_is_cut_two_is_normal
    dealer_items.remove(1)
    one_is_cut_two_is_normal = 1
    print("The gun has ben cut.")

def item_ai():
    for i in range(0, 8, 1):
        for i in dealer_items:
            if i == 1:
                x = checkblankrounds()
                y = checkliverounds()
                if x <= y:
                    cut_D()
            elif i == 2:
                if 1 in rounds:
                    pass
                else:
                    if len(rounds) != 1:
                        alchohol_D()
            elif i == 3:
                if 1 in rounds and 0 in rounds:
                    investigate_D()
            elif i == 4:
                if player_jail == 0:
                    jail_D()
            else:
                if dealerlife != 4:
                    smoking_D()


if __name__ == '__main__':
    z = int(input("would you like to read a tutorial? presss 0 for no."))
    if z != 0:
        print("Cigarettes heal for 1 hp. Saw makes the next bullet deal twice the damage. Beer ejects and reveals the next bullet. Spyglass reveals next bullet. Handcuffs give you an additional turn, but not consecutively. Shooting yourself with a blank round gives you an additional turn. Live rounds deal 1 damage, 2 if saw was used.")
    playerlife = 4
    dealerlife = 4
    items = []
    dealer_items = []
    while playerlife > 0 and dealerlife > 0:
        player_jail = 0
        dealer_jail = 0
        one_is_cut_two_is_normal = 2
        give_items()
        give_items_dealer()
        rounds = []
        addrounds()
        print(dealerlife, "lives i have left, and you have", playerlife)
        while rounds != []:
            if player_jail == 0:
                playerturn()
            one_is_cut_two_is_normal = 2
            if rounds != [] and dealer_jail == 0:
                dealerturn()
            else:
                dealer_jail = 0
                print("My turn has been skipped.")
    if playerlife != 0:
        print("You won 70,000 dollars.")
    else:
        print("You are dead.")




