import tkinter as tk

def click(event):
    print("Bazinga!")

window = tk.Tk()
window.geometry("500x500")

aLabel = tk.Label(text="This works!")
aLabel.grid(column=0, row=0)

bLable = tk.Label(text="Spoon")
bLable.grid(column=1,row=0)

abutton = tk.Button(window, text="Hit it")
abutton.grid(column=0, row=1)

bButton = tk.Button(window, text="Bazinga")
bButton.grid(column=1,row=1)

#window.bind("<Button-1>", click) 
bButton.bind("<Button-1>", click)

window.mainloop()