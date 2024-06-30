import time
import asyncio
from api import student
from api.student import Student


def main():
   student =  Student().getStudents()
   student1 = Student().getStudentById(22)  #ICI
   student2 = Student().deleteStudent(1)
   student3 = Student(2568, "mvogo nkolo",  "pierre").createStudent()
   loop = asyncio.get_event_loop()
   loop.run_until_complete(student)
   loop.run_until_complete(student1)  #et ICI
   loop.run_until_complete(student2)
   loop.run_until_complete(student3)
   loop.close()

if __name__ == "__main__":
    main()