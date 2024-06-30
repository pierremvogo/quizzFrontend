import time
import asyncio
from api import student
from api.student import Student


def main():
   student =  Student().getStudents()
   loop = asyncio.get_event_loop()
   loop.run_until_complete(student)
   loop.close()

if __name__ == "__main__":
    main()
    #asyncio.run(main())