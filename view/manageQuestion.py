from tkinter import NO, W, Button, Entry, Label, messagebox, ttk
import tkinter
from api.answer import Answer
from api.question import Question
from api.quizz import Quizz


class ManageQuestion:
    def __init__(self,windowquestion,framequestion,btnColor, style):
        self.btnColor = btnColor
        self.windowquestion = windowquestion
        self.framequestion = framequestion
        self.style = style
        self.placeholderArray = ['','','','','']
        self.offset = 0
        for i in range(0,5):
            self.placeholderArray[i]=tkinter.StringVar()
        self.typeQuestionArray=["Q.R.O","Q.C.M"]
        self.categoryArray=[]
        self.categoryArray1=[]
        self.quizz = Quizz().getQuizz()
        print("ALL QUIIZ DATA: ",self.quizz)

        for quizz in self.quizz:
            self.categoryArray.append(quizz['title'])
            self.categoryArray1.append({'quizz_id':quizz['id'], 'quizz_title':quizz['title']})

        self.listFrameQuestion=tkinter.LabelFrame(self.framequestion,text="LIST OF QUESTION",borderwidth=5,font=("Tahoma", 15),fg="black")
        self.listFrameQuestion.grid(row=5,column=0,sticky="w",padx=[10,10],pady=[0,200],ipadx=[50])

        self.my_tree = ttk.Treeview(self.listFrameQuestion,selectmode='browse',show='headings',height=11, padding=5, )
        self.my_tree.bind("<ButtonRelease-1>", self.select,)

        self.entriesFrameQuestion = tkinter.LabelFrame(self.framequestion,text="QUESTION",borderwidth=5,font=("Tahoma", 17),fg="black")
        self.entriesFrameQuestion.grid(row=1,column=0,sticky="w",padx=[10,200],pady=[0,20],ipadx=[2])

        self.questionTextLabel=Label(self.entriesFrameQuestion,text="Question Text",anchor="e",width=15,font=("Tahoma", 15))
        self.quizLabel=Label(self.entriesFrameQuestion,text="Select Quizz",anchor="e",width=15,font=("Tahoma", 15))
        self.typeOfQuestionLabel=Label(self.entriesFrameQuestion,text="Type of Question",anchor="e",width=15,font=("Tahoma", 15))

        self.countQuestion = 0
        self.countQuestionLabel=Label(self.entriesFrameQuestion,text=self.countQuestion,background="grey64",anchor="e",width=15,font=("Tahoma",15))
                          
        self.questionTextLabel.grid(row=2,column=0,padx=[110,5])
        self.quizLabel.grid(row=0,column=0,padx=[110,5])
        self.typeOfQuestionLabel.grid(row=1,column=0,padx=[110,5])
        self.countQuestionLabel.grid(row=0,column=3,padx=5,pady=5)

        self.questionTextEntry=Entry(self.entriesFrameQuestion,width=47,font=("Verdana", 15),textvariable=self.placeholderArray[0])
        self.categoryCombo=ttk.Combobox(self.entriesFrameQuestion,width=45,font=("Verdana", 15),textvariable=self.placeholderArray[1],values=self.categoryArray)
        self.typeQuestionCombo=ttk.Combobox(self.entriesFrameQuestion,width=45,font=("Verdana", 15),textvariable=self.placeholderArray[2],values=self.typeQuestionArray)
       
        self.questionTextEntry.grid(row=2,column=2,padx=5,pady=5)
        self.categoryCombo.grid(row=0,column=2,padx=5,pady=5)
        self.typeQuestionCombo.grid(row=1,column=2,padx=5,pady=5)
        if(self.typeQuestionCombo.get() == ""):
            self.typeQuestionCombo.current(0)
        if(len(self.categoryArray) != 0 and self.categoryCombo.get() == ""):
                self.categoryCombo.current(0)
                self.countQuestion = len(Question().getQuestionByQuizId(self.getQuizId()))
                if(self.countQuestion < 2):
                    self.countQuestion = 0
                self.countQuestionLabel['text'] = str(self.countQuestion)+" questions"
        self.categoryCombo.bind("<<ComboboxSelected>>", self.displayCountQuestion)

        self.manageActionQuestion=tkinter.LabelFrame(self.entriesFrameQuestion,text="ACTIONS QUESTION",borderwidth=5,font=("Tahoma", 15),fg="black")
        self.manageActionQuestion.grid(row=6,column=0,columnspan=70,rowspan=15,padx=[10,15],pady=20,ipadx=[5])

        self.saveBtn=Button(self.manageActionQuestion,text="SAVE",width=25,borderwidth=3,fg='black',height=2,command=self.save,cursor="hand2")
        self.updateBtn=Button(self.manageActionQuestion,text="UPDATE",width=25,borderwidth=3,fg='black',height=2,command=self.update,cursor="hand2")
        self.deleteBtn=Button(self.manageActionQuestion,text="DELETE",width=25,borderwidth=3,fg='black',height=2,command=self.delete,cursor="hand2")
        self.resetBtn=Button(self.manageActionQuestion,text="RESET",width=25,borderwidth=3,fg='black',height=2,command=self.reset,cursor="hand2")

        self.saveBtn.grid(row=0,column=0,padx=[490,10],pady=5)
        self.updateBtn.grid(row=0,column=1,padx=[5,10],pady=5)
        self.deleteBtn.grid(row=0,column=2,padx=[5,10],pady=5)
        self.resetBtn.grid(row=0,column=3,padx=[5,10],pady=5)

        self.style.configure(self.windowquestion)
        self.style.configure("Treeview.Heading", font=("Verdana", 12))
        self.style.configure("Treeview.Column", font=(None, 20))
        self.my_tree['columns']=("Question Id","Question Text","Question Type","Quizz Id")
        self.my_tree.column("#0",width=0,stretch=NO)
        self.my_tree.column("Question Id",anchor=W,width=200)
        self.my_tree.column("Question Text",anchor=W,width=750)
        self.my_tree.column("Question Type",anchor=W,width=250)
        self.my_tree.column("Quizz Id",anchor=W,width=90) 

        self.my_tree.heading("Question Id",text="Question Id",anchor=W)
        self.my_tree.heading("Question Text",text="Question Text",anchor=W)
        self.my_tree.heading("Question Type",text="Question Type",anchor=W)
        self.my_tree.heading("Quizz Id",text="Quizz Id",anchor=W)
        self.my_tree.tag_configure('orow',background="#EEEEEE")
        self.refreshTable()
         
    def displayCountQuestion(self,event):
            self.countQuestion = len(Question().getQuestionByQuizId(self.getQuizId()))
            if(self.countQuestion < 2):
                    self.countQuestion = 0
            self.countQuestionLabel['text'] = str(self.countQuestion)+" questions"

    def setph(self,word,num):
        for ph in range(0,5):
            if ph == num:
                self.placeholderArray[ph].set(word)
    def getQuizId(self):
        for cat1 in self.categoryArray1:
            if(self.categoryCombo.get() == cat1['quizz_title']):
                return cat1['quizz_id']
    def resetQuestionCombo(self, event):
        self.placeholderArray[0].set('')
    def save(self):
        question_text=str(self.questionTextEntry.get())
        question_type=str(self.typeQuestionCombo.get())
        if self.getQuizId() != None:
            quizz_id=int(self.getQuizId())
        valid=True
        if  not(question_text) or not(quizz_id):
            messagebox.showwarning("","Please fill up all entries")
            return
        if(question_type == "Q.R.O"):
           question_id =  Question(question_text,question_type,quizz_id).createQuestion()['id']
           Answer("",0,question_id).createAnswer()
        Question(question_text,question_type,quizz_id).createQuestion()
        self.countQuestion = len(Question().getQuestionByQuizId(self.getQuizId()))
        self.countQuestionLabel['text'] = str(self.countQuestion)+" questions"
        for num in range(0,5):
                if num == 0:
                 self.setph('',(num))
        self.refreshTable()

    def update(self):
        selectedItemId = ''
        try:
            selectedItem = self.my_tree.selection()[0]
            selectedItemId = str(self.my_tree.item(selectedItem)['values'][0])
        except:
            messagebox.showwarning("", "Please select quizz on the table")
            return
        print(selectedItemId)
        question_text=str(self.questionTextEntry.get())
        question_type=str(self.typeQuestionCombo.get())
        quizz_id=str(self.getQuizId())
        valid=True
        if  not(question_text) or not(quizz_id):
            messagebox.showwarning("","Please fill up all entries")
            return
        if(question_type == "Q.R.O"):
            answer = Answer().getAnswerByQuestionId(selectedItemId)[0]
            Answer("",0,selectedItemId).updateAnswer(answer['id'])
        Question(question_text,question_type,quizz_id).updateQuestion(selectedItemId)
        self.setph('',0)
        self.saveBtn['state']='active'
        self.refreshTable()

    def select(self,event):
        try:
            self.saveBtn['state']='disabled'
            selectedItem = self.my_tree.selection()[0]
            question_id = str(self.my_tree.item(selectedItem)['values'][0])
            question_text = str(self.my_tree.item(selectedItem)['values'][1])
            quizz_id = str(self.my_tree.item(selectedItem)['values'][3])
            question_type = str(self.my_tree.item(selectedItem)['values'][2])
            quizz_text = Quizz().getQuizzById(quizz_id)["title"]
            countAnswer = len(Answer().getAnswerByQuestionId(question_id))
            self.setph(question_text,0)
            self.setph(quizz_text,1)
            self.setph(question_type,2)
            self.countQuestion = len(Question().getQuestionByQuizId(quizz_id))
            self.countQuestionLabel['text'] = str(self.countQuestion)+" questions"
        except:
            messagebox.showwarning("", "Please select a data row--------")
            return

    def delete(self):
        try:
            if(self.my_tree.selection()[0]):
                decision = messagebox.askquestion("", "Delete this question?")
                if(decision != 'yes'):
                    return
                else:
                    selectedItem = self.my_tree.selection()[0]
                    itemId = str(self.my_tree.item(selectedItem)['values'][0])
                    try:
                        if(len(Answer().getAnswerByQuestionId(itemId)) != 0):
                            for i in Answer().getAnswerByQuestionId(itemId):
                                answerId = i['id']
                                Answer().deleteAnswer(answerId)
                        Question().deleteQuestion(itemId)
                        messagebox.showinfo("","Data has been successfully deleted")
                        self.typeQuestionCombo.current(0)
                        self.setph('',0)
                        self.refreshTable()
                    except:
                        messagebox.showinfo("","Sorry, an error occured")
                        return
                    self.countQuestion = len(Question().getQuestionByQuizId(self.getQuizId()))
                    self.countQuestionLabel['text'] = str(self.countQuestion)+" questions"
                    self.saveBtn['state']='active'
                    self.deleteBtn['state']='active'
                    self.refreshTable()
        except:
            messagebox.showwarning("", "Please select a data row")
                
    def read(self,offset):
        results =  Question().getQuestionsByPagination(offset)
        print(results)
        return results
    
    def refreshTable(self, offset = 0):
        no_recquestion =  Question().countQuestion()[0]['COUNT(*)']
        for data in self.my_tree.get_children():
            self.my_tree.delete(data)
        for array in self.read(offset):
            self.my_tree.insert(parent='',index='end',iid=array['id'],text="",values=(
                array['id'], 
                array['question_text'],
                array['question_type'],
                array['quiz_id']),tag="orow")
        self.my_tree.tag_configure('orow',background="#EEEEEE")
        self.my_tree.grid(row=0, column=4, pady=[10,5])
        back = offset - 10
        next = offset + 10
        b1=Button(self.listFrameQuestion,text="< Prev",command=lambda:self.refreshTable(back),width=10, height=1)
        b2=Button(self.listFrameQuestion,text="Next >",command=lambda:self.refreshTable(next),width=10, height=1)
        b1.grid(row=6, column=0, columnspan=10, rowspan=5,sticky="w",padx=[1145,10],pady=[0,20],)
        b2.grid(row=7, column=0, columnspan=10, rowspan=5, sticky="W",padx=[1235,10],pady=[0,20])
        print(back)
        print(next)
        if (no_recquestion <= next):
            b2['state']='disabled'
        else:
            b2['state']='active'
        if (back >= 0):
            b1['state']='active'
        else:
            b1['state']='disabled'

    def setph(self,word,num):
            for ph in range(0,5):
                if ph == num:
                    self.placeholderArray[ph].set(word)
    def reset(self):
        self.saveBtn['state']='active'
        self.deleteBtn['state']='active'
        for num in range(0,5):
            self.setph('',(num))

       