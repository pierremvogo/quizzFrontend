from tkinter import NO, W, Button, Checkbutton, Entry, IntVar, Label, messagebox, ttk
import tkinter
from api.answer import Answer
from api.question import Question
from api.quizz import Quizz
from api.student import Student
from api.answer import Answer
from api.student_answer import StudentAnswer


class ManageAnswer:
    def __init__(self,windowanswer,frameanswer,btnColor, style):
        self.btnColor = btnColor
        self.windowanswer = windowanswer
        self.frameanswer = frameanswer
        self.style = style
        self.placeholderArray = ['','','','','','','','']
        self.offset = 0

        for i in range(0,7):
            self.placeholderArray[i]=tkinter.StringVar()

        self.categoryArray=[]
        self.categoryArray1=[]

        self.isCorrectArrays=[]
        self.answerTextArrays=[]
        self.placeholderCorrectArray = ['','','','','','']
        for i in range(0,6):
            self.placeholderCorrectArray[i]=IntVar()
        
        self.categoryQuizArray=[]
        self.categoryQuizArray1=[]
        self.quizz = Quizz().getQuizz()
        for quizz in self.quizz:
            self.categoryQuizArray.append(quizz['title'])
            self.categoryQuizArray1.append({'quizz_id':quizz['id'], 'quizz_title':quizz['title']})

        self.listFrameAnswer=tkinter.LabelFrame(self.frameanswer,text="LIST OF ANSWER",borderwidth=5,font=("Tahoma", 15),fg="black")
        self.listFrameAnswer.grid(row=5,column=0,sticky="w",padx=[10,10],pady=[0,200],ipadx=[50])

        self.my_tree = ttk.Treeview(self.listFrameAnswer,selectmode='browse',show='headings',height=11, padding=5)
        self.my_tree.bind("<ButtonRelease-1>", self.select)

        self.entriesFrameAnswer = tkinter.LabelFrame(self.frameanswer,text="ANSWER",borderwidth=5, font=("Tahoma", 15),fg="black")
        self.entriesFrameAnswer.grid(row=1,column=0,sticky="w",padx=[10,290],pady=[0,20],ipadx=[2])

        self.countAnswer = 0
        ##self.countAnswerLabel=Label(self.entriesFrameAnswer,text=self.countAnswer,background="grey64",anchor="e",width=15,font=("Tahoma",15))
        
        self.quizComboLabel=Label(self.entriesFrameAnswer,text="Select Quiz",anchor="e",width=15)
        self.questionLabel=Label(self.entriesFrameAnswer,text="Select Question",anchor="e",width=15)
        self.isCorrect1=Checkbutton(self.entriesFrameAnswer,width=2, 
                                   variable=self.placeholderCorrectArray[0],
                                   onvalue=1, offvalue=0)
        self.isCorrectArrays.append(self.isCorrect1)
        self.isCorrect2=Checkbutton(self.entriesFrameAnswer,width=2, 
                                   variable=self.placeholderCorrectArray[1],
                                   onvalue=1, offvalue=0, )
        self.isCorrectArrays.append(self.isCorrect2)
        self.isCorrect3=Checkbutton(self.entriesFrameAnswer,width=2, 
                                   variable=self.placeholderCorrectArray[2],
                                   onvalue=1, offvalue=0, )
        self.isCorrectArrays.append(self.isCorrect3)
        self.isCorrect4=Checkbutton(self.entriesFrameAnswer,width=2, 
                                   variable=self.placeholderCorrectArray[3],
                                   onvalue=1, offvalue=0, )
        self.isCorrectArrays.append(self.isCorrect4)
        self.isCorrect5=Checkbutton(self.entriesFrameAnswer,width=2, 
                                   variable=self.placeholderCorrectArray[4],
                                   onvalue=1, offvalue=0,)
        self.isCorrectArrays.append(self.isCorrect5)
        self.isCorrect6=Checkbutton(self.entriesFrameAnswer,width=2, 
                                   variable=self.placeholderCorrectArray[5],
                                   onvalue=1, offvalue=0,)
        self.isCorrectArrays.append(self.isCorrect6)

        self.answerText1Label=Label(self.entriesFrameAnswer,text="Answer1",anchor="e",width=15)
        self.answerText1Label.grid(row=2,column=0,padx=0)
        self.answerText1Entry=Entry(self.entriesFrameAnswer,width=30,textvariable=self.placeholderArray[0], font=('Verdana',15))
        self.answerTextArrays.append(self.answerText1Entry)
        self.answerText1Entry.grid(row=2,column=1,padx=0,pady=2)
        self.isCorrect1.grid(row=2,column=2,padx=5,pady=2)

        self.answerText2Label=Label(self.entriesFrameAnswer,text="Answer2",anchor="e",width=15,)
        self.answerText2Label.grid(row=2,column=3,padx=0,columnspan=1)
        self.answerText2Entry=Entry(self.entriesFrameAnswer,width=30,textvariable=self.placeholderArray[1],font=('Verdana',15))
        self.answerTextArrays.append(self.answerText2Entry)
        self.answerText2Entry.grid(row=2,column=4,padx=0,pady=2)
        self.isCorrect2.grid(row=2,column=5,padx=5,pady=2)


        self.answerText3Label=Label(self.entriesFrameAnswer,text="Answer3",anchor="e",width=15,)
        self.answerText3Label.grid(row=3,column=0,padx=0)
        self.answerText3Entry=Entry(self.entriesFrameAnswer,width=30,textvariable=self.placeholderArray[2],font=('Verdana',15))
        self.answerTextArrays.append(self.answerText3Entry)
        self.answerText3Entry.grid(row=3,column=1,padx=0,pady=2)
        self.isCorrect3.grid(row=3,column=2,padx=5,pady=2)

        self.answerText4Label=Label(self.entriesFrameAnswer,text="Answer4",anchor="e",width=15, )
        self.answerText4Label.grid(row=3,column=3,padx=0)
        self.answerText4Entry=Entry(self.entriesFrameAnswer,width=30,textvariable=self.placeholderArray[3],font=('Verdana',15))
        self.answerTextArrays.append(self.answerText4Entry)
        self.answerText4Entry.grid(row=3,column=4,padx=0,pady=2)
        self.isCorrect4.grid(row=3,column=5,padx=5,pady=2)

        self.answerText5Label=Label(self.entriesFrameAnswer,text="Answer5",anchor="e",width=15, )
        self.answerText5Label.grid(row=4,column=0,padx=0)
        self.answerText5Entry=Entry(self.entriesFrameAnswer,width=30,textvariable=self.placeholderArray[4],font=('Verdana',15))
        self.answerTextArrays.append(self.answerText5Entry)
        self.answerText5Entry.grid(row=4,column=1,padx=0,pady=2)
        self.isCorrect5.grid(row=4,column=2,padx=5,pady=2)

        self.answerText6Label=Label(self.entriesFrameAnswer,text="Answer6",anchor="e",width=15, )
        self.answerText6Label.grid(row=4,column=3,padx=0)
        self.answerText6Entry=Entry(self.entriesFrameAnswer,width=30,textvariable=self.placeholderArray[5],font=('Verdana',15))
        self.answerTextArrays.append(self.answerText6Entry)
        self.answerText6Entry.grid(row=4,column=4,padx=0,pady=2)
        self.isCorrect6.grid(row=4,column=5,padx=5,pady=2)

        self.quizComboLabel.grid(row=0,column=0, padx=10)
        self.questionLabel.grid(row=1,column=0,padx=10)

    
        self.questionCombo=ttk.Combobox(self.entriesFrameAnswer,width=68,textvariable=self.placeholderArray[6],values=self.categoryArray,font=('Verdana',15))
        self.quizCombo=ttk.Combobox(self.entriesFrameAnswer,width=68,textvariable=self.placeholderArray[7],values=self.categoryQuizArray,font=('Verdana',15))

        self.questionCombo.grid(row=1,column=1,columnspan=5,padx=5,pady=2)
        self.quizCombo.grid(row=0,column=1,columnspan=5,padx=5,pady=2)
        ##self.countAnswerLabel.grid(row=1,column=6,padx=5,pady=2)

        
        self.questionCombo.bind("<<ComboboxSelected>>", self.displayCountAnswer)
        self.quizCombo.bind("<<ComboboxSelected>>", self.loadQuestion)

        self.manageActionAnswer=tkinter.LabelFrame(self.entriesFrameAnswer,text="ACTIONS ANSWER",borderwidth=5,font=("Tahoma", 15),fg="black")
        self.manageActionAnswer.grid(row=6,column=0,columnspan=70,rowspan=15,padx=[10,15],pady=1,ipadx=[5])

        self.saveBtn=Button(self.manageActionAnswer,text="SAVE",width=25,borderwidth=3,fg='black',height=2,command=self.save,cursor="hand2")
        self.updateBtn=Button(self.manageActionAnswer,text="UPDATE",width=25,borderwidth=3,fg='black',height=2,command=self.update,cursor="hand2")
        self.deleteBtn=Button(self.manageActionAnswer,text="DELETE",width=25,borderwidth=3,fg='black',height=2,command=self.delete,cursor="hand2")
        self.resetBtn=Button(self.manageActionAnswer,text="RESET",width=25,borderwidth=3,fg='black',height=2,command=self.reset,cursor="hand2")

        self.saveBtn.grid(row=0,column=0,padx=[490,10],pady=2)
        self.updateBtn.grid(row=0,column=1,padx=[5,10],pady=2)
        self.deleteBtn.grid(row=0,column=2,padx=[5,10],pady=2)
        self.resetBtn.grid(row=0,column=3,padx=[5,10],pady=2)

        self.style.configure(self.windowanswer)
        self.style.configure("Treeview.Heading", font=("Verdana", 12))
        self.style.configure("Treeview.Column", font=(None, 20))
        self.my_tree['columns']=("Answer Id","Answer Text","Is Correct","Question Id")
        self.my_tree.column("#0",width=0,stretch=NO)
        self.my_tree.column("Answer Id",anchor=W,width=120)
        self.my_tree.column("Answer Text",anchor=W,width=580)
        self.my_tree.column("Is Correct",anchor=W,width=200) 
        self.my_tree.column("Question Id",anchor=W,width=200)

        self.my_tree.heading("Answer Id",text="Answer Id",anchor=W)
        self.my_tree.heading("Answer Text",text="Answer Text",anchor=W)
        self.my_tree.heading("Is Correct",text="Is Correct",anchor=W)
        self.my_tree.heading("Question Id",text="Question Id",anchor=W)
        self.my_tree.tag_configure('orow',background="#EEEEEE")
        self.refreshTable()

        if(len(self.categoryQuizArray) != 0 and self.quizCombo.get() == ""):
            self.quizCombo.current(0)
            self.loadQuestion("")
        if(len(self.categoryArray) != 0 and self.questionCombo.get() == ""):
                self.questionCombo.current(0)
                self.countAnswer =  len(Answer().getAnswerByQuestionId(self.getQuestionId()))
                if(self.countAnswer <= 1):
                    self.countAnswer = 0
                    self.saveBtn['state']='active'
                else:
                    self.saveBtn['state']='disabled'
                    for i in range(0,self.countAnswer):
                        self.placeholderArray[i].set(Answer().getAnswerByQuestionId(self.getQuestionId())[i]["answer_text"])
                #self.countAnswerLabel['text'] = str(self.countAnswer)+" answers"


    def displayCountAnswer(self,event):
            self.countAnswer = len(Answer().getAnswerByQuestionId(self.getQuestionId()))
            if(self.countAnswer <= 1):
                    self.countAnswer = 0
                    self.saveBtn['state']='active'
            else:
                self.saveBtn['state']='disabled'
            #self.countAnswerLabel['text'] = str(self.countAnswer)+" answers"
            print("COUNT:", self.countAnswer)
            for num in range(0,6):
                self.placeholderArray[num].set('')
            if(self.countAnswer > 1):
                for i in range(0,self.countAnswer):
                    self.placeholderArray[i].set(Answer().getAnswerByQuestionId(self.getQuestionId())[i]["answer_text"])

    def loadQuestion(self,event):
            self.countAnswer = 0
            #self.countAnswerLabel['text'] = str(self.countAnswer)+" answers"
            for num in range(0,6):
                self.placeholderArray[num].set('')
            self.question = Question().getQuestionByQuizIdAndType(self.getQuizId(),"Q.C.M")
            self.categoryArray = []
            self.categoryArray1 = []
            self.placeholderArray[6].set('')
            if(isinstance(self.question, list)):
                for question in self.question:
                    self.categoryArray.append(question['question_text'])
                    self.categoryArray1.append({'question_id':question['id'], 'question_text':question['question_text']})
            self.questionCombo["values"] = self.categoryArray
            
         

    def setph(self,word,num):
        for ph in range(0,7):
            if ph == num:
                self.placeholderArray[ph].set(word)
            
    def setph1(self,word,num):
        for ph in range(0,6):
            if ph == num:
                self.placeholderCorrectArray[ph].set(word)

    def reset(self):
        self.saveBtn['state']='active'
        for num in range(0,7):
            self.setph('',(num))
        for num in range(0,6):
            self.setph1(0,(num))
               
    def getQuizId(self):
        for cat1 in self.categoryQuizArray1:
            if(self.quizCombo.get() == cat1['quizz_title']):
                return cat1['quizz_id']
    def getQuestionId(self):
        for cat1 in self.categoryArray1:
            if(self.questionCombo.get() == cat1['question_text']):
                return cat1['question_id']
    def save(self):
        try:
            self.countAnswer = len(Answer().getAnswerByQuestionId(self.getQuestionId()))
            if(self.countAnswer < 6):
                for i in range(0,len(self.answerTextArrays)):
                    question_id=int(self.getQuestionId())
                    answer_text=str(self.answerTextArrays[i].get())
                    is_correct = self.placeholderCorrectArray[i].get()
                    valid=True
                    if  not(question_id):
                        messagebox.showwarning("","Please fill up all entries")
                        return
                    Answer(answer_text,is_correct,question_id).createAnswer()
                    self.countAnswer = len(Answer().getAnswerByQuestionId(self.getQuestionId()))
                    #self.countAnswerLabel['text'] = str(self.countAnswer)+" answers"
                for num in range(0,7):
                        self.setph('',(num))
                for num in range(0,6):
                        self.setph1(0,(num))
                self.refreshTable()
            else:
                messagebox.showwarning("", "This question have the maximum anwser")
                return
        except:
            messagebox.showwarning("", "This question have the maximum anwser")
            return

    def update(self):
        try:
            countAnswer1 = Answer().getAnswerByQuestionId(self.getQuestionId())
            for i in range(0,len(countAnswer1)):
                question_id=int(self.getQuestionId())
                answer_text=str(self.answerTextArrays[i].get())
                is_correct = self.placeholderCorrectArray[i].get()
                answerId = int(Answer().getAnswerByQuestionId(self.getQuestionId())[i]['id'])
                valid=True
                Answer(answer_text,is_correct,question_id).updateAnswer(answerId)
                self.countAnswer = len(countAnswer1)
                #self.countAnswerLabel['text'] = str(self.countAnswer)+" answers"
            for num in range(0,7):
                if num == 6:
                    continue
                self.setph('',(num))
            for num in range(0,6):
                        self.setph1(0,(num))
            for i in range(0,self.countAnswer):
                self.placeholderArray[i].set(Answer().getAnswerByQuestionId(self.getQuestionId())[i]["answer_text"])
            self.refreshTable()
        except:
            messagebox.showwarning("", "An error occured !")
            return

    def select(self,event):
        try:
            self.saveBtn['state']='disabled'
            selectedItem = self.my_tree.selection()[0]
            answer_text = str(self.my_tree.item(selectedItem)['values'][1])
            question_id = str(self.my_tree.item(selectedItem)['values'][3])
            is_correct =  int(self.my_tree.item(selectedItem)['values'][2])
            question_text = Question().getQuestionById(question_id)["question_text"]
            self.setph(answer_text,0)
            self.setph(question_text,6)
            self.setph1(is_correct,0)
            self.countAnswer = len(Answer().getAnswerByQuestionId(question_id))
            #self.countAnswerLabel['text'] = str(self.countAnswer)+" answers"
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
                        StudentAnswer().deleteStudentAnswer(itemId, s)
                        Answer().deleteAnswer(itemId)
                        messagebox.showinfo("","Data has been successfully deleted")
                        for num in range(0,7):
                            self.setph('',(num))
                        self.saveBtn['state']='active'
                        self.refreshTable()
                    except:
                        messagebox.showinfo("","Sorry, an error occured")
                        return
                    self.countAnswer = 0
                    #self.countAnswerLabel['text'] = str(self.countAnswer)+" answers"
                    self.refreshTable()
        except:
            messagebox.showwarning("", "Please select a data row")


    def read(self,offset):
        results =  Answer().getAnswersByPagination(offset)
        print(results)
        return results
    
    def refreshTable(self, offset = 0):
        no_recquestion =  Answer().countAnswer()[0]['COUNT(*)']
        for data in self.my_tree.get_children():
            self.my_tree.delete(data)
        for array in self.read(offset):
            self.my_tree.insert(parent='',index='end',iid=array['id'],text="",values=(
                array['id'], 
                array['answer_text'],
                array['is_correct'],
                array['question_id']),tag="orow")
        self.my_tree.tag_configure('orow',background="#EEEEEE")
        self.my_tree.grid(row=0, column=4, pady=[10,5])
        back = offset - 10
        next = offset + 10
        b1=Button(self.listFrameAnswer,text="< Prev",command=lambda:self.refreshTable(back),width=10, height=1)
        b2=Button(self.listFrameAnswer,text="Next >",command=lambda:self.refreshTable(next),width=10, height=1)
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
                   
        