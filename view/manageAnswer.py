from tkinter import NO, W, Button, Checkbutton, Entry, IntVar, Label, messagebox, ttk
import tkinter
from api.answer import Answer
from api.question import Question
from api.student import Student
from api.answer import Answer


class ManageAnswer:
    def __init__(self,windowanswer,frameanswer,btnColor, style):
        self.btnColor = btnColor
        self.windowanswer = windowanswer
        self.frameanswer = frameanswer
        self.style = style
        self.placeholderArray = ['','','','','']
        self.offset = 0
        for i in range(0,5):
            self.placeholderArray[i]=tkinter.StringVar()

        self.categoryArray=[]
        self.categoryArray1=[]

        self.categoryArrays=[]
        self.categoryArrays1=[]

        self.CheckIscorrect = IntVar()

        self.question = Question().getQuestion()
        self.student = Student().getStudents()
        for question in self.question:
            self.categoryArray.append(question['question_text'])
            self.categoryArray1.append({'question_id':question['id'], 'question_text':question['question_text']})

        self.listFrameAnswer=tkinter.LabelFrame(self.frameanswer,text="LIST OF ANSWER",borderwidth=5)
        self.listFrameAnswer.grid(row=5,column=0,sticky="w",padx=[10,10],pady=[0,200],ipadx=[50])

        self.my_tree = ttk.Treeview(self.listFrameAnswer,selectmode='browse',show='headings',height=5, padding=5)
        self.my_tree.bind("<ButtonRelease-1>", self.select)

        self.entriesFrameAnswer = tkinter.LabelFrame(self.frameanswer,text="ANSWER",borderwidth=5)
        self.entriesFrameAnswer.grid(row=1,column=0,sticky="w",padx=[10,200],pady=[0,20],ipadx=[2])

        self.answerTextLabel=Label(self.entriesFrameAnswer,text="Answer Text",anchor="e",width=15)
        self.isCorrectLabel=Label(self.entriesFrameAnswer,text="Is Correct",anchor="e",width=15)
        self.questionLabel=Label(self.entriesFrameAnswer,text="Select Question",anchor="e",width=15)

        self.answerTextLabel.grid(row=1,column=0,padx=10)
        self.isCorrectLabel.grid(row=2,column=0,padx=10)
        self.questionLabel.grid(row=0,column=0,padx=10)

        self.answerTextEntry=Entry(self.entriesFrameAnswer,width=50,textvariable=self.placeholderArray[0])
        self.isCorrect=Checkbutton(self.entriesFrameAnswer,width=50, 
                                   variable=self.CheckIscorrect,
                                   onvalue=1, offvalue=0)
        self.questionCombo=ttk.Combobox(self.entriesFrameAnswer,width=47,textvariable=self.placeholderArray[1],values=self.categoryArray)

        self.answerTextEntry.grid(row=1,column=2,padx=5,pady=5)
        self.isCorrect.grid(row=2,column=2,padx=5,pady=5)
        self.questionCombo.grid(row=0,column=2,padx=5,pady=5)
         

    def setph(self,word,num):
        for ph in range(0,5):
            if ph == num:
                self.placeholderArray[ph].set(word)
    def getQuestionId(self):
        for cat1 in self.categoryArray1:
            if(self.questionCombo.get() == cat1['question_text']):
                return cat1['question_id']
    def save(self):
        question_id=int(self.getQuestionId())
        answer_text=str(self.answerTextEntry.get())
        is_correct = self.CheckIscorrect.get()
        valid=True
        if  not(answer_text) or not(question_id):
            messagebox.showwarning("","Please fill up all entries")
            return
        Answer(answer_text,is_correct,question_id).createAnswer()
        for num in range(0,5):
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
        question_id=str(self.getQuestionId())
        answer_text=str(self.answerTextEntry.get())
        is_correct = self.CheckIscorrect.get()
        valid=True
        if  not(answer_text) or not(question_id):
            messagebox.showwarning("","Please fill up all entries")
            return
        Answer(answer_text,is_correct,question_id).updateAnswer(selectedItemId)
        for num in range(0,5):
                self.setph('',(num))
        self.refreshTable()

    def select(self,event):
        try:
            selectedItem = self.my_tree.selection()[0]
            answer_text = str(self.my_tree.item(selectedItem)['values'][1])
            question_id = str(self.my_tree.item(selectedItem)['values'][3])
            is_correct =  int(self.my_tree.item(selectedItem)['values'][2])
            print("-------",is_correct)
            self.setph(answer_text,0)
            self.setph(question_id,1)
            self.CheckIscorrect.set(is_correct)
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
                        Answer().deleteAnswer(itemId)
                        messagebox.showinfo("","Data has been successfully deleted")
                        for num in range(0,5):
                            self.setph('',(num))
                        self.refreshTable()
                    except:
                        messagebox.showinfo("","Sorry, an error occured")
                        return
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
                array['question_id'],
                array['student_id']),tag="orow")
        self.my_tree.tag_configure('orow',background="#EEEEEE")
        self.my_tree.grid(row=0, column=4, pady=[10,5])
        back = offset - 5
        next = offset + 5
        b1=Button(self.listFrameAnswer,text="< Prev",command=lambda:self.refreshTable(back))
        b2=Button(self.listFrameAnswer,text="Next >",command=lambda:self.refreshTable(next))
        b1.grid(row=6, column=0, columnspan=10, rowspan=5,sticky="w",padx=[500,50],pady=[0,20],ipadx=[10])
        b2.grid(row=7, column=0, columnspan=10, rowspan=5, sticky="W",padx=[600,10],pady=[0,20],ipadx=[20])
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
                    self.CheckIscorrect.set(0)

    def reset(self):
        for num in range(0,5):
            self.setph('',(num))

    def constructFrame(self):
        manageActionAnswer=tkinter.LabelFrame(self.entriesFrameAnswer,text="ACTIONS ANSWER",borderwidth=5)
        manageActionAnswer.grid(row=6,column=0,columnspan=70,rowspan=15,padx=[10,15],pady=20,ipadx=[5])

        saveBtn=Button(manageActionAnswer,text="SAVE",width=20,borderwidth=3,bg=self.btnColor,fg='white',command=self.save,cursor="hand2")
        updateBtn=Button(manageActionAnswer,text="UPDATE",width=20,borderwidth=3,bg=self.btnColor,fg='white',command=self.update,cursor="hand2")
        deleteBtn=Button(manageActionAnswer,text="DELETE",width=20,borderwidth=3,bg=self.btnColor,fg='white',command=self.delete,cursor="hand2")
        resetBtn=Button(manageActionAnswer,text="RESET",width=20,borderwidth=3,bg=self.btnColor,fg='white',command=self.reset,cursor="hand2")

        saveBtn.grid(row=0,column=0,padx=5,pady=5)
        updateBtn.grid(row=0,column=1,padx=5,pady=5)
        deleteBtn.grid(row=0,column=2,padx=5,pady=5)
        resetBtn.grid(row=0,column=3,padx=5,pady=5)

        self.style.configure(self.windowanswer)
        self.my_tree['columns']=("Answer Id","Answer Text","Is Correct","Question Id", "Student Id")
        self.my_tree.column("#0",width=0,stretch=NO)
        self.my_tree.column("Answer Id",anchor=W,width=70)
        self.my_tree.column("Answer Text",anchor=W,width=400)
        self.my_tree.column("Is Correct",anchor=W,width=70) 
        self.my_tree.column("Question Id",anchor=W,width=70) 
        self.my_tree.column("Student Id",anchor=W,width=70) 

        self.my_tree.heading("Answer Id",text="Answer Id",anchor=W)
        self.my_tree.heading("Answer Text",text="Answer Text",anchor=W)
        self.my_tree.heading("Is Correct",text="Is Correct",anchor=W)
        self.my_tree.heading("Question Id",text="Question Id",anchor=W)
        self.my_tree.heading("Student Id",text="Student Id",anchor=W)
        self.my_tree.tag_configure('orow',background="#EEEEEE")
        self.refreshTable()