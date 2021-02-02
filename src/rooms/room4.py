##############
### Room 4 ###
##############

from src.rooms import room1
from src.core import wait
from src.core import ending

def treadmill():
    print("""
As you approach the row of treadmills, you notice one of them is on. There is nothing is remarkable about the
screen but you know nothing is that simple with the Riddler. 

You start up the treadmill and start a jog. You gradually increase the speed, running faster and faster until
you're hitting 20km/h. A message pops up on the screen.

"C'mon Bat-brains, you can do better than that!"

You push up the speed further, breaking out a sweat as you hit 23km/h, then 25, then 28, then 30. Eventually you hit 35km/h
- your lungs are burning, your muscles are about to give out. A message pops up on the screen.

"Nice workout?"

The screen then flashes with a single letter - D

You slow down and get off the treadmill, taking a moment to catch your breath.
""")
    room4_choice()

def weights():
    print("""
You walk over to the pile of weights, neatly stacked. You pick them up one by one in the hopes for clues
but you find nothing significant.
""")
    room4_choice()

def mirrors():
    print("""
You walk over to the mirrors in the corner of the room. 

There is nothing remarkable about them. You check to see if there is anything behind them but they are firmly
attached to the wall.
""")
    room4_choice()

def clock():
    print("""
You decide to take the clock off the wall in the hopes you might find a clue hidden inside. 

At a closer glance you notice that it's emanating a ticking noise yet the hands don't move. You pry open the back
to get a closer look at its inner workings. Inside you find an odd contraption with a giant green question mark
on it.

It's a bomb.

KABOOM

GAME OVER
""")
    ending.start_again()
 

def room4_text():    
    print("""
You make your way to the company gym.

The light flickers on and you're met with various cardio and weightlifting equipment as well as the lingering
smell of sweat and disinfectant in the air. To one side of the room are rows of treadmills, in front of which 
hangs a large clock on the wall. A pile of barbells is stacked in a corner of the room next to mats and walls
adorned with mirrors.

On the far wall you see a message written in green paint.

"I run a dozen times faster than him,
He runs all day,
twice around the gym.
What am I?"
""")  
    wait.wait()
    
def room4_choice():
    print("""
What do you do?:

1 Investigate the treadmills
2 Investigate the weights
3 Investigate the clock attached to the far wall
4 Investigate the mirrors
5 Go back to the entrance
""")
    choice = input(">> ").lower()

    if choice == "1":
        treadmill()
    elif choice == "2":
        weights()
    elif choice == "3":
        clock()
    elif choice == "4":
        mirrors()
    elif choice == "5":
        wait.go_back()
    else:
        print("Not a valid option")
        room4()

def room4():
    room4_text()
    room4_choice()




