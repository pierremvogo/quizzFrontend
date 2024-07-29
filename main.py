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
from api.student_answer import StudentAnswer
from api.tutor import Tutor
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
frame3=tkinter.Frame(window,bg="#02577A")
btnColor="#196E78"


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

def disconnectAdmin():
    frame.pack_forget()
    frame1.pack()
    controlPrivileges()


def header():
    global studentBtn, quizBtn, questionBtn, answerBtn

    manageFrame=tkinter.LabelFrame(frame,text="ADMINISTRATOR ACTIONS",borderwidth=2, font=("Tahoma", 15),fg="black")
    manageFrame.grid(row=0,column=0,sticky="W",padx=[10,0],pady=20,ipadx=[10])

    studentBtn=Button(manageFrame,text="MANAGE STUDENT",width=25,borderwidth=3,bg=btnColor,fg='white', height=2,command=manageStudent, cursor="hand2")
    quizBtn=Button(manageFrame,text="MANAGE QUIZZ",width=25,borderwidth=3,bg=btnColor,fg='white',height=2,command=manageQuiz, cursor="hand2")
    questionBtn=Button(manageFrame,text="MANAGE QUESTION",width=25,borderwidth=3,bg=btnColor,fg='white',height=2,command=manageQuestion, cursor="hand2")
    answerBtn=Button(manageFrame,text="MANAGE ANSWER",width=25,borderwidth=3,bg=btnColor,fg='white',height=2,command=manageAnswer, cursor="hand2")
    logoutBtn=Button(manageFrame,text="DISCONNECT",width=25,borderwidth=3,bg=btnColor,fg='white',height=2,command=disconnectAdmin, cursor="hand2")

    studentBtn.grid(row=0,column=1,padx=[350,0],pady=5)
    quizBtn.grid(row=0,column=2,padx=5,pady=5)
    questionBtn.grid(row=0,column=3,padx=5,pady=5)
    answerBtn.grid(row=0,column=4,padx=5,pady=5)
    logoutBtn.grid(row=0,column=5,padx=5,pady=5)
header()




def controlPrivileges(studentNumber=None,code=None,tutor_code=None, quizz=None, sname=None,sid=None, quizId=None):
    print("-----STN",studentNumber,"----STC",code)
    if studentNumber is None and code is None and tutor_code is None:
        frame1.pack()
        MainScreen(window,frame1).constructFrame()
    elif studentNumber is not None:
        frame2.pack()       
        QuizScreen(window,frame2,quizz,sname,sid,quizId)
    elif code is not None:
        frame.pack()
        ManageStudent(window,frame,btnColor,style)
    elif tutor_code is not None:
        frame3.pack()
        print("FRAME1333")
        TutorScreen(window,frame3)
        print("FRAME3")








        
class MainScreen:
    def __init__(self,window,frame):
        self.window = window,
        self.frame= frame
        self.image = Image.open("C:/Users/pc/Documents/projetPython/frontendQuizz/view/img1.png")
        self.bg = ImageTk.PhotoImage(self.image)
        self.canvas = Canvas(self.frame, width=1350, height=760, bg="#d0d2d6")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(15, 100, anchor=NW, image=self.bg)
        self.canvas.create_text(380, 70, text="Welcome To Your Quizz App!", font=("Purisa",30, 'bold italic'), fill="black")
        self.student_number = None
        self.code = None
        self.tutor_code = None

    def constructFrame(self):
        label=Label(self.frame,text="",width=100,height=2,borderwidth=3)
        b1=Button(self.frame,text="I'M STUDENT",width=40,height=2,borderwidth=3,bg="#538CC6",font=("Purisa",10,"bold"),fg='white', cursor="hand2", command=self.displayQuiz)
        b2=Button(self.frame,text="I'M ADMINISTRATOR",width=40,height=2,borderwidth=3,bg="#538CC6",font=("Purisa",10,"bold"),fg='white', cursor="hand2", command=self.displayAdmin)
        b3=Button(self.frame,text="I'M TUTOR",width=40,height=2,borderwidth=3,bg="#538CC6",font=("Purisa",10,"bold"),fg='white', cursor="hand2", command=self.displayTutor)
        
        
        self.canvas.create_window(70,220, anchor="nw", window=b1)
        self.canvas.create_window(70,290, anchor="nw", window=b2)
        self.canvas.create_window(70,360, anchor="nw", window=b3)

    def openAdminModal(self):
        self.pop = Toplevel()
        self.pop.title("Please Enter your Admin Code")
        self.pop.geometry("500x150")
        self.pop.config(bg="white")
        self.pop.grab_set()
        self.frame4 = Frame(self.pop)
        self.frame4.pack(pady=10)
        self.codeLabel=Label(self.frame4,text="Admin Code",anchor="e",width=15, fg="black")
        self.codeLabel.grid(row=0,column=0,padx=10)

        self.b1=Button(self.frame4,text="Get Access >",cursor="hand2",width=20,height=1,bg=btnColor,fg="white",command=lambda:self.signInAdmin(str(self.codeEntry.get()),self.pop))
        self.b1.grid(row=1,column=2,columnspan=10,padx=5,pady=5)

        self.codeEntry=Entry(self.frame4,width=50,textvariable="")
        self.codeEntry.grid(row=0,column=2,padx=5,pady=5)


    def openTutorModal(self):
        self.pop = Toplevel()
        self.pop.title("Please Enter your Admin Code")
        self.pop.geometry("500x150")
        self.pop.config(bg="white")
        self.pop.grab_set()
        self.frame4 = Frame(self.pop)
        self.frame4.pack(pady=10)
        self.codeLabel=Label(self.frame4,text="Admin Code",anchor="e",width=15, fg="black")
        self.codeLabel.grid(row=0,column=0,padx=10)

        self.b1=Button(self.frame4,text="Get Access >",cursor="hand2",width=20,height=1,bg=btnColor,fg="white",command=lambda:self.signInTutor(str(self.codeEntry.get()),self.pop))
        self.b1.grid(row=1,column=2,columnspan=10,padx=5,pady=5)

        self.codeEntry=Entry(self.frame4,width=50,textvariable="")
        self.codeEntry.grid(row=0,column=2,padx=5,pady=5)


    def signInTutor(self,code,pop):
        try:
            pop.destroy()
            results =  Tutor().getTutorByCode(code)
            print(results)
            self.tutor_code = int(results["code"])
            frame1.pack_forget()
            print("SING 1")
            controlPrivileges(None,None, self.tutor_code)
            print("SING 2")
            self.code = None
            self.student_number = None
            self.tutor_code = None
            
        except:
            messagebox.showwarning("", "An Error Occured! please try again--")

    def signInAdmin(self,code,pop):
        try:
            pop.destroy()
            results =  Admin().getAdminByCode(code)
            print(results)
            self.code = int(results["code"])
            frame1.pack_forget()
            controlPrivileges(None,self.code)
            print("break2")
            self.code = None
            self.student_number = None
            self.tutor_code = None
            
        except:
            messagebox.showwarning("", "An Error Occured! please try again--")
            
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
        self.quizzArray = []
        print("ALL QUIIZ DATA: ",self.quizz)
        for quizz in self.quizz:
            print("ddd--------------------------------->>>",Question().getQuestionByQuizId(quizz['id']))
            if(isinstance(Question().getQuestionByQuizId(quizz['id']), list)):
                self.quizzArray.append(quizz)
        print("Text Question -------------->>>>>-->", self.quizzArray)
        for i in range(0, len(self.quizzArray)):
                self.categoryArray.append(self.quizzArray[i]['title'])
                self.categoryArray1.append({'quizz_id':self.quizzArray[i]['id'], 'quizz_title':self.quizzArray[i]['title']})
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
            Student(self.student_number,None,None,self.getQuizId()).updateQuizStudent(results["student_id"])
            print(self.student_number, self.quizCombo.get(),results["name"]+" "+results["surname"],results["student_id"],self.getQuizId())
            frame1.pack_forget()
            controlPrivileges(
                self.student_number,
                None, 
                None,
                self.quizCombo.get(), 
                results["name"]+" "+results["surname"],
                results["student_id"],
                self.getQuizId()
                )
            self.student_number = None
            self.code = None
            self.tutor_code = None
            pop.destroy()
        except:
            messagebox.showwarning("", "An Error Occured! please try again")

    
    def displayAdmin(self):
        if (self.code is None):
            self.openAdminModal()
        else:
            controlPrivileges(None, self.code, None)

    def displayQuiz(self):
        if (self.student_number is None):
            self.openStudentModal()
        else:
            controlPrivileges(self.student_number, None, None)

    def displayTutor(self):
        if (self.tutor_code is None):
            self.openTutorModal()
        else:
            controlPrivileges(None, None, self.tutor_code)










class TutorScreen:
    def __init__(self,window,frame):
        self.window = window
        self.frame = frame
        self.titleFrame=tkinter.LabelFrame(self.frame,text="TUTORS ACTIONS",borderwidth=2, font=("Tahoma", 15),fg="black")
        self.titleFrame.grid(row=0,column=0,sticky="W", columnspan=10, padx=[10,0],pady=20,ipadx=[10])
        self.placeholderArray = ['','','','','']
        for i in range(0,5):
            self.placeholderArray[i]=tkinter.StringVar()
        self.categoryStudent = []
        self.categoryStudent1 = []
        self.studentArray=[]

        self.categoryArray=[]
        self.categoryArray1=[]
        self.quizz = Quizz().getQuizz()
        self.studentHasAnswer = StudentAnswer().getStudentByAnswerId1()
        self.quizzArray = []
        self.answerArray = []

        for student in self.studentHasAnswer:
            if(Student().getStudentById(student['student_id']) is not None):
                stud = Student().getStudentById(student['student_id'])
                self.studentArray.append(stud)
        for i in range(0, len(self.studentArray)):
            self.categoryStudent.append(self.studentArray[i]['name']+" "+self.studentArray[i]['surname'])
            self.categoryStudent1.append({'student_id':self.studentArray[i]['student_id'], 'student_name':self.studentArray[i]['name']+" "+self.studentArray[i]['surname']})
        
        self.questionLabel=Label(self.titleFrame,text="Select Question",anchor="e",width=15,font=("Tahoma", 15))
        self.questionCombo=ttk.Combobox(self.titleFrame,width=68,textvariable=self.placeholderArray[1],values=self.categoryArray,font=('Verdana',15))

        self.studentLabel=Label(self.titleFrame,text="Select Student",anchor="e",width=15,font=("Tahoma", 15))
        self.studentCombo=ttk.Combobox(self.titleFrame,width=68,textvariable=self.placeholderArray[2],values=self.categoryStudent,font=('Verdana',15))

        self.logoutBtn=Button(self.titleFrame,text="DISCONNECT",width=25,borderwidth=3,bg=btnColor,fg='white',height=2,command=self.disconnectTutor, cursor="hand2")
        self.placeholderCorrectArray = ['','']
        for i in range(0,1):
            self.placeholderCorrectArray[i]=IntVar()

        self.saveBtn=Button(self.titleFrame,text="SAVES",width=25,borderwidth=3,fg='black',height=2,command=self.save,cursor="hand2")

        self.isCorrect1=Checkbutton(self.titleFrame,width=2, 
                                   variable=self.placeholderCorrectArray[0],
                                   onvalue=1, offvalue=0)
        
        self.answerText1Label=Label(self.titleFrame,text="Answer",anchor="e",width=15,font=("Tahoma", 15))
        self.answerText1Label.grid(row=5,column=1,padx=0)
        self.answerText1Entry=Entry(self.titleFrame,width=68,textvariable=self.placeholderArray[0], font=('Verdana',15))
        self.answerText1Entry.grid(row=5,column=2,padx=0,pady=10)
        self.isCorrect1.grid(row=5,column=3,padx=0,pady=2)
        self.saveBtn.grid(row=6,column=2,padx=0,pady=2)


        self.questionLabel.grid(row=1,column=1,padx=[10,0],pady=5)
        self.questionCombo.grid(row=1,column=2,padx=5,pady=2)
        self.studentLabel.grid(row=0, column=1,padx=5,pady=2)
        self.studentCombo.grid(row=0, column=2,padx=5,pady=2)
        self.logoutBtn.grid(row=0,column=3,padx=[10,0],pady=5)

        self.studentCombo.bind("<<ComboboxSelected>>", self.loadQuestion)
        self.questionCombo.bind("<<ComboboxSelected>>", self.loadAnswer)

    def save(self):
        try:
            student_id = int(self.getStudentId())
            answer_id = 0
            correct = ""
            answer_text = str(self.answerText1Entry.get())
            is_correct = self.placeholderCorrectArray[0].get()
            if(is_correct == 0):
                correct = "is_false"
            else:
                correct = "is_true"
            for answer in self.categoryArray1:
                if(answer_text == answer['question_answer']):
                    answer_id = answer['answer_id']
            print(student_id, answer_id,correct, answer_text, is_correct)
            StudentAnswer(student_fkid=student_id, answer_fkid=answer_id, answer_text_fk=answer_text, is_correct=correct).updateStudentAnswer()     
            print("student : ")
        except:
            messagebox.showwarning("", "An error occured please try again")
            return

    def loadQuestion(self,event):
            self.question = Question().getQuestionByStudent(self.getStudentId())
            self.categoryArray = []
            self.categoryArray1 = []
            self.placeholderArray[1].set('')
            if(self.question is not None):
                for question in self.question:
                    self.categoryArray.append(question['question_text'])
                    self.categoryArray1.append({'answer_id':question['answer_fkid'],'question_text':question['question_text'], 'question_answer':question['answer_text_fk']})
            self.questionCombo["values"] = self.categoryArray

    def loadAnswer(self, event):
        print(self.categoryArray1)
        answer = ""
        for answ in self.categoryArray1:
            if(self.questionCombo.get() == answ['question_text']):
                answer = answ['question_answer']
        self.placeholderArray[0].set(answer)


    
    def getStudentId(self):
        for cat1 in self.categoryStudent1:
            if(self.studentCombo.get() == cat1['student_name']):
                return cat1['student_id']
        
    def disconnectTutor(self):
        frame3.pack_forget()
        frame1.pack()
        controlPrivileges()











class QuizScreen:
    def __init__(self,window,frame,quiz,sname,sid,quiz_id):
        self.window = window
        self.frame = frame
        self.quizz = quiz
        self.sname = sname
        self.sid = sid
        self.quiz_id = quiz_id
        self.image = Image.open("C:/Users/pc/Documents/projetPython/frontendQuizz/view/imgquizz.png")
        self.bg = ImageTk.PhotoImage(self.image)
        self.canvas = Canvas(self.frame, width=1500, height=900, bg="#d0d2d6")
        self.canvas.grid(row=0, column=0, rowspan=200, columnspan=1000)
        self.canvas.create_image(0, 0, anchor=NW, image=self.bg)
        self.placeholderCorrectArray = ['','','','','','']
        for i in range(0,6):
            self.placeholderCorrectArray[i]=IntVar()
        self.questions1 = Question().getQuestion()
        self.questions = []
        self.options = []
        self.dict_questions = {}
        self.placeholderArray = []
        self.questions1 = Question().getQuestionByQuizId(self.quiz_id)
        self.opts = None
        self.dictQroQuestion = {}
        self.arrayAnswerDict = {}
        for question1 in self.questions1:
            answer = Answer().getAnswerByQuestionId(question1["id"])
            if(question1['question_type'] == 'Q.R.O'):
                self.dictQroQuestion[f"{question1["question_text"]}"] = answer[0]['id']
                self.placeholderArray.append('')
                answer = ""
            if(isinstance(answer,list) or question1['question_type'] == "Q.R.O"):
                self.dict_questions[f"{question1["question_text"]}"] = answer
        for key,value in self.dict_questions.items():
            self.questions.append(key)
            self.options.append(value)

        self.answerQroEntry=Entry(self.frame,width=65,font=('Verdana',25)) 
        for i in range(0,len(self.placeholderArray)):
            self.placeholderArray[i]=tkinter.StringVar()
            self.answerQroEntry['textvariable'] = self.placeholderArray[i]
        self.vArray = []
        self.v1 = IntVar(self.frame)
        self.vArray.append(self.v1)
        self.v2 = IntVar(self.frame)
        self.vArray.append(self.v2)
        self.v3 = IntVar(self.frame)
        self.vArray.append(self.v3)
        self.v4 = IntVar(self.frame)
        self.vArray.append(self.v4)
        self.v5 = IntVar(self.frame)
        self.vArray.append(self.v5)
        self.v6 = IntVar(self.frame)
        self.vArray.append(self.v6)
        
        self.titleFrame = LabelFrame(self.frame,text=str(self.sname).upper(),fg="black" ,font=('BahnschriftLight', 15),borderwidth=2,bg="white")
        self.canvas.create_window(0,0, anchor="w", window=self.titleFrame)
       
        self.title = Label(self.titleFrame, height=1, fg="black", font=('BahnschriftLight', 15), text="Quiz Title: "+self.quizz, wraplength=500,)
        self.disconnect = Button(self.titleFrame,text="DISCONNECT",width=20,borderwidth=3, height=2, bg=btnColor, fg='black',command=self.disconnectStudent,cursor="hand2")
        self.radioArray = []
        self.question_label = Label(self.frame, height=5, width=80, fg="black", font=('Verdana', 20), text="hgvcg", wraplength=500, bg='#ddd')
        self.option1 =  Checkbutton(self.frame,width=149, bg="#fff",
                                   height=2,cursor="hand2", 
                                   font=('BahnschriftLight', 13),fg="black" ,
                                   activeforeground="darkgreen",highlightthickness=0,takefocus=0,
                                   command=lambda:self.checkAnswer(self.option1,0),
                                   variable=self.v1,
                                   onvalue=1, offvalue=0)
        self.radioArray.append(self.option1)
        self.option2 =  Checkbutton(self.frame,width=149, bg="#fff",
                                   height=2,cursor="hand2",command=lambda:self.checkAnswer(self.option2,1),
                                   variable=self.v2,font=('BahnschriftLight', 13),fg="black",
                                   activeforeground="darkgreen",highlightthickness=0,takefocus=0,
                                   onvalue=1, offvalue=0)
        self.radioArray.append(self.option2)
        self.option3 =  Checkbutton(self.frame,width=149, bg="#fff",
                                   height=2,cursor="hand2", command=lambda:self.checkAnswer(self.option3,2),
                                   variable=self.v3,font=('BahnschriftLight', 13),fg="black",
                                   activeforeground="darkgreen",highlightthickness=0,takefocus=0,
                                   onvalue=1, offvalue=0)
        self.radioArray.append(self.option3)
        self.option4 =  Checkbutton(self.frame,width=149, bg="#fff",
                                   height=2,cursor="hand2", command=lambda:self.checkAnswer(self.option4,3),
                                   variable=self.v4,font=('BahnschriftLight', 13),fg="black",
                                   activeforeground="darkgreen",highlightthickness=0,takefocus=0,
                                   onvalue=1, offvalue=0)
        self.radioArray.append(self.option4)
        self.option5 =  Checkbutton(self.frame,width=149, bg="#fff",
                                   height=2,cursor="hand2",  command=lambda:self.checkAnswer(self.option5,4),
                                   variable=self.v5,font=('BahnschriftLight', 13),fg="black",
                                   onvalue=1, offvalue=0)
        self.radioArray.append(self.option5)
        self.option6 =  Checkbutton(self.frame,width=149, bg="#fff",
                                   height=2,cursor="hand2", command=lambda:self.checkAnswer(self.option6,5),
                                   variable=self.v6,font=('BahnschriftLight', 13),fg="black",
                                   activeforeground="darkgreen",highlightthickness=0,takefocus=0,
                                   onvalue=1, offvalue=0)
        self.radioArray.append(self.option6)

      
        self.btn_next = Button(self.frame, text="Next",cursor="hand2",bg=btnColor, width=25, font=("Verdana", 15), command=self.displayNextQuestion)
        self.frame.pack(fill="both", expand="true")
        self.titleFrame.grid(row=0, column=0,padx=[0,0], pady=[2,2], columnspan=10)
        self.title.grid(row=0,column=0,padx=[0,450], pady=[5,0])
        self.disconnect.grid(row=0,column=1, padx=[500,5],pady=[5,0])
        self.question_label.grid(row=1, column=0,pady=[5,25])

        self.option1.grid(sticky="W", row=2, column=0, pady=2)
        self.option2.grid(sticky="W", row=3, column=0, pady=2)
        self.option3.grid(sticky="W", row=4, column=0, pady=2)
        self.option4.grid(sticky="W", row=5, column=0, pady=2)
        self.option5.grid(sticky="W", row=6, column=0, pady=2)
        self.option6.grid(sticky="W", row=7, column=0, pady=2)
       
        self.btn_next.grid(row=8, column=0,pady=[10,0])
        self.displayNextQuestion()
        print(self.correct)


    def displayOption(self):
        if(isinstance(self.options[self.index], list)):
            self.opts = self.options[self.index]
        else:
            self.opts = []
        if(len(self.opts) != 0):
            for i in range(0,6):
                rows = 2
                if i==0:
                    rows=2
                elif i==1:
                    rows=3
                elif i==2:
                    rows=4
                elif i==3:
                    rows=5
                elif i==4:
                    rows=6
                elif i==5:
                    rows=7
                if(self.opts[i]['answer_text'] != ""):
                    self.radioArray[i].grid(sticky="W", row=rows, column=0, pady=10)
                    self.radioArray[i]['text'] = self.opts[i]['answer_text']
                    self.vArray[i].set(self.opts[i]['answer_text'])
                else:
                    self.radioArray[i].grid_forget()
        else:
            for i in range(0,len(self.radioArray)):
                self.radioArray[i].grid_forget()
            self.answerQroEntry.grid(sticky="W", row=2, column=0, columnspan=25, pady=10)
    index = 0
    correct = 0
    lenCheck = 0
    correct1 = 0

    def disconnectStudent(self):
        frame2.pack_forget()
        frame1.pack()
        controlPrivileges()

    def disableButton(self, state):
        self.option1['state'] = state
        self.option2['state'] = state
        self.option3['state'] = state
        self.option4['state'] = state
        self.option5['state'] = state
        self.option6['state'] = state

    def checkAnswer(self,radio,id):
        global correct, index, lenCheck
        self.lenCheck += 1
        if(self.lenCheck == 2):
            self.disableButton('disable')
        for option in self.options[self.index]:
            if radio['text'] == option['answer_text']:
                if self.vArray[id].get() == 1:
                    self.arrayAnswerDict[f"{option['answer_text']}"] = option['id']
                    if option['is_correct'] == 1:
                        self.correct += 1

    def resetPlaceholder(self):
        for i in range(0,len(self.placeholderArray)): 
                self.placeholderArray[i].set('')

    def displayNextQuestion(self):
        global correct, index, lenCheck, correct1
        op = ""
        st1Array = []
        studentAnswerArray = StudentAnswer().getStudentByAnswerId(self.sid)
        if(len(studentAnswerArray) != 0):
            print("ST ARRAY------- --- ",studentAnswerArray)
            for st in studentAnswerArray:
                print("ST------- --- ",st)
                st1 = StudentAnswer().getStudentAnswersById(self.sid, st['id'])
                st1Array.append(st1)
                if st['is_correct'] == 1 or st1['correct'] == "is_true":
                    self.correct1 += 1
            self.btn_next['state'] = 'disabled'
            for i in range(0, len(self.radioArray)):
                self.radioArray[i].grid_forget()
            print("ST1 ARRAY", st1Array)
            strr = []
            for str1 in st1Array:
                if(str1['answer_text_fk'] != "" and str1['correct'] is None):
                    strr.append(str1)
            if(len(strr) != 0):
                op = "Partial Result "
            else:
                op = "Final Result "
            result = op + str(self.correct1) + " / " + str(len(studentAnswerArray))+"\n"+str(round((((self.correct1)/len(studentAnswerArray))*100),2))+"%"

            self.question_label['text'] = result
            self.question_label['bg'] = 'green'
            self.btn_next['width'] = 20
            self.btn_next['text'] = 'Refresh'
            if self.correct1 >= len(studentAnswerArray)/2:
                self.question_label['bg'] = "green"
            else:
                self.question_label['bg'] = "red"
        else:
            print("Question Legnt ",len(self.questions), " INDEX: ", self.index)
            if(self.answerQroEntry.get() != '' or self.lenCheck == 2 or self.lenCheck == 1):
                if(len(self.questions) == self.index):
                    self.index  = 0
                if(self.options[self.index] == ""):
                    print("DICT QRO QUESTION :", self.dictQroQuestion);
                    for key,value in self.dictQroQuestion.items():
                        if(self.questions[self.index] == key):
                            self.arrayAnswerDict[f"Q.R.O-{self.answerQroEntry.get()}"] = value
                self.index += 1 
            if self.btn_next['text'] == 'Restart The Quiz':
                self.resetPlaceholder()
                self.correct = 0
                self.index = 0
                self.lenCheck = 0
                self.question_label['bg'] = '#ddd'
                self.btn_next['text'] = 'Next'

            if self.index == len(self.options):
                for key,value in self.arrayAnswerDict.items():
                    if(key.split("-")[0] == "Q.R.O"):
                        StudentAnswer(self.sid, value, key.split("-")[1], 0).createStudentsAnswers()
                    else:
                        StudentAnswer(self.sid, value, "", 0).createStudentsAnswers()
                self.resetPlaceholder()

                result = "Result: "+ str(self.correct) + " / " + str(len(self.options))+"\n"+str(round((((self.correct)/len(self.options))*100),2))+"%"
                for op in self.options:
                    if(op == ""):
                        result = "Partial "+result+"\n Please wait 24 hours for final results"
                        break
                self.question_label['text'] = result
                self.question_label['bg'] = 'green'
                self.btn_next['width'] = 20
                self.btn_next['text'] = 'Restart The Quiz'
                if self.correct >= len(self.options)/2:
                    self.question_label['bg'] = "green"
                else:
                    self.question_label['bg'] = "red"

            else:
                self.lenCheck = 0
                self.question_label['text'] = self.questions[self.index]
                self.disableButton('normal')
                self.displayOption()

                if self.index == len(self.options)-1:
                    self.btn_next['text'] = 'Save'
                self.resetPlaceholder()



async def main():
   controlPrivileges()
   window.resizable(False,False)
   window.mainloop()
   
if __name__ == "__main__":
   asyncio.run(main())