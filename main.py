import time
import asyncio
from api import student
from api.student import Student


async def main():
   student =  Student().getStudents()
   student1 = Student().getStudentById(22)  
   student2 = Student().deleteStudent(1)
   student3 = Student(2568, "mvogo nkolo",  "pierre").createStudent()

  
   batch = asyncio.gather(student,student1,student2,student3)
   await batch

if __name__ == "__main__":
   asyncio.run(main())