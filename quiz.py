# Our quiz!

def quiz():
    Correct = 0
    Wrong = 0
    import time
    print("Guten Tag")
    time.sleep(1)
    Q1 = input("Do you like The Walking Dead? ")
    
    if Q1 == "yes":
          print("Nice You Know What Good Television Is")
          Correct = Correct + 1
    else:
          print("You Disgust Me")
          Wrong = Wrong + 1
    time.sleep(1)
    Q2= input("Has Carl Been Shot In The Eye? ")
    if Q2 == "yes":
          print("Well done, you actually have watched The Walkind Dead")
          Correct = Correct + 1
    else:
          print("You haven't watched it. I depise you!")
          Wrong = Wrong + 1
    time.sleep(1)
    Q3 = input("What Is The Tiger In The Walking Dead Called? ")
    if Q3 == "Shiva":
          print("Wow, That One Even Baffled Me And You Got It Right")
          Correct = Correct + 1
    else:
          print("No God Damn It!")
          Wrong = Wrong + 1
    time.sleep(1)
    Q4 = input("Is Eugene Dead? ")
    if Q4 == "no":
          print("You Are Doing Well")
          Correct = Correct + 1
    else:
          print("ARE YOU SERIOUS!")
          Wrong = Wrong + 1
    time.sleep(1)
    Q5 = input("How Many People Did Neegan Kill? ")
    if Q5 == "2":
          print("You Know Your Walking Dead Information")
          Correct = Correct + 1
    else:
          print("That Is Just Completely Incorect")
          Wrong = Wrong + 1
    time.sleep(1)
    Q6 = input("How Many Series Does The Walking Dead Have? ")
    if Q6 == "7":
          print("Of Course There Are Currently 7 Seasons")
          Correct = Correct + 1
    else:
          print("7 thats it and yet you still got it wrong")
          Wrong = Wrong + 1
    time.sleep(1)
    Q7 = input("Does Rick Have A Daughter? ")
    if Q7 == "yes":
          print("Yep Judith")
          Correct = Correct + 1
    else:
          print("JUDITH!!!!!!!!!! How Do You Not Kow This?")
          Wrong = Wrong + 1
    time.sleep(1)
    Q8 = input("What Is Neegan's Group Called? ")
    if Q8 == "The Saviours":
          print("Yes But They Are All Horrible People")
          Correct = Correct + 1
    else:
          print("YOU SERIOUS? It's The Saviours")
          Wrong = Wrong + 1
    time.sleep(1)
    Q9 = input("What Is The Place Where Rick And The Rest Live Called? ")
    if Q9 == "Alexandria":
          print("Yes But Unfortunately Neegan And The Saviours Might Overthrow It")
          Correct = Correct + 1
    else:
          print("No, Just No.")
          Wrong = Wrong + 1            
    time.sleep(1)
    
    Q10 = input("Is There A Pregnant Character? ")
    if Q10.lower() == "yes":
          print("Yep but unfortunately the father, SPOILER ALERT, Glen is dead")
          Correct = Correct + 1
    else:
          print("Maggie Is Pregnant Come ON!")
          Wrong = Wrong + 1                 
                           
                     
                     
                     
               





# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    quiz()
