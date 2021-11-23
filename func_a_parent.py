# Import the required libraries
from tkinter import *
from idlelib.tooltip import Hovertip
import webbrowser


def a_parent(self):
    par = Toplevel()
    self.hungry = self.dirty = self.thirst = False
    self.get_dirty = self.get_thirst = self.get_hungry = False
    par.grab_set()
    par.geometry("580x270")
    par.configure(bg="#34A2FE")
    par.resizable(False, False)
    par.title("It all starts in your head")
    text_title = "Here are some questions to better understand your situation.\
    \nIn the following questions, please choose Yes or No:"
    label0 = LabelFrame(par, text=text_title, width=800, height=200, background="#34A2FE", font=("black", 14))
    label0.grid()
    index = 0
    len_of_problem = int(len(self.optionalProblemAndSolution))
    while index < len_of_problem:
        the_problem = self.optionalProblemAndSolution[index]
        problem = "My " + self.only_gander + " is " + the_problem + "?"
        Label(label0, text=problem, pady=7, padx=5, background="#34A2FE", font=("black", 11)).grid(row=index,
                                                                                                   column=0,
                                                                                                   sticky="W")
        index += 1
    # parameter for radioButton
    hun = par.var = StringVar()
    thi = par.var = StringVar()
    ddir = par.var = StringVar()
    hun.set(value="a")
    thi.set(value="a")
    ddir.set(value="a")

    # Setting the conclusion from the user answer
    def ready_conclusion():
        if self.get_thirst is True and self.get_hungry is True and self.get_dirty is True:
            self.ready = True
            if self.hungry is False and self.dirty is False and self.thirst is False:
                text_conclusion = " WOW. " + self.gender_first + " really ready to sleep!!"
                text_finish = "Your are ready to the next level"
            elif self.hungry is True and self.dirty is True and self.thirst is True:
                text_finish = "I took care of my kid\n" + self.gender + " is ready for sleep!"
                text_conclusion = "Hemm, you should check again if " + self.gender_y + " is ready to sleep..."

            else:
                text_finish = "I followed the recommendations, " + self.gender + " is ready for sleep!"
                text_conclusion = "OK. Here is the answer: "
                if self.hungry is True:
                    text_conclusion += "Give " + self.to_ + " to eat"
                    if self.thirst is True:
                        text_conclusion += " and drink"
                    elif self.dirty is True:
                        text_conclusion = "OK, give " + self.to_ + " to eat and clean " + self.to_
                elif self.dirty is True:
                    text_conclusion = "Please clean " + self.to_
                    if self.thirst is True:
                        text_conclusion += " and give " + self.to_ + " to drink"
                elif self.thirst is True:
                    text_conclusion += "give " + self.to_ + " to drink"
            label1.destroy()
            label_con = LabelFrame(label0, text=text_conclusion, width=400, height=100,
                                   font=("black", 13))
            label_con.grid(sticky="ews", row=3, column=0, columnspan=3)
            check_b = Checkbutton(label_con, text=text_finish, command=fin1, font=('Helvetica bold', 9))
            check_b.grid(row=0, sticky="w")
            Button(label_con, text="Press here!", background="#34A2FE", font=('Helvetica bold', 11),
                   padx=20, pady=5, command=fin).grid(padx=55, pady=5, row=1)

    def fin1():
        self.select_check_b = True
        return

    def fin():
        self.status = "from_beginning"
        par.destroy()
        self.reminder()

    def hun1():
        self.get_hungry = True
        if hun.get() == "True":
            self.hungry = True
        ready_conclusion()

    def thi1():
        self.get_thirst = True
        if thi.get() == "True":
            self.thirst = True
        ready_conclusion()

    def ddir1():
        self.get_dirty = True
        if ddir.get() == "True":
            self.dirty = True
        ready_conclusion()

    Radiobutton(label0, text="Yes", value="True", variable=hun, pady=7, padx=5, background="#34A2FE",
                font=("black", 11), command=hun1).grid(row=0, column=1)
    Radiobutton(label0, text="No", value="False", variable=hun, pady=7, padx=5, background="#34A2FE",
                font=("black", 11), command=hun1).grid(row=0, column=2)
    Radiobutton(label0, text="Yes", value="True", variable=thi, pady=7, padx=5, background="#34A2FE",
                font=("black", 11), command=thi1).grid(row=1, column=1)
    Radiobutton(label0, text="No", value="False", variable=thi, pady=7, padx=5, background="#34A2FE",
                font=("black", 11), command=thi1).grid(row=1, column=2)
    Radiobutton(label0, text="Yes", value="True", variable=ddir, pady=7, padx=5, background="#34A2FE",
                font=("black", 11), command=ddir1).grid(row=2, column=1)
    Radiobutton(label0, text="No", value="False", variable=ddir, pady=7, padx=5, background="#34A2FE",
                font=("black", 11), command=ddir1).grid(row=2, column=2)

    label1 = LabelFrame(label0, text="Here will be our recommendation:)", width=400, height=100,
                        background="#34A2FE",
                        font=("black", 14))
    label1.grid(sticky="enws", row=3, column=1, columnspan=2)
