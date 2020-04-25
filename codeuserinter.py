from Tkinter import *
import tkMessageBox
class App:
    def __init__(self, master):
        #First Name
        Label(master, text=”First Name”).grid(row=0)
        self.e1=Entry(master)
        self.e1.grid(row=0, column=1)
        #Last Name
        Label(master, text=”Last Name”).grid(row=1)
        self.e2=Entry(master)
        self.e2.grid(row=1, column=1)
        #Age
        Label(master, text=”Age”).grid(row=2)
        self.e3=Entry(master)
        self.e3.grid(row=2, column=1)
        #Blank
        Label(master, text=””, width=5).grid(row=0, column=3)
        #Gender
        Label(master, text=”Gender”).grid(row=0, column=4)
        self.f1=Frame(master, relief= “sunken”, bd=2)
        self.v=IntVar()
        self.r1=Radiobutton(self.f1, text=”Male”,\
        variable=self.v, value=1).pack(anchor=W)
        self.r2=Radiobutton(self.f1, text=”Female”,\
        variable=self.v, value=2).pack(anchor=W)
        self.f1.grid(row=1, column=4)
        #Blank
        Label(master, text=””).grid(row=3)
        #Course Applied For
        Label(master, text=”Course Applied for:”,
wraplength=60).grid(row=4)
        self.L1 = Listbox(master, width = 25, height = 4)
        for item in [“Quality Management (Adv.)”,\
        “Financial Management (Adv.)”,\
        “Project Management (Adv.)”,\
        “Project Management (Int.)”]:
            self.L1.insert(END, item)
        self.L1.grid(row=4, column=1)
#Buttons
        self.f2=Frame(master)

        self.w=Button(self.f2, text =”Prerequisites”, height =1,\
            width=10, command=self.Chk_Prereq, default=ACTIVE).pack()
            self.w1=Button(self.f2, text =”Clear”, height =1, \
                width=10, command=self.Clear).pack()
        self.w2=Button(self.f2, text =”Cancel”, height=1, \
                width=10, command=self.Close).pack()
        self.f2.grid(row=4, column=4)
        #Blank
        Label(master, text=””).grid(row=6)
        #Checkbox
        self.var=IntVar()
        self.c=Checkbutton(master, text=”Part-Time Course”, variable=
self.var, offvalue=0, onvalue=1)
        self.c.grid(row=7)

def Chk_Prereq(self):
        self.Eval()
def Eval(self):
        self.fname = self.e1.get()
        self.lname = self.e2.get()
        self.age =  int(self.e3.get())
#Check for Age
        if self.age < 21:
            tkMessageBox.showwarning(“Invalid Age”,\
“You are not eligible”)
            return
#Check for Gender
        if self.v.get()==1:
                self.str1 = “Dear Mr.”
        elif self.v.get()==2:
                self.str1 = “Dear Ms.”
        else:
            tkMessageBox.showwarning(“Missing Info”, \
            “Please select the appropriate gender”)
            return
        #Check for Prereq Course
        self.name = self.str1 + “ “ + self.fname + “ “ + self.lname
        self.varl1 = self.L1.get(self.L1.curselection())

        if self.varl1 == “Quality Management (Adv.)”:
            self.prereq =
        “The prereq for this course is Quality Management (Int).”
            self.flag = 1
        elif self.varl1 == “Financial Management (Adv.)”:
            self.prereq = \
        “The prereq for this course is Financial Management (Bas).”
            self.flag = 1
        elif self.varl1 == “Project Management (Adv.)”:
            self.prereq = \
        “The prereq for this course is Project Management (Int).”
            self.flag = 0
        else:
            self.prereq = \
        “The prereq for this course is Project Management (Bas).”
            self.flag = 0
        #Check whether Part Time
        if self.var.get() == 1 and self.flag == 0:
            self.str2 = “\nThis course is not available part time.”
        elif self.var.get() == 1 and self.flag == 1:
            self.str2 = “\nThis course is available part time.”
        else:
            self.str2 = “”
            self.result = self.prereq + self.str2
            tkMessageBox.showinfo(self.name, self.result)
        def Close(self):
            root.destroy()
        def Clear(self):
            self.e1.delete(0,END)
            self.e2.delete(0,END)
            self.e3.delete(0,END)
            self.c.deselect()
            self.L1.select_clear(self.L1.curselection())

root = Tk()
app = App(root)
root.mainloop()
