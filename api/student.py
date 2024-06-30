import requests


class Student(object):
    def __init__(self, student_number=0, name="", surname=""):
        self.student_number = student_number
        self.name = name
        self.surname = surname
    
    async def getStudents(self):
        try:
            response  =  requests.get("http://localhost:8080/api/students/get")
            print(response.json())
            return  response.json()
        except requests.ConnectionError as err:
            print(err)


    async def getStudentById(self, id):
        try:
            response  =  requests.get(f"http://localhost:8080/api/students/getById/{id}")
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)

    async def deleteStudent(self, id):
        try:
            response  =  requests.delete(f"http://localhost:8080/api/students/delete/{id}")
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)

    async def createStudent(self):
        payload = {
            "student_number": self.student_number,
            "name": self.name,
            'surname': self.surname
        }
        headers = {"Content-type": "application/json" }
        try:
            response  =  requests.post("http://localhost:8080/api/students/create", json=payload, headers=headers)
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)

    async def updateStudent(self, id):
        payload = {
            "student_number": self.student_number,
            "name": self.name,
            'surname': self.surname
        }
        headers = {"Content-type": "application/json" }
        try:
            response  =  requests.put(f"http://localhost:8080/api/students/update/{id}", json=payload, headers=headers)
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)