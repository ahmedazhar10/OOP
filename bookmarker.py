import tkinter as tk
import webbrowser

def google(event):
    webbrowser.open_new_tab("google.com")

def youtube(event):
    webbrowser.open_new_tab("youtube.com")

window = tk.Tk()

window.geometry("500x500")

aButton = tk.Button(window, text="Google")
aButton.grid(column=0, row=0)

bButton = tk.Button(window, text="Youtube")
bButton.grid(column=1, row=0)

aButton.bind("<Button-1>", google)
bButton.bind("<Button-1>", youtube)

window.mainloop()