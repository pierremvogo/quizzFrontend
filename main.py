import random
import time
import asyncio
from tkinter import *
import tkinter
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

from tkinter import StringVar
from api.admin import Admin
from api.answer import Answer
from api.question import Question
from api.quizz import Quizz
from api.student import Student
from view.manageAnswer import ManageAnswer
from view.manageQuestion import ManageQuestion
from view.manageQuizz import ManageQuizz
from view.manageStudent import ManageStudent

window=tkinter.Tk()
img = PhotoImage(file="C:/Users/pc/Documents/projetPython/frontendQuizz/view/icon.png")
window.iconphoto(False, img)
window.wm_iconphoto(False,img)
window.title("Quizz App")
window.geometry("1360x768")

style=ttk.Style()

frame=tkinter.Frame(window,bg="#02577A")
frame1=tkinter.Frame(window,bg="#02577A")
frame2=tkinter.Frame(window,bg="#02577A")
frame2.pack()
frame1.pack()
frame.pack()

btnColor="#196E78"

manageFrame=tkinter.LabelFrame(frame,text="ADMINISTRATOR ACTIONS",borderwidth=2, font=("Tahoma", 15),fg="black")
manageFrame.grid(row=0,column=0,sticky="W",padx=[10,0],pady=20,ipadx=[10])


def manageStudent():
   studentBtn.configure(bg = "grey")
   quizBtn.config(bg = btnColor)
   questionBtn.config(bg = btnColor)
   answerBtn.config(bg = btnColor)
   ManageStudent(window,frame,btnColor,style)

def manageQuiz():
    studentBtn.configure(bg = btnColor)
    quizBtn.config(bg = "grey")
    questionBtn.config(bg = btnColor)
    answerBtn.config(bg = btnColor)
    ManageQuizz(window,frame,btnColor,style)

def manageQuestion():
    studentBtn.configure(bg = btnColor)
    quizBtn.config(bg = btnColor)
    questionBtn.config(bg = "grey")
    answerBtn.config(bg = btnColor)
    ManageQuestion(window,frame,btnColor,style)

def manageAnswer():
    studentBtn.configure(bg = btnColor)
    quizBtn.config(bg = btnColor)
    questionBtn.config(bg = btnColor)
    answerBtn.config(bg = "grey")
    ManageAnswer(window,frame,btnColor,style)

def disconnect():
    controlPrivileges()
def header():
    global studentBtn, quizBtn, questionBtn, answerBtn
    studentBtn=Button(manageFrame,text="MANAGE STUDENT",width=25,borderwidth=3,bg=btnColor,fg='white', height=2,command=manageStudent, cursor="hand2")
    quizBtn=Button(manageFrame,text="MANAGE QUIZZ",width=25,borderwidth=3,bg=btnColor,fg='white',height=2,command=manageQuiz, cursor="hand2")
    questionBtn=Button(manageFrame,text="MANAGE QUESTION",width=25,borderwidth=3,bg=btnColor,fg='white',height=2,command=manageQuestion, cursor="hand2")
    answerBtn=Button(manageFrame,text="MANAGE ANSWER",width=25,borderwidth=3,bg=btnColor,fg='white',height=2,command=manageAnswer, cursor="hand2")
    logoutBtn=Button(manageFrame,text="DISCONNECT",width=25,borderwidth=3,bg=btnColor,fg='white',height=2,command=disconnect, cursor="hand2")

    studentBtn.grid(row=0,column=1,padx=[350,0],pady=5)
    quizBtn.grid(row=0,column=2,padx=5,pady=5)
    questionBtn.grid(row=0,column=3,padx=5,pady=5)
    answerBtn.grid(row=0,column=4,padx=5,pady=5)
    logoutBtn.grid(row=0,column=5,padx=5,pady=5)
header()

def controlPrivileges(studentNumber=None,code=1024, quizz="quiz1", sname="pierre", quizId=2):
    if studentNumber is None and code is None:
        frame1.pack()
        MainScreen(window,frame1).constructFrame()
        frame2.destroy()
        frame.destroy()
    elif studentNumber is not None:
        frame2.pack()       
        QuizScreen(window,frame2,quizz,sname,quizId)
        frame1.destroy()
        frame.destroy()
    elif code is not None:
        frame.pack()
        ManageStudent(window,frame,btnColor,style)
        frame1.destroy()
        frame2.destroy()
        
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
            print(results)
            self.code = results["code"]
            pop.destroy()
            controlPrivileges(None,self.code)
            self.code = None
            self.student_number = None
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
        self.placeholderArray = ['','','','','']
        for i in range(0,5):
            self.placeholderArray[i]=tkinter.StringVar()

        self.categoryArray=[]
        self.categoryArray1=[]
        self.quizz = Quizz().getQuizz()
        print("ALL QUIIZ DATA: ",self.quizz)
        for quizz in self.quizz:
            self.categoryArray.append(quizz['title'])
            self.categoryArray1.append({'quizz_id':quizz['id'], 'quizz_title':quizz['title']})
            
        self.numberLabel=Label(frame5,text="Student Number",anchor="e",width=15, fg="black")
        self.numberLabel.grid(row=0,column=0,padx=10)

        self.b1=Button(frame5,text="Get Access >",cursor="hand2",width=20,height=1,bg=btnColor,fg="white",command=lambda:self.signInStudent(str(self.numberEntry.get()),pop))
        self.b1.grid(row=2,column=2,columnspan=10,padx=5,pady=5)

        self.numberEntry=Entry(frame5,width=50,textvariable="")
        self.numberEntry.grid(row=0,column=2,padx=5,pady=5)
        


        self.quizLabel=Label(frame5,text="Select your quiz",anchor="e",width=15, fg="black")
        self.quizLabel.grid(row=1,column=0,padx=10)

        self.quizCombo=ttk.Combobox(frame5,width=47,textvariable=self.placeholderArray[1],values=self.categoryArray)
        self.quizCombo.grid(row=1,column=2,padx=5,pady=5)

    def getQuizId(self):
        for cat1 in self.categoryArray1:
            if(self.quizCombo.get() == cat1['quizz_title']):
                print("quizz Id", cat1["quizz_id"])
                return cat1['quizz_id']
    def signInStudent(self,student_number,pop):
        try:
            results =  Student().getStudentByNumber(student_number)
            self.student_number = results["student_number"]
            Student(self.student_number,None,None,self.getQuizId()).updateQuizStudent(results["id"])
            controlPrivileges(self.student_number,None, self.quizCombo.get(), results["name"]+" "+results["surname"], self.getQuizId())
            self.student_number = None
            self.code = None
            pop.destroy()
        except:
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
    def __init__(self,window,frame,quiz,sname,quiz_id):
        self.window = window
        self.frame = frame
        self.quizz = quiz
        self.sname = sname
        self.quiz_id = quiz_id
        self.questions1 = Question().getQuestion()
        self.questions = []
        self.options = []
        self.dict_questions = {}

        self.questions1 = Question().getQuestionByQuizId(self.quiz_id)
        for question1 in self.questions1:
            answer = Answer().getAnswerByQuestionId(question1["id"])
            self.dict_questions[f"{question1["question_text"]}"] = answer
        for key,value in self.dict_questions.items():
            self.questions.append(key)
            self.options.append(value)
        
        self.v1 = StringVar(self.frame)
        self.v2 = StringVar(self.frame)
        self.v3 = StringVar(self.frame)
        self.v4 = StringVar(self.frame)
        self.titleFrame = LabelFrame(self.frame,text=str(self.sname).upper(),fg="Orange" ,font=('Verdana', 10),borderwidth=2, width=200,bg="#02577A")
       
        self.title = Label(self.titleFrame, height=1, fg="black", font=('Verdana', 15),bg="#02577A", text=self.quizz, wraplength=500,)
        self.disconnect = Button(self.titleFrame,text="DISCONNECT",width=20,borderwidth=3,bg=btnColor,fg='white',command=self.disconnect,cursor="hand2")
       
        self.question_label = Label(self.frame, height=4, width=50, fg="black", font=('Verdana', 20), text="hgvcg", wraplength=500, bg='#ddd')
        self.option1 = Radiobutton(self.frame, bg="#fff", variable=self.v1, width=75, cursor="hand2", font=('Verdana', 13), command=lambda:self.checkAnswer(self.option1))
        self.option2 = Radiobutton(self.frame, bg="#fff", variable=self.v2, width=75,cursor="hand2", font=('Verdana', 13), command=lambda:self.checkAnswer(self.option2))
        self.option3 = Radiobutton(self.frame, bg="#fff", variable=self.v3, width=75,cursor="hand2", font=('Verdana', 13), command=lambda:self.checkAnswer(self.option3))
        self.option4 = Radiobutton(self.frame, bg="#fff", variable=self.v4, width=75,cursor="hand2", font=('Verdana', 13), command=lambda:self.checkAnswer(self.option4))
        
        self.btn_next = Button(self.frame, text="Next Question >",cursor="hand2",bg="Orange", width=15, font=("Verdana", 15), command=self.displayNextQuestion)
        self.frame.pack(fill="both", expand="true")
        self.titleFrame.grid(row=0, column=0,padx=[0,10], pady=[2,2])
        self.title.grid(row=0,column=0,padx=[0,450], pady=[5,0])
        self.disconnect.grid(row=0,column=1, padx=[110,5],pady=[5,0])
        self.question_label.grid(row=1, column=0,)

        self.option1.grid(sticky="W", row=2, column=0, pady=10)
        self.option2.grid(sticky="W", row=3, column=0, pady=10)
        self.option3.grid(sticky="W", row=4, column=0, pady=10)
        self.option4.grid(sticky="W", row=5, column=0, pady=10)

        self.btn_next.grid(row=6, column=0,pady=[10,0])
        self.displayNextQuestion()
        print(self.correct)

        
    index = 0
    correct = 0
    def disconnect(self):
        controlPrivileges()
    def disableButton(self, state):
        self.option1['state'] = state
        self.option2['state'] = state
        self.option3['state'] = state
        self.option4['state'] = state

    def checkAnswer(self,radio):
        global correct, index
        for option in self.options[self.index]:
            if radio['text'] == option['answer_text'] and option['is_correct'] == 1:
                self.correct += 1
        self.index += 1
        self.disableButton('disable')

    def displayNextQuestion(self):
        global correct, index

        if self.btn_next['text'] == 'Restart The Quiz':
            self.correct = 0
            self.index = 0
            self.question_label['bg'] = '#ddd'
            self.btn_next['text'] = 'Next'

        if self.index == len(self.options):
            self.question_label['text'] = "Result: "+ str(self.correct) + " / " + str(len(self.options))+"\n"+str(round((((self.correct)/len(self.options))*100),2))+"%"
            self.question_label['bg'] = 'green'
            self.btn_next['width'] = 20
            self.btn_next['text'] = 'Restart The Quiz'
            if self.correct >= len(self.options)/2:
                self.question_label['bg'] = "green"
            else:
                self.question_label['bg'] = "red"

        else:
            self.question_label['text'] = self.questions[self.index]

            self.disableButton('normal')
            opts = self.options[self.index]
            self.option1['text'] = opts[0]['answer_text']
            self.option2['text'] = opts[1]['answer_text']
            self.option3['text'] = opts[2]['answer_text']
            self.option4['text'] = opts[3]['answer_text']

            self.v1.set(opts[0]['answer_text'])
            self.v2.set(opts[1]['answer_text']) 
            self.v3.set(opts[2]['answer_text'])
            self.v4.set(opts[3]['answer_text'])

            if self.index == len(self.options)-1:
                self.btn_next['text'] = 'Check Result'


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