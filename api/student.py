import requests


class Student(object):
    def __init__(self, student_number=0, name="", surname=""):
        self.student_number = student_number
        self.name = name
        self.surname = surname
    
    def getStudents(self):
        try:
            response  =  requests.get("http://localhost:8080/api/students/get")
            return  response.json()
        except requests.ConnectionError as err:
            print(err)

    def getStudentsByPagination(self,offset):
        try:
            response  =  requests.get(f"http://localhost:8080/api/students/get/pagination/{offset}")
            return  response.json()
        except requests.ConnectionError as err:
            print(err)

    def countStudent(self):
        try:
            response  =  requests.get(f"http://localhost:8080/api/students/count")
            return  response.json()
        except requests.ConnectionError as err:
            print(err)


    def getStudentById(self, id):
        try:
            response  =  requests.get(f"http://localhost:8080/api/students/getById/{id}")
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)

    def getStudentByNumber(self, studentNumber):
        try:
            response  =  requests.get(f"http://localhost:8080/api/students/getByNumber/{studentNumber}")
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            return err
        except requests.JSONDecodeError as err:
            return err
        except requests.HTTPError as err:
            return err

    def deleteStudent(self, id):
        try:
            response  =  requests.delete(f"http://localhost:8080/api/students/delete/{id}")
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)

    def createStudent(self):
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

    def updateStudent(self, id):
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
            return err

    def deleteAllStudent(self):
        try:
            response  =  requests.delete(f"http://localhost:8080/api/students/deleteAll")
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)