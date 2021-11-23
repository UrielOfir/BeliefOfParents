# Import the required libraries
from tkinter import *
from idlelib.tooltip import Hovertip
import webbrowser
from func_a_parent import *
import func_about
import func_gender_and_age

class Menu:
    # Setting the main window
    def __init__(self, master):
        self.master = master
        master.title("Trust as a sleeping aid for children")
        self.title_of_main = Label(master, text="How to help your child fall a sleep, using the Shefer Method",
                                   font=('Helvetica bold', 18),
                                   padx=120, pady=50, background="#34A2FE", borderwidth=7).grid(row=0, column=0,
                                                                                                columnspan=3)

        self.button_starting_parent = Button(master, text="I want to start from the beginning",
                                             font=('Helvetica bold', 11), padx=45, pady=30,
                                             command=self.click_button_starting_parent).grid(row=1, column=0)
        self.button_practiced_parent = Button(master, text="I'm here again and need you", font=('Helvetica bold', 11),
                                              padx=45, pady=30, command=self.begin).grid(row=1, column=1)
        self.button_for_reminder = Button(master, text="I'm just need a little reminder", font=('Helvetica bold', 11),
                                          padx=45, pady=30, command=self.click_button_to_reminder).grid(row=1, column=2)
        self.button_about_shefer_approach = Button(master, text="About Shefer Approach", font=('Helvetica bold', 11),
                                                   padx=75, pady=30,
                                                   command=self.click_button_about_shefer_approach).grid(row=2,
                                                                                                         column=0)
        self.button_about_this_project = Button(master, text="About this project", font=('Helvetica bold', 11), padx=79,
                                                pady=30, command=self.click_button_about_project).grid(row=2, column=1)
        self.button_about_me = Button(master, text="About me", font=('Helvetica bold', 11), padx=106, pady=30,
                                      command=self.click_button_about_me).grid(
            row=2, column=2)

    # Setting a 'global' variables
    about_what = ""
    status = ""
    optionalProblemAndSolution = ["hungry", "thirsty", "dirty"]
    the_gender = "gender"
    only_gander = "child"
    gender = "your child"
    gender_y = "your child"
    gender_first = ""
    belong = "his"
    to_ = "him"
    level = 0
    select_check_b = False
    get_hungry = False
    get_thirst = False
    get_dirty = False
    ready = False
    hungry = False
    thirst = False
    dirty = False

    get_gender = False
    get_age = False
    finish = False

    # Setting the click function
    def click_button_starting_parent(self):
        #func_ask_user.ask_user(self, "Do you have a child?")
        #func_ask_user.ask_user(self, "Do you have a child?")
        self.ask_user("Do you have a child?")

    def begin(self):
        self.status = "a parent"
        func_gender_and_age.gender_and_age(self)
        # self.gender_and_age()

    def click_button_to_reminder(self):
        self.status = "reminder"
        func_gender_and_age.gender_and_age(self)
        # self.gender_and_age()

    def click_button_about_shefer_approach(self):
        self.about_what = "Shefer Approach"
        func_about.about(self)
        #self.about()

    def click_button_about_project(self):
        self.about_what = "This Project"
        func_about.about(self)
        #self.about()

    def click_button_about_me(self):
        self.about_what = "Me"
        func_about.about(self)
        #self.about()

    # Auxiliary functions
    def ask_user(self, question):
        ask_window = Toplevel()
        ask_window.grab_set()
        ask_window.geometry("350x120")
        ask_window.resizable(False, False)
        ask_window.title("Please click your choice:")
        Frame(ask_window, background="#34A2FE", width=350, height=60, pady=3).grid(row=0, sticky="ewn", columnspan=2)
        Label(ask_window, text=question, background="#34A2FE", font=("black", 14)).grid(row=0, sticky="ew")

        def answer():
            ask_window.destroy()
            ans = Toplevel()
            ans.grab_set()
            ans.geometry("250x227")
            ans.resizable(False, False)
            ans.title("Bye")
            ans.configure(bg="#34A2FE")
            text_bye = "\nOK. You really don't need this \nheadache now (: " \
                       "\nWe will be happy to help you when\n you will need us.\n\nGoodbye!!\n\n\n\n"
            label1 = LabelFrame(ans, text="So...", width=350, height=120, background="#34A2FE", font=("black", 14))
            label1.grid(sticky="enws")
            label2 = Label(label1, text=text_bye, background="#34A2FE", font=("black", 11))
            label2.grid(sticky="enws")
            main.after(6000, main.destroy)
            # time.sleep(10)
            # raise SystemExit
            # main.after(10000, main.destroy)
            # main.after(10000, main.destroy)

        def beginning():
            self.status = "a parent"
            ask_window.destroy()
            func_gender_and_age.gender_and_age(self)
            # self.gender_and_age()

        Label(ask_window, text="", ).grid(row=1, columnspan=2)
        Button(ask_window, text="Yes", font=('Helvetica bold', 11), padx=35, pady=1,
               command=beginning).grid(row=2, column=0)
        Button(ask_window, text="No", font=('Helvetica bold', 11), padx=35, pady=1, command=answer).grid(row=2,
                                                                                                         column=1)


# Main
main = Tk()
main.resizable(False, False)
main.title("How to think that the child will fall asleep?")
my_gui = Menu(main)
main.mainloop()
