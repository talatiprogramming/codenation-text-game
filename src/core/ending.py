from src.core import wait
from src.core import intro
def start_again():
    choice = input("""
Do you wish to start again or quit?:

1 Quit
2 Start over

""")
    if choice == "1":
        quit()
    elif choice == "2":
        pass
    else:
        print("Please enter a valid option")
        start_again()

def pre_ending_text():
    print("""
The elevator takes you down way deeper than you expected. Typical of Luthor to leave his secret 
research facilities in plain sight.

As the elevator finally reaches its destination and the doors open, you're greeted with a research facility
filled with mech suits, computers, Bane's venom, alien tech and lots of other gadgets you imagine is only a
small fraction of Luthor's collection. In the centre of the room a group of panic-striken there's a circle of
office workers bound and gagged. A ticking bomb is tied to one of them. 

Standing over them you can see Riddler in his signature green suit laughing, waving a usb stick at you
with one hand and holding a boom tube in the other. Boom tubes are alien tech used by the denizens of 
Apokalips to travel across vast difference via extra-dimensional portals.

"Oh quite the conundrum eh Batman? Come for me and you'll be sending these innocent souls to their dooms.
Save them and who knows what I'll do with the software? Maybe I'll crash the stock market. Maybe I'll
blackmail congressmen. Maybe I'll pass on Justice League data to the Legion of Doom. I look forward to
watching your decision."

He begins to cackle loudly as he charges up the boom tube and creates a portal.
""")

def ending1():
    print("""
You lunge for Riddler, tackling him as you both tumble and fight while travelling through dimensions.
The boom tube takes you back onto the streets of Gotham where a bruised and bloodied Riddler lies beneath
you, smiling up at you with cracked teeth. You arrest him without any resistance and take him back to
Arkham, the shadow of guilt hanging over you. 
""")
    wait.wait()
    print("""
Word gets out about what happened that night. How Batman put justice above the lives of the innocent.
Batman finds himself under the scorn of the Justice League and resigns membership a few months later.
The papers, controlled by the biggest gangs of Gotham, use the opportunity to relentless tarnish
Batman and turn public against him.

The isolation, guilt and anger drives Batman to become even more relentless against crime. Even more
viscious. After taking down another group of Joker's goons on the streets, Batman stands among the 
broken, unconcsious bodies around him. He notices a gun on the group that one of the criminals dropped
during the chaos. He leans down and picks it up. 

A large grin stretches across his face as he begins to laugh uncontrollably.
""")
    start_again()

def ending2():
    print("""
You rush towards the hostages and watch as the Riddler escapes through a portal. You cut the rope tying them
together and shout for them to run to the elevator, leaving the bomb behind to destroy whatever nefarious
plans Lex Luthor had running here. The hostages escape the building in time as you disappear into the night,
doubt lingering at the back of your mind as to whether you did the right thing. You begin the hunt for the Riddler
again.
""")
    wait.wait()
    print("""
Soon after the incident Batman found Riddler again but it was too late. He was dead. His body lay in a random
alley of Gotham.
Word had gotten out about the code and what it could do. Forces superior to the Riddler got a hold of it and quickly
put it to work. All of the Justice League's enemies found untold power as they had leverage over the world's
governments and quickly put themselves to work attacking the League. Humanity's heroes found themselves split up
and taken out one by one, their new-found weaknesses exploited and secrets used against them. 

Eventually the world fell under the shadow of the rulership of the Legion of Doom. The world was split up into
territories controlled by Braniac, Darkseid, Ocean Master, Lex Luthor and the Joker. Humanity would suffer
under tyranny, with no one left to protect them.

Batman hides among the streets of Gotham, one of the few survivors of the League, building a resistance in 
the hopes to overthrow the new global regime.
""")
    start_again()


def ending_choice():
    choice = input("""
What do you do?:

1 Chase after Riddler through the portal
2 Let Riddler escape and defuse the bomb
""")

    if choice == "1":
        ending1()
    elif choice == "2":
        ending2()
    else:
        print("Please pick a valid choice")
        ending_choice()

def ending():
    pre_ending_text()
    ending_choice()


