##############
### Room 2 ###
##############

from src.rooms import room1
from src.core import wait
from src.core import ending

def room2_text():
    print("""
You make your way up a flight of stairs to the various offices of the building. They're very modern in design, 
surrounded by glass panels to allow light in from both inside and outside. Most of them are locked, however
you notice the glass door to one of the workspaces has been left open. Inside you notice a layout of desks, chairs,
and outlets. Whiteboards adorn the walls alongside motivational posters. A few potted plants are scattered about
to give some character to a rather mundane area. 

Some of the desks have laptops left out, documents are strewn across one desk and a photocopier has been left on. There's
even a bonsai tree on someone's desk. It's seems the cleaners didn't bother tidying this office, or maybe it's
been deliberately tampered with.

On one of the whiteboards, written in green is a message:

One becomes two, or three or even four
Ask what you want, I can even give you more
I’m precise and exact in just what I do
Unless you forget to refill me, that’s all on you
""")

def bonsai():
    print("""
Oh all the things to find in this office, a bonsai tree seems strange. Almost as if it was deliberately left out.
You approach it, expecting it to lead you to a clue. 

On closer inspection, you realise it's not actually a tree. It's made of metal and painted to look exactly like a 
bonsai tree. As you pick it up, a light comes on from the leaves and you hear a hiss as green gas begins to 
escape out of the tree. 

You reach for your respirator but it's too late, you were too close and it's in your eyes and lungs. You hear the
faint sound of laughter approaching as your cough and splutter, falling to the ground. The last thing you see before
losing consciousness is a green figure standing above you.

GAME OVER""")
    ending.start_again()

def photocopier():
    print("""
You walk towards the photocopier that's been left on. It emits a faint glow in the dark of the office, almost
like a beacon. As you get closer you notice that a sheet of paper has been left on top of it with the words 
'COPY ME' written in green on it. You shrug and decide to scan it. What could be the harm?

The photocopier whirrs and lights up as you scan the document. Out of the other end comes the copy, only it
unexpectedly has a large letter D on it.

You throw both pieces of paper in the nearby bin and continue your investigation.
""")
    room2_choice()

def laptop():
    print("""
You walk over to the laptops that have been left out. After being turned on, you're greeted with the company's 
sign in page which prompts you for a password you don't know. Running some of your own hacking software from a
usb stick on your utility belt opens bypasses the login but you're greeted with a standard Windows layout. The
software doesn't pick up anything unusual either.

You go back to your investigation, having found nothing of interest.
""")
    room2_choice()

def documents():
    print("""
You go to the desk with documents strewn about it. The documents seem to be various reports on sales trends and
marketing strategies the company is using. A few of the documents contain lines and lines of riddles. As you study
the riddles, you find the answer to all of them is 'bat'.

You roll your eyes and continue your investigation. 
""")
    room2_choice()


def room2_choice():
    print("""
    What do you do?

    1 Investigate the bonsai
    2 Investigate the photocopier
    3 Investigate the laptops
    4 Investigate the documents
    5 Go back to the entrance
    """)
    choice = input(">> ").lower()

    if choice == "1":
        bonsai()
    elif choice == "2":
        photocopier()
    elif choice == "3":
        laptop()
    elif choice == "4":
        documents()
    elif choice == "5":
        wait.go_back()
    else:
        print("Please pick a valid option")

def room2():
    room2_text()
    room2_choice()