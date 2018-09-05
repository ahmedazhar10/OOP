import datetime
import tkinter as tk
from dateutil.relativedelta import relativedelta

class Person:

    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def __str__(self):
        return "Name: {}, Birthdate: {}".format(self.name, self.birthdate)

    def age(self):
        today = datetime.date.today()
        #return today.year - self.birthdate.year ----Gives me a bug. Result is a year less
        age_calculated = relativedelta(today, self.birthdate)
        return age_calculated.years




#print(ahmed)
#print(ahmed.age())

def age():
    #today = datetime.date.today()
    #print(year_entry.get())
    #converting string to int --- int('str') eg. int('58')
    #birthdate = datetime.date(int(year_entry.get()), int(month_entry.get()), int(day_entry.get()))
    ahmed = Person("Ahmed", datetime.date(int(year_entry.get()),
                                          int(month_entry.get()),
                                          int(day_entry.get())))
    print(ahmed.age())
    # Result Field
    result_field = tk.Text(master=window, height=3, width=50)
    result_field.grid(column=4, row=6)
    answer_text = "Congrats! You have successfully survived {} years of your life. Keep on living :)".format(ahmed.age())
    result_field.insert(tk.END, answer_text)
    #print(birthdate)
    #return rdelta.years



window = tk.Tk()
window.geometry("700x500")
window.title("Age Calculator") #Title of Window

#Lables
year_lable = tk.Label(text="Year")
year_lable.grid(column=0, row=1)

month_lable = tk.Label(text="Month")
month_lable.grid(column=0, row=2)

day_lable = tk.Label(text="Day")
day_lable.grid(column=0, row=3)

#Entry
year_entry = tk.Entry()
year_entry.grid(column=1, row=1)

month_entry = tk.Entry()
month_entry.grid(column=1, row=2)

day_entry = tk.Entry()
day_entry.grid(column=1, row=3)

calcButton = tk.Button(text="Let's see what your age is", command=age)
calcButton.grid(column=4, row=4)




window.mainloop()
