
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
        self.listFrameStudent = listFrameStudent=tkinter.LabelFrame(self.framestudent,text="LIST OF STUDENT",borderwidth=5,font=("Tahoma", 15),fg="black")
        self.listFrameStudent.grid(row=5,column=0,sticky="w",padx=[10,10],pady=[0,200],ipadx=[50])

        self.my_tree = ttk.Treeview(self.listFrameStudent,selectmode='browse',show='headings',height=11, padding=5)
        self.my_tree.bind("<ButtonRelease-1>", self.select)

        self.entriesFrameStudent = tkinter.LabelFrame(self.framestudent,text="STUDENT",borderwidth=5,font=("Tahoma", 15),fg="black")
        self.entriesFrameStudent.grid(row=1,column=0,sticky="w",padx=[10,200],pady=[0,20],ipadx=[2])

        self.studentNumberLabel=Label(self.entriesFrameStudent,text="STUDENT NUMBER",anchor="e",width=15,font=("Tahoma", 15))
        self.nameLabel=Label(self.entriesFrameStudent,text="NAME",anchor="e",width=15,font=("Tahoma", 15))
        self.surnameLabel=Label(self.entriesFrameStudent,text="SURNAME",anchor="e",width=15, font=("Tahoma", 15))

        self.studentNumberLabel.grid(row=0,column=0,padx=[200,5])
        self.nameLabel.grid(row=1,column=0,padx=[200,5])
        self.surnameLabel.grid(row=2,column=0,padx=[200,5])

        self.studentNumberEntry=Entry(self.entriesFrameStudent,width=37,font=("Verdana", 15),textvariable=self.placeholderArray[0])
        self.nameEntry=Entry(self.entriesFrameStudent,width=37,font=("Verdana", 15),textvariable=self.placeholderArray[1])
        self.surnameEntry=Entry(self.entriesFrameStudent,width=37,font=("Verdana", 15),textvariable=self.placeholderArray[2])

        self.studentNumberEntry.grid(row=0,column=2,padx=5)
        self.nameEntry.grid(row=1,column=2,padx=5,pady=5)
        self.surnameEntry.grid(row=2,column=2,padx=5,pady=5)

        self.manageActionStudent=tkinter.LabelFrame(self.entriesFrameStudent,text="ACTIONS STUDENT",borderwidth=5,font=("Tahoma", 15),fg="black")
        self.manageActionStudent.grid(row=6,column=0,columnspan=70,rowspan=15,padx=[10,15],pady=20,ipadx=[5])

        self.saveBtn=Button(self.manageActionStudent,text="SAVE",width=25,borderwidth=3,fg='black', height=2,command=self.save,cursor="hand2")
        self.updateBtn=Button(self.manageActionStudent,text="UPDATE",width=25,borderwidth=3,fg='black', height=2,command=self.update,cursor="hand2")
        self.deleteBtn=Button(self.manageActionStudent,text="DELETE",width=25,borderwidth=3,fg='black', height=2,command=self.delete,cursor="hand2")
        self.selectBtn=Button(self.manageActionStudent,text="RESET",width=25,borderwidth=3,fg='black', height=2,command=self.reset,)
        self.saveBtn.grid(row=0,column=0,padx=[490,10],pady=5)
        self.updateBtn.grid(row=0,column=1,padx=[5,10],pady=5)
        self.deleteBtn.grid(row=0,column=2,padx=[5,10],pady=5)
        self.selectBtn.grid(row=0,column=3,padx=[5,10],pady=5)



        self.style.configure(self.windowstudent)
        self.style.configure("Treeview.Heading", font=("Verdana", 12))
        self.style.configure("Treeview.Column", font=(None, 20))
        self.my_tree['columns']=("Student Id","Student Number","Student Name","Student Surname", "Quiz Id")
        self.my_tree.column("#0",width=0,stretch=NO)
        self.my_tree.column("Student Id",anchor=W,width=200)
        self.my_tree.column("Student Number",anchor=W,width=200)
        self.my_tree.column("Student Name",anchor=W,width=300) 
        self.my_tree.column("Student Surname",anchor=W,width=320)
        self.my_tree.column("Quiz Id",anchor=W,width=200)

        self.my_tree.heading("Student Id",text="Student Id",anchor=W)
        self.my_tree.heading("Student Number",text="Student Number",anchor=W)
        self.my_tree.heading("Student Name",text="Student Name",anchor=W)
        self.my_tree.heading("Student Surname",text="Student Surname",anchor=W)
        self.my_tree.heading("Quiz Id",text="Quiz Id",anchor=W)
        self.my_tree.tag_configure('orow',background="#EEEEEE")
        self.refreshTable()
         

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
        Student(student_number,name,surname,None).updateStudent(selectedItemId)
        for num in range(0,5):
                self.setph('',(num))
        self.saveBtn['state']='active'
        self.refreshTable()

    def select(self,event):
        try:
            self.saveBtn['state']='disabled'
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
                    self.saveBtn['state']='enable'
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
            self.my_tree.insert(parent='',index='end',iid=array['student_id'],text="",values=(
                array['student_id'], 
                array['student_number'],
                array['name'],
                array['surname'],
                array['quiz_id']),tag="orow")
        self.my_tree.tag_configure('orow',background="#EEEEEE")
        self.my_tree.grid(row=0, column=4, pady=[10,5])
        back = offset - 10
        next = offset + 10
        b1=Button(self.listFrameStudent,text="< Prev",command=lambda:self.refreshTable(back), width=10, height=1)
        b2=Button(self.listFrameStudent,text="Next >",command=lambda:self.refreshTable(next), width=10, height=1)
        b1.grid(row=6, column=0, columnspan=10, rowspan=5,sticky="w",padx=[1050,10],pady=[0,20],)
        b2.grid(row=7, column=0, columnspan=10, rowspan=5, sticky="W",padx=[1155,10],pady=[0,20])
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
        self.saveBtn['state']='active'
        for num in range(0,5):
            self.setph('',(num))

       

        