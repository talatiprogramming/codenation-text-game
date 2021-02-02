from src.core import wait

title_art = """
Mystery Inc presents:

████████╗██╗  ██╗███████╗    ██████╗ ██╗██████╗ ██████╗ ██╗     ███████╗██████╗ ███████╗     ██████╗  █████╗ ███╗   ███╗███████╗
╚══██╔══╝██║  ██║██╔════╝    ██╔══██╗██║██╔══██╗██╔══██╗██║     ██╔════╝██╔══██╗██╔════╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
   ██║   ███████║█████╗      ██████╔╝██║██║  ██║██║  ██║██║     █████╗  ██████╔╝███████╗    ██║  ███╗███████║██╔████╔██║█████╗  
   ██║   ██╔══██║██╔══╝      ██╔══██╗██║██║  ██║██║  ██║██║     ██╔══╝  ██╔══██╗╚════██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
   ██║   ██║  ██║███████╗    ██║  ██║██║██████╔╝██████╔╝███████╗███████╗██║  ██║███████║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                                                                

                _____________________                             _____________________
                `-._:  .:'   `:::  .:\          |\__/|           /::  .:'   `:::  .:.-'
                   \      :          \          |:   |          /         :       /    
                    \     ::    .     `-_______/ ::   \_______-'   .      ::   ./      
                    |  :   :: ::'  :   :: ::'  :   :: ::'      :: ::'  :   :: :|       
                    |     ;::         ;::         ;::         ;::         ;::  |       
                    |  .:'   `:::  .:'   `:::  .:'   `:::  .:'   `:::  .:'   `:|       
                    /     :           :           :           :           :    \       
                   /______::_____     ::    .     ::    .     ::   _____._::____\      
                                `----._:: ::'  :   :: ::'  _.----'                    
                                        `--.       ;::  .--'                           
                                            `-. .:'  .-'                               
                                                \    /                           
                                                 \  /                                   
                                                  \/ 

"""

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

def start():    
    print(title_art)
    print("Welcome to Batman: Stuck in the Riddle!\n")

    start_game = input('Type "1" to start the game or "2" to quit the game: ')

    if start_game == "1":
        intro_text()                
    elif start_game == "2":
        print("Goodbye")
        quit()
    else:
        print("Try again.")
        start()

