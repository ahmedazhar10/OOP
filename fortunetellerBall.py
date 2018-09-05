import sys
import random
from tkinter import *




#window = Tk()
#window.title("Know Your Fortune")
#canvas = Canvas(window, width=500, height=500)
#canvas.pack()

#thisLabel = Label(top, text="Hey there")
#thisLabel.pack() #finds first available spot and adds it there
#window.mainloop() #keeps window open
#img = PhotoImage(file='C:\\Users\\hp\\Pictures\\crystal_ball.jpg')
#canvas.create_image(0, 0, anchor=NW, image=img)


ans = True

while ans:

    question = input("Go on my child ask me something nice. ")

    answers = random.randint(1,8)

    if question == "":
       sys.exit()

    elif answers == 1:
        print ("It is certain")

    elif answers == 2:
        print ("Outlook good")

    elif answers == 3:
        print ("You may rely on it")

    elif answers == 4:
        print("Go ahead")

    elif answers == 5:
        print("Haha goodluck with that")

    elif answers == 6:
        print("Yeah I think that too")

    elif answers == 7:
        print("Stop! Dont do it.")

    elif answers == 8:
        print("I don't agree with you on that one.")






