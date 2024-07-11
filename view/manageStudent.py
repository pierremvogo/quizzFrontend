
from tkinter import NO, W, Button, Entry, Label, messagebox, ttk
import tkinter
from api.student import Student


class ManageStudent:
    def __init__(self,windowstudent,framestudent,btnColor, style):
        self.btnColor = btnColor
        self.windowstudent = windowstudent
        self.framestudent = framestudent
        self.framestudent.pack()
        self.style = style
        self.placeholderArray = placeholderArray=['','','','','']
        offset = 0
        for i in range(0,5):
            placeholderArray[i]=tkinter.StringVar()
        self.listFrameStudent = listFrameStudent=tkinter.LabelFrame(self.framestudent,text="LIST OF STUDENT",borderwidth=5)
        self.listFrameStudent.grid(row=5,column=0,sticky="w",padx=[10,10],pady=[0,200],ipadx=[50])

        self.my_tree = ttk.Treeview(self.listFrameStudent,selectmode='browse',show='headings',height=5, padding=5)
        self.my_tree.bind("<ButtonRelease-1>", self.select)

        self.entriesFrameStudent = tkinter.LabelFrame(self.framestudent,text="STUDENT",borderwidth=5)
        self.entriesFrameStudent.grid(row=1,column=0,sticky="w",padx=[10,200],pady=[0,20],ipadx=[2])

        self.studentNumberLabel=Label(self.entriesFrameStudent,text="STUDENT NUMBER",anchor="e",width=15)
        self.nameLabel=Label(self.entriesFrameStudent,text="NAME",anchor="e",width=15)
        self.surnameLabel=Label(self.entriesFrameStudent,text="SURNAME",anchor="e",width=15)

        self.studentNumberLabel.grid(row=0,column=0,padx=10)
        self.nameLabel.grid(row=1,column=0,padx=10)
        self.surnameLabel.grid(row=2,column=0,padx=10)

        self.studentNumberEntry=Entry(self.entriesFrameStudent,width=50,textvariable=self.placeholderArray[0])
        self.nameEntry=Entry(self.entriesFrameStudent,width=50,textvariable=self.placeholderArray[1])
        self.surnameEntry=Entry(self.entriesFrameStudent,width=50,textvariable=self.placeholderArray[2])

        self.studentNumberEntry.grid(row=0,column=2,padx=5,pady=5)
        self.nameEntry.grid(row=1,column=2,padx=5,pady=5)
        self.surnameEntry.grid(row=2,column=2,padx=5,pady=5)
         

    def setph(self,word,num):
        for ph in range(0,5):
            if ph == num:
                self.placeholderArray[ph].set(word)

    def save(self):
        student_number=str(self.studentNumberEntry.get())
        name=str(self.nameEntry.get())
        surname=str(self.surnameEntry.get())
        valid=True
        if  not(student_number and student_number.strip()) or not(name and name.strip()) or not(surname and surname.strip()):
            messagebox.showwarning("","Please fill up all entries")
            return
        Student(student_number,name,surname).createStudent()
        for num in range(0,5):
                self.setph('',(num))
        self.refreshTable()

    def update(self):
        selectedItemId = ''
        try:
            selectedItem = self.my_tree.selection()[0]
            selectedItemId = str(self.my_tree.item(selectedItem)['values'][0])
        except:
            messagebox.showwarning("", "Please select student on the table")
            return
        print(selectedItemId)
        student_number=str(self.studentNumberEntry.get())
        name=str(self.nameEntry.get())
        surname=str(self.surnameEntry.get())
        valid=True
        if  not(student_number and student_number.strip()) or not(name and name.strip()) or not(surname and surname.strip()):
            messagebox.showwarning("","Please fill up all entries")
            return
        Student(student_number,name,surname).updateStudent(selectedItemId)
        for num in range(0,5):
                self.setph('',(num))
        self.refreshTable()

    def select(self,event):
        try:
            selectedItem = self.my_tree.selection()[0]
            student_number = str(self.my_tree.item(selectedItem)['values'][1])
            name = str(self.my_tree.item(selectedItem)['values'][2])
            surname = str(self.my_tree.item(selectedItem)['values'][3])
            self.setph(student_number,0)
            self.setph(name,1)
            self.setph(surname,2)
        except:
            messagebox.showwarning("", "Please select a data row--------")
            return

    def delete(self):
        try:
            if(self.my_tree.selection()[0]):
                decision = messagebox.askquestion("", "Delete this student?")
                if(decision != 'yes'):
                    return
                else:
                    selectedItem =self. my_tree.selection()[0]
                    itemId = str(self.my_tree.item(selectedItem)['values'][0])
                    try:
                        Student().deleteStudent(itemId)
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
        results =  Student().getStudentsByPagination(offset)
        print(results)
        return results
    
    def refreshTable(self, offset = 0):
        no_recstudent =  Student().countStudent()[0]['COUNT(*)']
        for data in self.my_tree.get_children():
            self.my_tree.delete(data)
        for array in self.read(offset):
            self.my_tree.insert(parent='',index='end',iid=array['id'],text="",values=(
                array['id'], 
                array['student_number'],
                array['name'],
                array['surname'],
                array['quiz_id']),tag="orow")
        self.my_tree.tag_configure('orow',background="#EEEEEE")
        self.my_tree.grid(row=0, column=4, pady=[10,5])
        back = offset - 5
        next = offset + 5
        b1=Button(self.listFrameStudent,text="< Prev",command=lambda:self.refreshTable(back))
        b2=Button(self.listFrameStudent,text="Next >",command=lambda:self.refreshTable(next))
        b1.grid(row=6, column=0, columnspan=10, rowspan=5,sticky="w",padx=[500,50],pady=[0,20],ipadx=[10])
        b2.grid(row=7, column=0, columnspan=10, rowspan=5, sticky="W",padx=[600,10],pady=[0,20],ipadx=[20])
        print(back)
        print(next)
        if (no_recstudent <= next):
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
       

        manageActionStudent=tkinter.LabelFrame(self.entriesFrameStudent,text="ACTIONS STUDENT",borderwidth=5)
        manageActionStudent.grid(row=6,column=0,columnspan=70,rowspan=15,padx=[10,15],pady=20,ipadx=[5])

        saveBtn=Button(manageActionStudent,text="SAVE",width=20,borderwidth=3,bg=self.btnColor,fg='white',command=self.save,cursor="hand2")
        updateBtn=Button(manageActionStudent,text="UPDATE",width=20,borderwidth=3,bg=self.btnColor,fg='white',command=self.update,cursor="hand2")
        deleteBtn=Button(manageActionStudent,text="DELETE",width=20,borderwidth=3,bg=self.btnColor,fg='white',command=self.delete,cursor="hand2")
        selectBtn=Button(manageActionStudent,text="RESET",width=20,borderwidth=3,bg=self.btnColor,fg='white',command=self.reset,)
        saveBtn.grid(row=0,column=0,padx=5,pady=5)
        updateBtn.grid(row=0,column=1,padx=5,pady=5)
        deleteBtn.grid(row=0,column=2,padx=5,pady=5)
        selectBtn.grid(row=0,column=3,padx=5,pady=5)



        self.style.configure(self.windowstudent)
        self.my_tree['columns']=("Student Id","Student Number","Student Name","Student Surname", "Quiz Id")
        self.my_tree.column("#0",width=0,stretch=NO)
        self.my_tree.column("Student Id",anchor=W,width=70)
        self.my_tree.column("Student Number",anchor=W,width=100)
        self.my_tree.column("Student Name",anchor=W,width=200) 
        self.my_tree.column("Student Surname",anchor=W,width=150)
        self.my_tree.column("Quiz Id",anchor=W,width=150)

        self.my_tree.heading("Student Id",text="Student Id",anchor=W)
        self.my_tree.heading("Student Number",text="Student Number",anchor=W)
        self.my_tree.heading("Student Name",text="Student Name",anchor=W)
        self.my_tree.heading("Student Surname",text="Student Surname",anchor=W)
        self.my_tree.heading("Quiz Id",text="Quiz Id",anchor=W)
        self.my_tree.tag_configure('orow',background="#EEEEEE")
        self.refreshTable()