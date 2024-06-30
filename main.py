import time
import asyncio
from api import student
from api.student import Student


async def main():
   student = Student()
   print(student.getStudents())

if __name__ == "__main__":
    asyncio.run(main())