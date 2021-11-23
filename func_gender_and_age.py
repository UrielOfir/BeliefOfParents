from tkinter import *
from idlelib.tooltip import Hovertip

import func_a_parent
import func_reminder


def gender_and_age(self):
    gender_window = Toplevel()
    gender_window.grab_set()
    gender_window.geometry("333x245")
    gender_window.resizable(False, False)
    gender_window.title("Some technical details:")
    Label(gender_window, text="Do you have a girl or a boy?", font=('Helvetica bold', 14), padx=50, pady=13,
          background="#34A2FE", borderwidth=5).grid(row=0, column=0, columnspan=2)

    def sel():
        if str(v.get()) != "chil":
            self.the_gender = str(v.get())
            self.get_gender = True

            if self.get_age is True and self.get_gender is True:
                Button(gender_window, text="I finished", background="#34A2FE", font=('Helvetica bold', 11), padx=35,
                       pady=1, command=fin).grid(row=5, column=0, columnspan=2)
                self.finish = True

    def age(x):
        self.level = a.get()
        self.get_age = True
        self.finish = True
        if self.get_age is True and self.get_gender is True:
            self.finish = True
            Button(gender_window, text="I finished", background="#34A2FE", font=('Helvetica bold', 11),
                   padx=35, pady=1, command=fin).grid(row=5, column=0, columnspan=2)

    def fin():

        gender_f(self)
        if self.finish is True:
            gender_window.destroy()
            if self.status == "reminder":
                func_reminder.reminder(self)
                #self.reminder()
            elif self.status == "a parent":
                func_a_parent.a_parent(self)
                #func_a_parent.a_parent(self)

    v = gender_window.var = StringVar()
    v.set("chil")
    Radiobutton(gender_window, text="Girl", font=('Helvetica bold', 11), variable=v,
                value="girl", command=sel).grid(row=1, column=0)
    Radiobutton(gender_window, text="Boy", font=('Helvetica bold', 11), variable=v, value="boy",
                command=sel).grid(row=1, column=1)
    Radiobutton(gender_window, text="I am not sure about my child's gender",
                font=('Helvetica bold', 11), variable=v, value="child", command=sel).grid(row=2,
                                                                                          column=0,
                                                                                          columnspan=2)
    Label(gender_window, text="What is your kid's age?", font=('Helvetica bold', 14),
          padx=50, pady=13, background="#34A2FE", borderwidth=7).grid(row=3, column=0,
                                                                      columnspan=2, sticky="we")
    a = gender_window.var = IntVar()
    a.set(0)
    option_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    OptionMenu(gender_window, a, *option_tuple, command=age).grid(row=4, column=0, columnspan=2)
    Button(gender_window, text="I finished", state=DISABLED, background="#34A2FE",
           font=('Helvetica bold', 11), padx=35, pady=1, command=fin).grid(row=5, column=0, columnspan=2)


def gender_f(self):
    if str(self.the_gender) == "boy":
        self.gender = "he"
        self.gender_first = "He"
        self.belong = "his"
        self.to_ = "him"
    elif str(self.the_gender) == "girl":
        self.gender = "she"
        self.gender_first = "She"
        self.belong = self.to_ = "her"
    elif self.level < 3:
        self.gender = "my baby"
        self.gender_first = "My baby"
    else:
        self.gender = "my child"
        self.gender_y = "your child"
        self.gender_first = "My child"

