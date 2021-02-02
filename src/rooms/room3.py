##############
### Room 3 ###
##############

from src.rooms import room1
from src.core import wait
from src.core import ending

def room3_text():
    print("""
You make your way to the building's cafeteria - a large hall filled with circlular tables and plastic chairs
stacked on one end of the room. In the back there are the kitchens and serving areas, next to long lines of fridges
which have been locked up. With the hall being empty, you approach the serving area. Behind the serving station 
there's a work top with a coffee machine, a tub of coffee grounds, a sink and menu board. At the back of the 
serving station there's a line of fridges and cupboards which you assume contain things like milk and serving 
utensils. At one end of the serving station there's a cash register which has a bowl of fruit and a packet of 
cigarettes next to it that have been left out.

You notice the menu board above you contain a message instead of the usual menus you would expect. It reads:

I blacken your breath,
I spoil your grin,
I hunt in a pack,
And kill from within.
""")

def coffee_machine():
    print("""
You take a closer look at the coffee machine. There's not that seems to be out of the ordinary about it. It's a
high quality brand and a similar one that Wayne Enterprises uses in their offices. A look inside the tub
reveals that it contains nothing more than coffee grounds. 

You try turning on the coffee machine, at which point the screen lights up green with the word 'GOTCHA'. The
machine explodes and you're sent hurtiling through glass into the middle of the hall. In the distance you see 
the blurry shape of a green figure clapping as you slip into unconsciousness.

GAME OVER
""")
    ending.start_again()

def fruit_bowl():
    print("""
The fruit bowl contains a selection of browning apples, bananas and pears. Employees hear must not enjoy the 
healthy option it seems. You find nothing out of the ordinary as you inspect the bowl and it's contents.

You continue with your investigation
""")
    room2_choice()

def cigarettes():
    print("""
You approach the cash register and pick up the pack of cigarettes. It must have been left out by one of the kitchen
staff. 

You open it up and dump the contents into your hand, only to find it doesn't contain cigarettes but instead a folded
note. Opening up the note reveals a giant green 'O' painted onto it. Finding nothing else, you discard the note
and continue with your investigation.
""")
    room2_choice()

def fridges():
    print("""
You kneel down behind the serving station and open up the fridges and cupboards. The fridges are filled with
various kinds of milk, juice and soda. The cupboards contain plates, utensils and boxes filled with sachets
of sugar, salt and pepper.

There's nothing here that stands out to you. You get up and continue your investgation.
""")
    room2_choice()



def room3_choice():
    print("""
    What do you do?
    1 Investigate the coffee machine
    2 Investigate the fruit bowl
    3 Investigate the cigarettes
    4 Investigate the fridges
    5 Go back to the entrance
    """)
    choice = input(">> ").lower()

    if choice == "1":
        coffee_machine()
    elif choice == "2":
        fruit_bowl()
    elif choice == "3":
        cigarettes()
    elif choice == "4":
        fridges()
    elif choice == "5":
        wait.go_back()
    else:
        print("Please pick a valid option")

def room3():
    room3_text()
    room3_choice()