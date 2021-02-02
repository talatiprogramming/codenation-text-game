from src.core import intro as i
from src.core import ending as e
from src.rooms import room1 
from src.rooms import room4 

def batman_game():
    while True:
        i.start()
        room1.room1()

batman_game()