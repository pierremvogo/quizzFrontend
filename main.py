import time
import asyncio
from api import student
from api.student import Student


def main():
   student =  Student().getStudents()
   student1 = Student().getStudentById(1)  #ICI
   loop = asyncio.get_event_loop()
   loop.run_until_complete(student)
   loop.run_until_complete(student1)  #et ICI
   loop.close()

if __name__ == "__main__":
    main()
    #asyncio.run(main())