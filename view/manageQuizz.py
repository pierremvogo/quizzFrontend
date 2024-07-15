from tkinter import NO, W, Button, Entry, Label, messagebox, ttk
import tkinter
from api.quizz import Quizz


class ManageQuizz:
    def __init__(self,window,framequizz,btnColor, style):
        self.btnColor = btnColor
        self.window = window
        self.framequizz = framequizz
        self.framequizz.pack()
        self.style = style
        self.placeholderArray = placeholderArray=['','','','','']
        offset = 0
        for i in range(0,5):
            placeholderArray[i]=tkinter.StringVar()

        self.listFrameQuizz=tkinter.LabelFrame(self.framequizz,text="LIST OF QUIZZ",borderwidth=5,font=("Tahoma", 15),fg="black")
        self.listFrameQuizz.grid(row=5,column=0,sticky="w",padx=[10,10],pady=[0,200],ipadx=[50])

        self.my_tree = ttk.Treeview(self.listFrameQuizz,selectmode='browse',show='headings',height=11, padding=5)
        self.my_tree.bind("<ButtonRelease-1>", self.select)

        self.entriesFrameQuizz = tkinter.LabelFrame(self.framequizz,text="QUIZZ",borderwidth=5,font=("Tahoma", 15),fg="black")
        self.entriesFrameQuizz.grid(row=1,column=0,sticky="w",padx=[10,200],pady=[0,20],ipadx=[2])

        self.titleLabel=Label(self.entriesFrameQuizz,text="Quizz Title",anchor="e",width=15, pady=20,font=("Tahoma", 15))
        self.descriptionLabel=Label(self.entriesFrameQuizz,text="Description",anchor="e",width=15,font=("Tahoma", 15))

        self.titleLabel.grid(row=0,column=0,padx=10)
        self.descriptionLabel.grid(row=1,column=0,padx=10)

        self.titleEntry=Entry(self.entriesFrameQuizz,width=55,font=("Verdana", 15),textvariable=self.placeholderArray[0])
        self.descriptionEntry=Entry(self.entriesFrameQuizz,width=55,font=("Verdana", 15),textvariable=self.placeholderArray[1])

        self.titleEntry.grid(row=0,column=2,padx=5,pady=5)
        self.descriptionEntry.grid(row=1,column=2,padx=5,pady=5)

        self.manageActionQuizz=tkinter.LabelFrame(self.entriesFrameQuizz,text="ACTIONS QUIZZ",borderwidth=5,font=("Tahoma", 15),fg="black")
        self.manageActionQuizz.grid(row=6,column=0,columnspan=70,rowspan=15,padx=[10,15],pady=20,ipadx=[5])

        self.saveBtn=Button(self.manageActionQuizz,text="SAVE",width=25,borderwidth=3,fg='black',height=2,command=self.save,cursor="hand2")
        self.updateBtn=Button(self.manageActionQuizz,text="UPDATE",width=25,borderwidth=3,fg='black',height=2,command=self.update,cursor="hand2")
        self.deleteBtn=Button(self.manageActionQuizz,text="DELETE",width=25,borderwidth=3,fg='black',height=2,command=self.delete,cursor="hand2")
        self.selectBtn=Button(self.manageActionQuizz,text="RESET",width=25,borderwidth=3,fg='black',height=2,command=self.reset,cursor="hand2")

        self.saveBtn.grid(row=0,column=0,padx=[490,10],pady=5)
        self.updateBtn.grid(row=0,column=1,padx=[5,10],pady=5)
        self.deleteBtn.grid(row=0,column=2,padx=[5,10],pady=5)
        self.selectBtn.grid(row=0,column=3,padx=[5,10],pady=5)

        self.style.configure(self.window)
        self.style.configure("Treeview.Heading", font=("Verdana", 12))
        self.style.configure("Treeview.Column", font=(None, 20))
        self.my_tree['columns']=("Quizz Id","Quizz Title","Quizz Description","Student")
        self.my_tree.column("#0",width=0,stretch=NO)
        self.my_tree.column("Quizz Id",anchor=W,width=100)
        self.my_tree.column("Quizz Title",anchor=W,width=400)
        self.my_tree.column("Quizz Description",anchor=W,width=600) 

        self.my_tree.heading("Quizz Id",text="Quizz Id",anchor=W)
        self.my_tree.heading("Quizz Title",text="Quizz Title",anchor=W)
        self.my_tree.heading("Quizz Description",text="Quizz Description",anchor=W)
        self.my_tree.tag_configure('orow',background="#EEEEEE")
        self.refreshTable()
        

    def setph(self,word,num):
        for ph in range(0,5):
            if ph == num:
                self.placeholderArray[ph].set(word)

    def save(self):
        title=str(self.titleEntry.get())
        description=str(self.descriptionEntry.get())
        valid=True
        if  not(title and title.strip()) or not(description and description.strip()):
            messagebox.showwarning("","Please fill up all entries")
            return
        Quizz(title,description).createQuizz()
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
        title=str(self.titleEntry.get())
        description=str(self.descriptionEntry.get())
        valid=True
        if  not(title and title.strip()) or not(description and description.strip()):
            messagebox.showwarning("","Please fill up all entries")
            return
        Quizz(title,description).updateQuizz(selectedItemId)
        for num in range(0,5):
                self.setph('',(num))
        self.refreshTable()

    def select(self,event):
        try:
            self.saveBtn['state']='disabled'
            selectedItem = self.my_tree.selection()[0]
            title = str(self.my_tree.item(selectedItem)['values'][1])
            description = str(self.my_tree.item(selectedItem)['values'][2])
            self.setph(title,0)
            self.setph(description,1)
        except:
            messagebox.showwarning("", "Please select a data row--------")
            return

    def delete(self):
        try:
            if(self.my_tree.selection()[0]):
                decision = messagebox.askquestion("", "Delete this quizz?")
                if(decision != 'yes'):
                    return
                else:
                    selectedItem = self.my_tree.selection()[0]
                    itemId = str(self.my_tree.item(selectedItem)['values'][0])
                    try:
                        Quizz().deleteQuizz(itemId)
                        messagebox.showinfo("","Data has been successfully deleted")
                        for num in range(0,5):
                            self.setph('',(num))
                        self.refreshTable()
                    except:
                        messagebox.showinfo("","Sorry, an error occured")
                        return
                    self.saveBtn['state']='active'
                    self.refreshTable()
        except:
            messagebox.showwarning("", "Please select a data row")


    no_rec =  Quizz().countQuizz()[0]['COUNT(*)'] 
    def setph(self,word,num):
        for ph in range(0,5):
            if ph == num:
                self.placeholderArray[ph].set(word)
    def read(self,offset):
        results =  Quizz().getQuizzsByPagination(offset)
        print(results)
        return results
    
    def refreshTable(self, offset = 0):
        no_recquiz =  Quizz().countQuizz()[0]['COUNT(*)'] 
        for data in self.my_tree.get_children():
            self.my_tree.delete(data)
        for array in self.read(offset):
            self.my_tree.insert(parent='',index='end',iid=array['id'],text="",values=(
                array['id'], 
                array['title'],
                array['description']),tag="orow")
        self.my_tree.tag_configure('orow',background="#EEEEEE")
        self.my_tree.grid(row=0, column=4, pady=[10,5])
        back = offset - 10
        next = offset + 10
        b1=Button(self.listFrameQuizz,text="< Prev",command=lambda:self.refreshTable(back),width=10, height=1)
        b2=Button(self.listFrameQuizz,text="Next >",command=lambda:self.refreshTable(next),width=10, height=1)
        b1.grid(row=6, column=0, columnspan=10, rowspan=5,sticky="w",padx=[1145,10],pady=[0,20],)
        b2.grid(row=7, column=0, columnspan=10, rowspan=5, sticky="W",padx=[1235,10],pady=[0,20])
        print(back)
        print(next)
        if (no_recquiz <= next):
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
        for num in range(0,5):
            self.setph('',(num))

   
        