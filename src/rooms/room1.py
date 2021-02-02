##############
### Room 1 ###
##############

from src.core import wait 
from src.rooms import room2
from src.rooms import room3
from src.rooms import room4
from src.rooms import room5
from src.core import ending

been_here = False

def guess_pass():
    pass_attempt = 0
    while pass_attempt < 3:
        pass_input = input("\nPlease enter the passcode:\n").upper()
        if pass_input == "DOOM":
            ending.ending()
        else:
            pass_attempt += 1
            if pass_attempt < 3:
                print("\nWrong password, try again")
            else:
                wait.wait()            
    print("\nDEATH")
    quit()

def elevator_choice():
    print("\nThe elevator has a small keypad attached to it.")
    choice = input("""
1 - Attempt the password
2 - Return to the entrance
    """)    
    if choice == "1":
        guess_pass()
    elif choice == "2":        
        wait.wait()
        wait.go_back()
    else:
        print("Please pick a valid option")
        elevator_choice()          

def intro_text():
    print("""
There's been a rumour circulating amongst Gotham's crime gangs of a new computer super-virus that has emerged
with the ability to bypass the strongest security algorithms. In the wrong hands it could be used to access government
data, military systems, or even the Justice League technology. It wasn't long before the various super-criminals
of Gotham were on the hunt. 

After months of investigation and interrogation, Batman managed to track the new virus to none other than LexCorp
- Lex Luthor's subsidiary company. Unfortunately, there was on other person who beat him to it - The Riddler.

Time is crucial, you will no doubt have to play the Riddler's game before you can get to him and, hopefully,
the virus.
 """)
    wait.wait()
    
def room1_flavour():
    if been_here == False:
        print("""
You stand outside the LexCorp building, ominous and dark. No lights are on except for the bright neon
'LexCorp' on the outside of the building, marking it among the concrete jungle of Gotham. The workers have gone
home for the night, blissfully asleep and unaware of what's going on inside. 

Despite it being abandoned, the automatic doors open for you. You know for sure now that the Riddler is here -  
inviting you to play his game. 
You walk into the entrance. Attached to the reception desk there's a small note with a giant green question marks
on it. You turn it over to find a message:

"I'm in the high-security research facilities in the basement, but you guessed that already didn't you?
I'm afraid it won't be that easy to get in however. You'll want to hurry up too, there's something else down
here that you will want to see."

There's a sign above you with directions to the different parts
of the building. 
        """)
        wait.wait()
    else:
        print("\nYou're back in the main entrance.")

def room1_choice(): 
    choice = input("""
Where do you want to go?:
    
1 - The Office
2 - The Cafeteria
3 - The Server room
4 - The Gym
5 - The elevator
>> """)

    if choice == "1":
        room2.room2()
    elif choice == "2":
        room3.room3()
    elif choice == "3":
        room5.room5()
    elif choice == "4":
        room4.room4()
    elif choice == "5":
        elevator_choice()
    else:
        print("Please pick a valid option")
        room1_choice()
            
def room1():       
    room1_flavour()
    room1_choice()

    