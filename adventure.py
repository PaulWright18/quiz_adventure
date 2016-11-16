# An adventure game
from random import randint
from time import sleep
def room1():
    print("Welcome To Soul Searcher")
    sleep(5)
    name = ""
    Health = 100
    XP = 0
    start()
    

def unknown():
        response = ""
        unknown = randint(1, 6)
        if unknown == 1:
            response = "Did I Tell You To Right That?"
        elif unknown == 2:
            response = "Do You Realise That You Can't Do That"
        elif unknown == 3:
            response = "Error 404. Page Not Found"
        elif unknown == 4:
            response = "NO, NO, NO, NO, NO, NO!"
        else:
            response = "You Need To Re-think our Life If That Is Your Answer"
        print(response)
        start()
        

def start():
        print("You have been sent to the land of eternal damnation.")
        sleep(3)
        print("However,")
        sleep(1)
        print("You are lucky because if you find the lost soul of Argon, you will be freed back to wherever you came from")
        sleep(3)
        print("You will be given multiple choice questions and the answers you choose will depend the way the game turns out. So choose wisely")

   








# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    room1()
