import sys
import os
import random
import pickle
import HELP_DOC_MANUAL
import creden



weapon = {'Dragon Sword': 40,'Infinity Sword':100,'Magical spell':50,'Cursed Crossbow':30}


class player:
    def __init__(self, name,role):
        self.name = name
        self.role = role
        self.maxhealth = 100
        self.health = self.maxhealth
        self.base_attack = 10
        # comment continuation from v3
        self.gold = 500
        self.score = self.gold*2.2
        self.pots = 3
        self.weap = ['Phoenix Sword']
        self.curweap = ['Phoenix Sword']
    @property
    def attack(self):
        attack = self.base_attack
        if self.curweap == 'Phoenix Sword':
           attack += 10
        if self.curweap == 'Dragon Sword':
           attack += 25
        if self.curweap == 'Infinity Sword':
           attack += 100
        if self.curweap == 'Magical spell':
            attack += 40
            self.health += 5
        if self.curweap == 'Cursed Crossbow':
            attack += 50
            self.health -= 20
        return attack



# class for the monster / enemny in the game
class goblin:
    def __init__(self, name):
        self .name = name
        self.maxhealth = 50
        self.health = self.maxhealth
        self.attack = 10  # kindly change the value to 5 to minimize the difficulty
        self.goldgain = 10
goblinig = goblin('goblin')


class zombie:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 70
        self.health = self.maxhealth
        self.attack = 10  # kindly change the value to 5 to minimize the difficulty
        self.goldgain = 15
zombieig = zombie('zombie')


class dracula:
    def __init__(self, name):
        self .name = name
        self.maxhealth = 120
        self.health = self.maxhealth
        self.attack = 10  # kindly change the value to 5 to minimize the difficulty
        self.goldgain = 28
draculaig = dracula('dracula')


class blackmagician:
    def __init__(self, name):
        self .name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 10  # kindly change the value to 5 to minimize the difficulty
        self.goldgain = 10000
blackmagicianig = blackmagician('blackmagician')


"""class roles:
       def __init__(self,role):
              self.role = role"""

# main line code
print('Login successful')

#************G A M E P L A Y *********************************

def main():
    os.system('cls||clear')
    print('Welcome to the ARKESIA <WORLD OF THE WARRIORS')
    print('MESSAGE')
    print('PRESS 1 Start')
    print('PRESS 2 Load')
    print('PRESS 3 EXIT')
    print('PRESS 4 HELP AND MANUAL')
    user_input = input('ENTER YOUR CHOICE --> ')
    if user_input == '1':
        start()
    elif user_input == '2':
         if os.path.exists("login.txt") == True:
             with open('savegame.txt','rb') as f:
                  global playerig
                  playerig = pickle.load(f)

             print("loaded save state")
             option = input('')
             start1()
         else:
             print('you have no save file for this ')
             option = input('')
             main()
    elif user_input == '3':
         sys.exit()
    elif user_input == '4':
         HELP_DOC_MANUAL.main()
         uinput = input('press enter to continue')
         main()
    else:
        main()


def start():
    os.system('cls||clear')
    option = creden.username
    avatar = creden.avatar_name
    print('choose your class ')
    print('NINJA')
    print('MAGICIAN')
    print('Warrior')
    roleinput = input('Enter/type the role of the player')
    print(f'Oh son of earth {option} THE <{avatar}> Merlyn welcome you in to the world of warriors')
    global playerig
    playerig = player(option,roleinput)
    #roleig = roles(roleinput)
    start1()


def start1():
    os.system('cls||clear')
    print(f"hello {playerig.name} how are you")
    print(f"Warrior Class of Player is {playerig.role}")
    print(f"your current GAME SCORE is {playerig.score}")
    print('ITEMS AVAILABLE AT THE YOUR BAG')
    print("attack power--> ", playerig.attack)
    print("Gold in the inventory-->", playerig.gold)
    print("Weapons In the Inventory --> ",playerig.weap)
    print("Current weapons -->", playerig.curweap)
    print("potionsc-->", playerig.pots)
    print("health -->", (playerig.health, playerig.maxhealth))
    print("1.)Fight")
    print("2.)Store")
    print("3.)Save")
    print("4.)EXIT ")
    print("5)Inventory")
    print("6) Leadership Board")
    option  = input("Give your choice")
    if option == '1':
        prefight()
    elif option == '2':
        store()
    elif option == '3':
         savegame()
    elif option == '4':
        sys.exit()
    elif option == '5':
         inventory()
    elif option == '6':
         leadershipboard()
         print("\n L E A D E R S H I P  B O A R D")
         printdata()
         takeinput = input('PRESS ENTER TO CONTINUE')
         start1()
    else:
        start1()


def savegame():
    with open('savegame.txt', 'wb') as f:
        pickle.dump(playerig, f)
        print('\ngame has been saved with latest checkpoint\n')
        option = input()
        start1()

def inventory():
    print('What action you want to take ')
    print('1> Press 1 to equip weapon')
    print('2> Press 2 to go back to start')
    option = input('Choose your option from the above ')
    if option == '1':
        equip()
    elif option == '2':
         start1()



def equip():
    print('what you want to equip')
    for weapon in playerig.weap:
        print(weapon)
    print('Press B to go back')
    option = input('')
    if option == playerig.curweap:
        print('you already have that weapon')
        option = input('')
        equip()
    elif option =='b':
         inventory()
    elif option in playerig.weap:
         playerig.curweap = option
         print(f'you are equipped with weapon{option}')
         option = input()
         equip()
    else:
        print(f'you dont have this weapon in the inventory{option}')


def prefight():
    global enemy
    print('PRESS 1 FOR LEVEL 1 <THE GOBLIN CASTLE')
    print('PRESS 2 FOR LEVEL 2 <Zombie Apocalypse')
    print('PRESS 3 FOR LEVEL 3 <Wraith of Dracula')
    print('PRESS 4 FOR LEVEL 4 <FINAL JUDEGEMENT')
    print('Press enter if you want to go back to earth')
    enemynum = input('Please choose your level')
    print('Current world is Level ',enemynum)
    if enemynum == '1':
        print('This Realm creatures called me Goblin <i will steal your soul >')
        enemy = goblinig
        riddle1()
        level1()


    elif enemynum == '2':
        enemy = zombieig
        riddle2()
        level2()
    elif enemynum == '3':
         enemy  = draculaig
         riddle3()
         level3()
    elif enemynum == '4':
         enemy = blackmagicianig
         riddle4()
         level4()
    else :
         print('Afraid of fighting || want to go back to earth')
         print('Merlyn : OK SON OF ADAM YOU ARE TELEPORTED BACK TO EARTH')
         sys.exit()
    fight()


def fight():
    print('in progress')
    print(f"{playerig.name} vs {enemy.name}")
    print(f"current score -----> {playerig.score}")
    print(f"Player name {playerig.name},\nn Health bar {playerig.health},\nmax health -->{playerig.maxhealth},\n opponent --> {enemy.name},"
          f" \n opponent health-->{enemy.health},\n opponent max health-->{enemy.maxhealth}")
    print("potion\n",playerig.pots)
    print('Current Weapon-->', playerig.curweap)
    print("1> Attack")
    print("2> Drink Potion")
    print("3> RUN ")
    print("4 > EXIT ")
    option = input('Enter your choice as per the above option')
    if option == "1":
        attack()
    elif option == "2":
         drinkpot()
    elif option == "3":
         run()
    elif option == "4":
         sys.exit()
    else:
        fight()




def attack():
    os.system('cls||clear')
    pattack = random.sample(playerig.attack / 2,playerig.attack)
    eattack = random.sample(enemy.attack/2,enemy.attack)
    if pattack == playerig.attack/2:
        print('you miss')
    else:
        enemy.health -= pattack
        print(f'you did {pattack} damage')
    option = input('enter the value non string')     #modify it to enter
    if enemy.health <= 0:
       win()
    os.system('cls||clear')
    if eattack == enemy.attack/2:
        print('Enemy missed')
    else:
        playerig.health -= eattack
        print('the enemy deals with the damage -->',eattack)
    option = input('')
    if playerig.health <= 0:
       dead()
    else:
        fight()

def attack():
    os.system('cls||clear')
    pattack = random.randint(playerig.attack / 2,playerig.attack)
    eattack = random.randint(enemy.attack/2,enemy.attack)
    if pattack == playerig.attack/2:
        print('you miss')
    else:
        enemy.health -= pattack
        print(f'you did {pattack} damage')
    option = input('enter the value non string')
    if enemy.health <= 0:
       win()
    os.system('cls||clear')
    if eattack == enemy.attack/2:
        print('Enemy missed')
    else:
        playerig.health -= eattack
        print('the enemy deals with the damage -->',eattack)
    option = input('')
    if playerig.health <= 0:
       dead()
    else:
        fight()
#************************************************************************************
def finalfight():
    print('in progress')
    print(f"{playerig.name} vs {enemy.name}")
    print(f"Player name {playerig.name},\nn Health bar {playerig.health},\nmax health -->{playerig.maxhealth},\n opponent --> {enemy.name},"
          f" \n opponent health-->{enemy.health},\n opponent max health-->{enemy.maxhealth}")
    print("potion%i\n",playerig.pots)
    print('Current Weapon-->', playerig.curweap)
    print("1> Final Attack")
    print("2> Drink Potion")
    print("3> RUN ")
    print("4 > EXIT ")
    option = input('Enter your choice as per the above option')
    if option == "1":
        finalattack()
    elif option == "2":
         drinkpot()
    elif option == "3":
         run()
    elif option == "4":
         sys.exit()
    else:
        fight()





def finalattack():
    os.system('cls||clear')
    pattack = random.randint(playerig.attack / 2,playerig.attack)
    eattack = random.randint(enemy.attack/2,enemy.attack)
    if pattack == playerig.attack/2:
        print('you miss')
    else:
        enemy.health -= pattack
        print(f'you did {pattack} damage')
    option = input('enter the value non string')
    if enemy.health <= 0:
       finalwin()
    os.system('cls||clear')
    if eattack == enemy.attack/2:
        print('Enemy missed')
    else:
        playerig.health -= eattack
        print('the enemy deals with the damage -->',eattack)
    option = input('')
    if playerig.health <= 0:
       dead()
    else:
        finalfight()


def finalwin():
    playerig.gold += enemy.goldgain
    #enemy.health = enemy.maxhealth
    playerig.health = playerig.maxhealth
    print('you have defeated the enemy --> ',enemy.name)
    print('you found the gold ',enemy.goldgain)
    print('You have won the the title of " THE GUARDIAN " ')
    print('Credits')
    print('Designer -> Nahush Agrawal')
    print('thankyou for playing this game')
    playerig.score += 100
    leadershipboard()
    printdata()
    sys.exit()

#********************************************************************
def drinkpot():
    os.system('cls||clear')
    if playerig.pots == 0:
        print('you dont have any potions')
        option = input('press 1,2,3')
        fight()
    else:
        playerig.health += 50
        if playerig.health > playerig.maxhealth:
           playerig.health = playerig.maxhealth
        print('you drank a potion powered up')
    option = input('press1,2,3')
    fight()

def run(eattack=None):
    os.system('cls||clear')
    runnum = random.randint (1,3)
    if runnum == 1:
       print('congrats you are successfully run away')
       option = input('game is restarted press 1 to start')
       start1()
    else:
        print('you failed to run away')
        option = input('')
        os.system('cls||clear')
        eattack = random.randint(enemy.attack / 2, enemy.attack)
        if eattack == enemy.attack / 2:
            print('Enemy missed')
        else:
            playerig.healthbar -= eattack
        option = input('')
        if playerig.health <= 0:
            dead()
        else:
            fight()




def win():
    playerig.gold += enemy.goldgain
    #enemy.health = enemy.maxhealth
    playerig.health = playerig.maxhealth
    print('you have defeated the enemy --> ',enemy.name)
    print('you found the gold ',enemy.goldgain)
    playerig.pots +=1
    print('your rewards is --->')
    print('you got the additional health potion')
    option = input('')
    playerig.score += 45
    start1()

def dead():
    print('you are teleported back to earth ')
    option = input('')
    start1()

def store():
    os.system('cls||clear')
    print(' Welcome to the albela shop')
    print('Kindly choose/type the name of the object that you want to purchase from below the list ')
    print(' Dragon Sword : 40 GOLD COIN ')
    print('Dragon sword will make your attacks more effective then before')
    print(' Infinity Sword : 100 GOLD COIN')
    print('Infinity Sword is the most powerful weapon once slice is sufficient to anhilate enemy')
    print('Magical spell : 50 : GOLD COIN')
    print('Magical spell is great chant which will bookst your health after each use and parallely attacks on enemy')
    print('Cursed Crossbow : 30 GOLD COIN')
    print(' Potion for health')
    print('input back for the start game window')
    option = input('')
    if option == 'Potion for health':
       store2()
    if option in weapon:
       if playerig.gold >= weapon[option]:
           os.system('cls||clear')
           playerig.gold -= weapon[option]
           playerig.weap.append(option)
           print(f'you have bought{option} ')
           option = input()
           store()
       else:
           print('you dont have enough gold for the item ')
           option = input('')
           store()
    elif option == 'back':
         start1()
    else:
         os.system('cls||clear')
         print('asked item is not in the list ')
         option = input('')
         store()

def store2():
    os.system('cls||clear')
    print(' Welcome to the potion shop')
    print('input back for the start game window')
    option = input('')
    if playerig.gold >= 40:
           print(f'previous status of GOLD is {playerig.gold} and Available potions is {playerig.pots}')
           os.system('cls||clear')
           playerig.pots += 1
           playerig.gold -= 30
           print(f'you have bought{option} current status of your potions as per inventory is {playerig.pots} ')
           print(f'current status of your gold is {playerig.gold} and current status of potions is {playerig.pots}')
           option = input()
           store()
    else:
           print('you dont have enough gold for the item ')
           option = input('')
           store()

#*********************** levels *****************************

def level1():
    print(f"Welcome to the level 1 {playerig.name} the great {playerig.role}")
    enemy = goblinig
    print(f"your enemy is the {goblinig.name}")
    fight()

def level2():
    print(f"Welcome to the level 2 {playerig.name} the great {playerig.role}")
    print('Group of zombies attacking you || finish them before they bite you ')
    enemy = zombieig
    print(f"your enemy is the {zombieig.name}")
    fight()

def level3():
    print(f"Welcome to the level 3 {playerig.name} the great <{playerig.role}>")
    print('Myself Dracula <King of blood serphants')
    enemy = draculaig
    print(f"your enemy is the {draculaig.name}")
    fight()

def level4():
    print(f"Welcome to the level 4 [FINAL LEVEL] {playerig.name} the great< {playerig.role}>")
    print('Congratulation oh son of saphein')
    print('i am your final opponent . to get the title of "THE GUARDIAN" you have to finish me')
    enemy = blackmagicianig
    print(f"your enemy is the {blackmagicianig.name}")
    finalfight()

#****************** R I D D L E S *************************************

def riddle1():
     print('Yakasa appeared ')
     print(f'Yaksha --> To pass this gate answer my questions ohh son of saphein {playerig.name} the great <{playerig.role} >')
     print('Yakshya --> who is really a helpful companion and always be with you ')
     print('1 -> Steady Intelligence ')
     print('2->   Loyal Friend')
     print('3 ->  No one')
     user_input = input("Enter your preference")
     if user_input == '1':
         print("that'correct son of saphien --> you have passed ")
         level1()
     elif user_input == '2':
         print('Wrong <you are not worthy i am sending you out of this world>')
         start1()
     else:
         print('RETRY')
         riddle1()


def riddle2():
    print('Yakasa appeared ')
    print(f'Yaksha --> To pass this gate answer my questions ohh son of saphein {playerig.name} the great <{playerig.role}> ')
    print('Yakshya --> What makes person a true hero ? ')
    print('1 -> Super Powers')
    print('2->  Acknowledgement of others')
    print('3 -> Will to risk their own life to save other')
    user_input = input("Enter your preference")
    if user_input == '3':
        print("that'correct son of saphien --> you have passed ")
        level2()
    elif user_input == '2':
        print('Wrong <you are not worthy i am sending you back to breakout area >')
        print('Please restart the fight')
        start1()
    else:
        print('RETRY')
        riddle2()


def riddle3():
    print('Yakasa appeared ')
    print(f'Yaksha --> To pass this gate answer my questions ohh son of saphein {playerig.name} the great<{playerig.role}> ')
    print('Yakshya --> What makes person a true Leader ? ')
    print('1 -> Bossy Attitude')
    print('2->  Supremacy over others')
    print('3 -> Sense of responsibility')
    user_input = input("Enter your preference")
    if user_input == '3':
        print("that'correct son of saphien --> you have passed ")
        level1()
    elif user_input == '2':
        print('Wrong <you are not worthy i am sending you back to freeroam area>')
        start1()
    else:
        print('RETRY')
        riddle3()


def riddle4():
    print('Yakasa appeared ')
    print(f'Yaksha --> To pass this gate answer my questions ohh son of saphein<{playerig.name} the great {playerig.role}>')
    print('Yakshya --> When people start enjoy doing their work? ')
    print('1 -> Work for rewards')
    print('2->  Work with good team')
    print('3 -> Work without desires and start enjoying their quest')
    user_input = input("Enter your preference")
    if user_input == '3':
        print("that'correct son of saphien --> you have passed ")
        level4()
    elif user_input == '2':
        print('Wrong <you are not worthy i am sending you back to earth>')
        print('you are teleported please restart the game ')
        sys.exit()
    else:
        riddle4()



#********************** LEADERSHIP BOARD *******************************

def leadershipboard():
    print(f"Player Name ---> {playerig.name}")
    print(f"Player Class -->  {playerig.role}  ")
    print(f"Current Score of player is {playerig.score}")
    file = open("leadershipboard.txt", "a")
    file.write(str(playerig.score))
    file.write('   ')
    file.write(playerig.name)
    file.write('   ')
    file.write("PlayerRole")
    file.write('   ')
    file.write(playerig.role)
    file.write("     ")
    file.write('Your Score is ')
    file.write('   ')
    file.write(str(playerig.score))
    #file.write("\n")
    file.close()
    sorting()

def sorting():
    bands = list()
    file ='leadershipboard.txt'
    with open (file) as fin:
         for line in fin:
             bands.append(line)

    bands.sort(reverse=True)
    #print(bands)
    filename = 'leadershipboard.txt'
    with open(filename, 'w') as fout:
         for band in bands:
             fout.write(band + '\n')



def printdata():
    with open('leadershipboard.txt','r') as f:
         lines = f.readlines()
         for i in lines:
             print(i)
















#*************************************************************************
# ************* main code ******************
#registeration.register()
#registeration.login()

main()



#playerig.name --> name of the player
#roleig.role --> assigned role to player