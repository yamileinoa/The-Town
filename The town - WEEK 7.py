#Program: The Town Game
#Programmer: Yamile Inoa Khouri
#Date: February 27th, 2021
#Version: 6.0

 
import random #will allow me to acces the function in the model

class Contestant:

    def __init__(self,c_health, c_stamina, c_attack, e_witch, e_witch_attack):
        self.__c_health = c_health
        self.__c_stamina = c_stamina
        self.__c_attack = c_attack
        self.__e_witch = e_witch
        self.__e_witch_attack = e_witch_attack

    def set_c_health(self, c_health):
        self.__c_health = c_health

    def set_c_stamina(self, c_stamina):
        self.__c_stamina = c_stamina

    def set_c_attack(self, c_attack):
        self.__c_attack = c_attack 

    def set_e_witch(self, e_witch):
        self.__e_witch = e_witch

    def set_e_witch_attack(self, e_witch_attack):
        self.__e_witch_attack = e_witch_attack

    def get_c_health(self):
        return self.__c_health
 
    def get_c_stamina(self):
        return self.__c_stamina

    def get_c_attack(self):
        return self.__c_attack

    def get_e_witch(self):
        return self.__e_witch
 
    def get_e_witch_attack(self):
        return self.__e_witch_attack
 

#Constants
EQUIP_BLADE = 0
EQUIP_KUNAI = 1
MAX_HEALTH = 2
MAX_STAMINA = 3
WITCH_HEALTH =4
RUN = 5
REST = 6

CONST_TUPLE = (1, 1, 100, 100, 100, 10, 20)
#__________________________________________________________________________________________________________________________________________________

def main():
   
    #Contestant object
    player = Contestant(CONST_TUPLE[MAX_HEALTH], CONST_TUPLE[MAX_STAMINA], 0, CONST_TUPLE[WITCH_HEALTH], 0)

    done = False

    splash_screen()

    while not done:

    #display_commands() was moved to menu choice

        commands_choice = get_commands_choice()

        #Heal
        if (commands_choice == 1):
            player = action_heal(player)
        #Run   
        elif (commands_choice == 2):
           player = run(player)
        #Rest
        elif (commands_choice == 3):
            player = action_rest(player)
        #Attack
        elif (commands_choice == 4):
           player = action_attack(player)
        #Character Status
        elif (commands_choice == 5):
            character_status(player)
        #Save Game
        elif (commands_choice == 6):
            save_game(player)
        #Load Game
        elif (commands_choice == 7):
            player = load_game(player);

        else:
            print()
            print('You selected an invalid command option', end = '\n\n')
        print()
 

    #Check if the game was lost or won

        done = check_won(player)
    return main()

#_____________________________________________________________________________________________________________________

#Splash Screen

def splash_screen():

    print ('_____________________________________________________________________________________', end = '\n\n\n')
    print ('|                                The Town                                           |', end = '\n\n\n')
    print ('|       Will you be able to save the town from the evil witch or die trying?        |', end = '\n\n\n')
    print ('|                           Yamile Inoa Khouri                                      |')
    print ('|                              Version 3.0                                          |')
    print ('-------------------------------------------------------------------------------------')

    c_name = input('What is your Character name? ')
    print (                      'Welcome to The Town', c_name, end = '\n\n\n')
    print ('The Town is awaiting for the chosen one to save them and that is you', c_name, end = '\n\n\n')

#______________________________________________________________________________________________________________________
    #Character Start
    print ('    Your current health is', CONST_TUPLE[MAX_HEALTH], 'and your current stamina is', CONST_TUPLE[MAX_STAMINA])
    print ('    You will be equiped with ', CONST_TUPLE[EQUIP_BLADE], 'blade and', CONST_TUPLE[EQUIP_KUNAI], 'kunai knife')
    print ('You can heal by eating those rice cakes that will be provided at the start of the game')
    print ()
#_____________________________________________________________________________________________________________________   
    #Display Commands
def display_commands():
    print('1 - Heal')#each rice cake heals by 25
    print('2 - Run')#decreases stamina by 10
    print('3 - Rest')#restores stamina and health
    print('4 - Attack')#10 to 15 damage to witch and witch can attack back with a 10 to 15 damage (random number)
    print('5 - Character Status')
    print('6 - Save Game')
    print('7 - Load Game')
    print()
#_____________________________________________________________________________________________________________________

def get_commands_choice():

    good_data = False

    while not good_data:

        display_commands()

        try:
            c_choice = int(input('Which action would you like to proceed with to start your journey? '))
            print()

        except ValueError:
            print('***Value entered must be an integer ****')
            print()

        else:    

            good_data = 1 <= c_choice <=7
            if not good_data:
                print('Invalid command choice, Try again')
                print()

            else:

                good_data = True

    return c_choice

#____________________________________________________________________________________________________________________   

    #Heal
def action_heal(player):
    player.set_c_health(min(player.get_c_health() + get_random_health(), CONST_TUPLE[MAX_HEALTH]))

    if (player.get_c_health() == CONST_TUPLE[MAX_HEALTH]):
        print('Your health is already full')
    else:
        print ('You have healed, continue your adventure!')
    return player

def get_random_health():
    
    return random.randint(10, 20)
#_____________________________________________________________________________________________________________________  
    #Run
def run(player):
    player.set_c_stamina(max(0, player.get_c_stamina() - RUN))
    player.set_c_health(max(0, player.get_c_health() - get_random_attack()))

    print ('You are running, be careful your being attacked')

    return player

def get_random_attack():

    return random.randint(10, 15)
#_____________________________________________________________________________________________________________________       

    #Rest   
def action_rest(player):
    player.set_c_stamina(min(player.get_c_stamina() + REST, CONST_TUPLE[MAX_STAMINA]))
    player.set_e_witch(min(player.get_e_witch() + get_random_health(), CONST_TUPLE[WITCH_HEALTH]))
    if (player.get_c_stamina() == CONST_TUPLE[MAX_STAMINA]):
        print('Your stamina is full')
      
    else:
        print ('You have regained some of your stamina, watch out the evil witch is healing!')

    return player   

#_____________________________________________________________________________________________________________________

    #Attack
def action_attack(player):
    player.set_c_health(max(0, player.get_c_health() - get_random_attack()))
    player.set_e_witch(max(0, player.get_e_witch() - get_random_attack()))
    player.set_c_stamina(max(0, player.get_c_stamina() - get_random_attack()))

    print ('The enemy witch has been attacked, watch out you have been attacked back! ')

    return player

#______________________________________________________________________________________________________________________

    #Character Status
def character_status(player):
     print('\tCheck Status:', end = '\n\n')
     print('\tHealth: ', format (player.get_c_health()))
     print('\tStamina: ', format (player.get_c_stamina()))
     print('\tWitch: ', format (player.get_e_witch()))
     print()

#________________________________________________________________________________________________________________________

    #Check if game has been won or lost
def check_won(player):

    if (player.get_c_health() <= 0):
        print('You have been killed by an enemy, Game Over')
        return True

    elif (player.get_c_stamina() <= 0):
        print ('You ran out of stamina, Game over')
        return True

    elif (player.get_e_witch() <= 0):
        print('You have defeated the evil witch and saved the town, Congratulations ')
        return True

#_______________________________________________________________________________________________________________________

        #Save Game
def save_game(player):

    file_name = input('Please enter the name to save your progress: ')
    try:
        outfile = open(file_name + '.txt', 'w')
    except:
        print('The file could not be opened')

    else:
        outfile.write(str(player.get_c_health())+ '\n')
        outfile.write(str(player.get_c_stamina())+ '\n')             
        outfile.write(str(player.get_c_attack())+ '\n')
        outfile.write(str(player.get_e_witch())+ '\n')
        outfile.write(str(player.get_e_witch_attack())+ '\n')
        outfile.close()

#_________________________________________________________________________________________________________________________                     

        #Load Game
def load_game(player):
    file_name = input('Enter the name of your saved game: ')

    try:
        infile = open(file_name + '.txt.', 'r')
    except:
        print('The saved game could not be opened')
    else:
        player.set_c_health(int(infile.readline()))
        player.set_c_stamina(int(infile.readline()))
        player.set_c_attack(int(infile.readline()))
        player.set_e_witch(int(infile.readline()))
        player.set_e_witch_attack(int(infile.readline()))

        infile.close()

    return player
#_______________________________________________________________________________________________________________________________

        #Returns to main
main()      
