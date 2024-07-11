from tkinter import NO, W, Button, Entry, Label, messagebox, ttk
import tkinter
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

        self.categoryArray=[]
        self.categoryArray1=[]
        self.quizz = Quizz().getQuizz()
        print("ALL QUIIZ DATA: ",self.quizz)
        for quizz in self.quizz:
            self.categoryArray.append(quizz['title'])
            self.categoryArray1.append({'quizz_id':quizz['id'], 'quizz_title':quizz['title']})

        self.listFrameQuestion=tkinter.LabelFrame(self.framequestion,text="LIST OF QUESTION",borderwidth=5)
        self.listFrameQuestion.grid(row=5,column=0,sticky="w",padx=[10,10],pady=[0,200],ipadx=[50])

        self.my_tree = ttk.Treeview(self.listFrameQuestion,selectmode='browse',show='headings',height=5, padding=5)
        self.my_tree.bind("<ButtonRelease-1>", self.select)

        self.entriesFrameQuestion = tkinter.LabelFrame(self.framequestion,text="QUESTION",borderwidth=5)
        self.entriesFrameQuestion.grid(row=1,column=0,sticky="w",padx=[10,200],pady=[0,20],ipadx=[2])

        self.questionTextLabel=Label(self.entriesFrameQuestion,text="Question Text",anchor="e",width=15, pady=20)
        self.quizLabel=Label(self.entriesFrameQuestion,text="Quizz",anchor="e",width=15)

        self.questionTextLabel.grid(row=0,column=0,padx=10)
        self.quizLabel.grid(row=1,column=0,padx=10)

        self.questionTextEntry=Entry(self.entriesFrameQuestion,width=50,textvariable=self.placeholderArray[0])
        self.categoryCombo=ttk.Combobox(self.entriesFrameQuestion,width=47,textvariable=self.placeholderArray[1],values=self.categoryArray)

        self.questionTextEntry.grid(row=0,column=2,padx=5,pady=5)
        self.categoryCombo.grid(row=1,column=2,padx=5,pady=5)
         

    def setph(self,word,num):
        for ph in range(0,5):
            if ph == num:
                self.placeholderArray[ph].set(word)
    def getQuizId(self):
        for cat1 in self.categoryArray1:
            if(self.categoryCombo.get() == cat1['quizz_title']):
                return cat1['quizz_id']
    def save(self):
        question_text=str(self.questionTextEntry.get())
        quizz_id=int(self.getQuizId())
        valid=True
        if  not(question_text) or not(quizz_id):
            messagebox.showwarning("","Please fill up all entries")
            return
        Question(question_text,quizz_id).createQuestion()
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
        question_text=str(self.questionTextEntry.get())
        quizz_id=str(self.getQuizId())
        valid=True
        if  not(question_text) or not(quizz_id):
            messagebox.showwarning("","Please fill up all entries")
            return
        Question(question_text,quizz_id).updateQuestion(selectedItemId)
        for num in range(0,5):
                self.setph('',(num))
        self.refreshTable()

    def select(self,event):
        try:
            selectedItem = self.my_tree.selection()[0]
            question_text = str(self.my_tree.item(selectedItem)['values'][1])
            quizz_id = str(self.my_tree.item(selectedItem)['values'][2])
            self.setph(question_text,0)
            self.setph(quizz_id,1)
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
                        Question().deleteQuestion(itemId)
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


    
    def setph(self,word,num):
        for ph in range(0,5):
            if ph == num:
                self.placeholderArray[ph].set(word)
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
                array['quiz_id']),tag="orow")
        self.my_tree.tag_configure('orow',background="#EEEEEE")
        self.my_tree.grid(row=0, column=4, pady=[10,5])
        back = offset - 5
        next = offset + 5
        b1=Button(self.listFrameQuestion,text="< Prev",command=lambda:self.refreshTable(back))
        b2=Button(self.listFrameQuestion,text="Next >",command=lambda:self.refreshTable(next))
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

    def reset(self):
        for num in range(0,5):
            self.setph('',(num))

    def constructFrame(self):
        manageActionQuestion=tkinter.LabelFrame(self.entriesFrameQuestion,text="ACTIONS QUESTION",borderwidth=5)
        manageActionQuestion.grid(row=6,column=0,columnspan=70,rowspan=15,padx=[10,15],pady=20,ipadx=[5])

        saveBtn=Button(manageActionQuestion,text="SAVE",width=20,borderwidth=3,bg=self.btnColor,fg='white',command=self.save,cursor="hand2")
        updateBtn=Button(manageActionQuestion,text="UPDATE",width=20,borderwidth=3,bg=self.btnColor,fg='white',command=self.update,cursor="hand2")
        deleteBtn=Button(manageActionQuestion,text="DELETE",width=20,borderwidth=3,bg=self.btnColor,fg='white',command=self.delete,cursor="hand2")
        resetBtn=Button(manageActionQuestion,text="RESET",width=20,borderwidth=3,bg=self.btnColor,fg='white',command=self.reset,cursor="hand2")

        saveBtn.grid(row=0,column=0,padx=5,pady=5)
        updateBtn.grid(row=0,column=1,padx=5,pady=5)
        deleteBtn.grid(row=0,column=2,padx=5,pady=5)
        resetBtn.grid(row=0,column=3,padx=5,pady=5)

        self.style.configure(self.windowquestion)
        self.my_tree['columns']=("Question Id","Question Text","Quizz Id")
        self.my_tree.column("#0",width=0,stretch=NO)
        self.my_tree.column("Question Id",anchor=W,width=100)
        self.my_tree.column("Question Text",anchor=W,width=400)
        self.my_tree.column("Quizz Id",anchor=W,width=200) 

        self.my_tree.heading("Question Id",text="Question Id",anchor=W)
        self.my_tree.heading("Question Text",text="Question Text",anchor=W)
        self.my_tree.heading("Quizz Id",text="Quizz Id",anchor=W)
        self.my_tree.tag_configure('orow',background="#EEEEEE")
        self.refreshTable()