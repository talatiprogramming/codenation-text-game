from src.rooms import room1
def wait():
    input("Press ENTER to continue...")

def go_back():
    room1.been_here = True
    room1.room1()