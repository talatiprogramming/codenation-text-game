##############
### Room 5 ###
##############

from src.rooms import room1
from src.core import wait
from src.core import ending

def room5_choice():
    print("""
What do you do?

1 Investigate the posters
2 Investigate the fridge
3 Investigate the computer
4 Investigate the door 
5 Go back to the entrance
""")
    choice = input(">> ").lower()

    if choice == "1":
        posters()
    elif choice == "2":
        fridge()
    elif choice == "3":
        computer()
    elif choice == "4":
        door()
    elif choice == "5":
        wait.go_back()
    else:
        print("Not a valid option")
        room5()

def posters():
    print("""
You look to the posters next to the note. They depict art from Justice Brawl 2 and the Arkham Asylum game. 
You smirk - video game depictions of superheroes are always far from the truth and greatly exagerrated. 

There's nothing remarkable about them. You continue your investigation.
""")
    room5_choice()

def fridge():
    print("""
You walk over to the fridge. It contains various types of soda, energy drinks and few beers. Lex Luthor knows how
to treat his staff, that's for sure. Most likely to keep them sweet so they don't question the more sinister aspects
of his research.

You pull out the drinks and give the fridge a look-over but find nothing out of the ordinary.
""")
    room5_choice()

def computer():
    print("""
You walk over to the computer. You notice there's some program running, prompting you to enter a password. The keyboard
is, oddly, a light green colour.

You type the word 'enigma' into the text box.

A large M appears on the screen and the computer switches itself off.
""")
    room5_choice()

def door():
    print("""
You approach the mysterious door and turn the handle. To your surprise, it's not locked. You pull it open and you're
greeted with a large axe attached to a trip mechanism that swings downwards hitting you square in the chest.

You fly across the room and tumble onto the floor. You feel yourself fading as the blood drains from your body. A blurry
green figure stands over your body.

"C'mon Bat-brains, that was an obvious trap wasn't it?"

Everything goes dark and you lose consciousness to the sound of laughter.

GAME OVER
""")
    ending.start_again()

    
def room5_text():
    print("""
You make your way through various corridors, following signs, until you reach a vast room with rows and rows of 
computers. Adorned with glass panels to protect them, they whirr away, lights flickering, storing and processing many 
thousands of terabytes worth of data. A small EMP here could put Lex Luthor out of business for a long period of time
but he's not your focus right now. You wouldn't want to tread on Kal-el's toes anyway.

You on the other side of the room, past the labyrinth of servers, is a small office for the server engineers. You
make your way inside. 

It's a small room lined with desks, swivel chairs and computers - one of which has been left on, it's screen leaving a 
faint glow in the dark. On one wall a few video game posters, notes and a calendar adorn a tack board. You also notice 
a fridge stacked with energy drinks and beer at the far end of the room, and next to it, a mysterious door with a giant
green question mark painted on it.

You notice there's a large note attached to the tack board with a message.

"I have keys that open no locks, 
with space but no room, 
and I allow you to enter but not go in.
What am I?"
""")

def room5():
    room5_text()
    room5_choice()
    


