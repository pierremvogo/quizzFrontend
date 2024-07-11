import random
import time
import asyncio
from tkinter import *
import tkinter
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

from api.admin import Admin
from api.student import Student
from view.manageAnswer import ManageAnswer
from view.manageQuestion import ManageQuestion
from view.manageQuizz import ManageQuizz
from view.manageStudent import ManageStudent

window=tkinter.Tk()
window.title("Quizz Management System")
window.geometry("850x560")

style=ttk.Style()

frame=tkinter.Frame(window,bg="#02577A")
frame1=tkinter.Frame(window,bg="#02577A")
frame2=tkinter.Frame(window,bg="#02577A")
frame2.pack()
frame1.pack()
frame.pack()

btnColor="#196E78"

manageFrame=tkinter.LabelFrame(frame,text="ADMINISTRATOR ACTIONS",borderwidth=5)
manageFrame.grid(row=0,column=0,sticky="W",padx=[10,200],pady=20,ipadx=[5])


def manageStudent():
   studentBtn.configure(bg = "grey")
   quizBtn.config(bg = btnColor)
   questionBtn.config(bg = btnColor)
   answerBtn.config(bg = btnColor)
   ManageStudent(window,frame,btnColor,style).constructFrame()

def manageQuiz():
    studentBtn.configure(bg = btnColor)
    quizBtn.config(bg = "grey")
    questionBtn.config(bg = btnColor)
    answerBtn.config(bg = btnColor)
    ManageQuizz(window,frame,btnColor,style).constructFrame()

def manageQuestion():
    studentBtn.configure(bg = btnColor)
    quizBtn.config(bg = btnColor)
    questionBtn.config(bg = "grey")
    answerBtn.config(bg = btnColor)
    ManageQuestion(window,frame,btnColor,style).constructFrame()

def manageAnswer():
    studentBtn.configure(bg = btnColor)
    quizBtn.config(bg = btnColor)
    questionBtn.config(bg = btnColor)
    answerBtn.config(bg = "grey")
    ManageAnswer(window,frame,btnColor,style).constructFrame()

def disconnect():
    controlPrivileges()
def header():
    global studentBtn, quizBtn, questionBtn, answerBtn
    studentBtn=Button(manageFrame,text="MANAGE STUDENT",width=20,borderwidth=3,bg=btnColor,fg='white',command=manageStudent, cursor="hand2")
    quizBtn=Button(manageFrame,text="MANAGE QUIZZ",width=20,borderwidth=3,bg=btnColor,fg='white',command=manageQuiz, cursor="hand2")
    questionBtn=Button(manageFrame,text="MANAGE QUESTION",width=20,borderwidth=3,bg=btnColor,fg='white',command=manageQuestion, cursor="hand2")
    answerBtn=Button(manageFrame,text="MANAGE ANSWER",width=20,borderwidth=3,bg=btnColor,fg='white',command=manageAnswer, cursor="hand2")
    logoutBtn=Button(manageFrame,text="DISCONNECT",width=20,borderwidth=3,bg=btnColor,fg='white',command=disconnect, cursor="hand2")

    studentBtn.grid(row=0,column=0,padx=5,pady=5)
    quizBtn.grid(row=0,column=1,padx=5,pady=5)
    questionBtn.grid(row=0,column=2,padx=5,pady=5)
    answerBtn.grid(row=0,column=3,padx=5,pady=5)
    logoutBtn.grid(row=0,column=4,padx=5,pady=5)
header()

def controlPrivileges(studentNumber=None,code=None):
    if studentNumber is None and code is None:
        frame1.pack()
        MainScreen(window,frame1).constructFrame()
        frame2.pack_forget()
        frame.pack_forget()
    elif studentNumber is not None:
        frame2.pack()       
        QuizScreen(window,frame2).constructFrame()
        frame1.pack_forget()
        frame.pack_forget()
    elif code is not None:
        frame.pack()
        ManageStudent(window,frame,btnColor,style).constructFrame()
        frame1.pack_forget()
        frame2.pack_forget()
        
class MainScreen:
    def __init__(self,window,frame):
        self.window = window,
        self.frame= frame
        self.image = Image.open("C:/Users/pc/Documents/projetPython/frontendQuizz/view/img1.png")
        self.bg = ImageTk.PhotoImage(self.image)
        self.canvas = Canvas(self.frame, width=800, height=700, bg="#d0d2d6")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(15, 100, anchor=NW, image=self.bg)
        self.canvas.create_text(380, 70, text="Welcome To Your Quizz App!", font=("Purisa",30, 'bold italic'), fill="black")
        self.student_number = None
        self.code = None
    def constructFrame(self):
        label=Label(self.frame,text="",width=100,height=2,borderwidth=3)
        b1=Button(self.frame,text="I'M STUDENT",width=40,height=2,borderwidth=3,bg="#538CC6",font=("Purisa",10,"bold"),fg='white', cursor="hand2", command=self.displayQuiz)
        b2=Button(self.frame,text="I'M ADMINISTRATOR",width=40,height=2,borderwidth=3,bg="#538CC6",font=("Purisa",10,"bold"),fg='white', cursor="hand2", command=self.displayAdmin)
        
        
        self.canvas.create_window(70,220, anchor="nw", window=b1)
        self.canvas.create_window(70,290, anchor="nw", window=b2)

    def openAdminModal(self):
        pop = Toplevel(frame1)
        pop.title("Please Enter your Admin Code")
        pop.geometry("500x150")
        pop.config(bg="white")
        pop.grab_set()
        frame4 = Frame(pop)
        frame4.pack(pady=10)
        self.codeLabel=Label(frame4,text="Admin Code",anchor="e",width=15, fg="black")
        self.codeLabel.grid(row=0,column=0,padx=10)

        self.b1=Button(frame4,text="Get Access >",cursor="hand2",width=20,height=1,bg=btnColor,fg="white",command=lambda:self.signInAdmin(str(self.codeEntry.get()),pop))
        self.b1.grid(row=1,column=2,columnspan=10,padx=5,pady=5)

        self.codeEntry=Entry(frame4,width=50,textvariable="")
        self.codeEntry.grid(row=0,column=2,padx=5,pady=5)

    def signInAdmin(self,code,pop):
        try:
            results =  Admin().getAdminByCode(code)
            self.code = results["code"]
            pop.destroy()
            print("C1")
            controlPrivileges(None,self.code)
        except:
            messagebox.showwarning("", "An Error Occured! please try again")

    def openStudentModal(self):
        pop = Toplevel(frame1)
        pop.title("Please Enter your Student Number")
        pop.geometry("500x150")
        pop.config(bg="white")
        pop.grab_set()
        frame5 = Frame(pop)
        frame5.pack(pady=10)
    
        self.numberLabel=Label(frame5,text="Student Number",anchor="e",width=15, fg="black")
        self.numberLabel.grid(row=0,column=0,padx=10)

        self.b1=Button(frame5,text="Get Access >",cursor="hand2",width=20,height=1,bg=btnColor,fg="white",command=lambda:self.signInStudent(str(self.numberEntry.get()),pop))
        self.b1.grid(row=1,column=2,columnspan=10,padx=5,pady=5)

        self.numberEntry=Entry(frame5,width=50,textvariable="")
        self.numberEntry.grid(row=0,column=2,padx=5,pady=5)

    def signInStudent(self,student_number,pop):
        try:
            results =  Student().getStudentByNumber(student_number)
            self.student_number = results["student_number"]
            pop.destroy()
            controlPrivileges(self.student_number,None)
        except:
            print("ERROR OCCURED")
            messagebox.showwarning("", "An Error Occured! please try again")
    
    def displayAdmin(self):
        if (self.code is None):
            self.openAdminModal()
        else:
            controlPrivileges(None, self.code)

    def displayQuiz(self):
        if (self.student_number is None):
            self.openStudentModal()
        else:
            controlPrivileges(self.student_number, None)

class QuizScreen:
    def __init__(self,window,frame):
        self.window = window,
        self.frame= frame
        self.image = Image.open("C:/Users/pc/Documents/projetPython/frontendQuizz/view/img1.png")
        self.bg = ImageTk.PhotoImage(self.image)
        self.canvas = Canvas(self.frame, width=800, height=700, bg="#d0d2d6")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(15, 100, anchor=NW, image=self.bg)
        self.canvas.create_text(380, 70, text="Welcome To Your Quizz App!", font=("Purisa",30, 'bold italic'), fill="black")
    def constructFrame(self):
        label=Label(self.frame,text="",width=100,height=2,borderwidth=3)
        b1=Button(self.frame,text="ALREADY",width=40,height=2,borderwidth=3,bg="red",font=("Purisa",10,"bold"),fg='white', cursor="hand2", command=self.displayQuiz)
        b2=Button(self.frame,text="ALREADY",width=40,height=2,borderwidth=3,bg="red",font=("Purisa",10,"bold"),fg='white', cursor="hand2", command=self.displayAdmin)
        
        
        self.canvas.create_window(70,220, anchor="nw", window=b1)
        self.canvas.create_window(70,290, anchor="nw", window=b2)

    def displayAdmin(self):
        print("ADMIN SYSTEM")
        controlPrivileges(None, 125)

    def displayQuiz(self):
        print("QUIZ SYSTEM")
        controlPrivileges(2, None)


async def main():
   controlPrivileges()
   window.resizable(False,False)
   window.mainloop()
   
if __name__ == "__main__":
   asyncio.run(main())