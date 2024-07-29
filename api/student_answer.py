import requests


class StudentAnswer(object):
    def __init__(self, student_fkid=0, answer_fkid=0, answer_text_fk="", is_correct=0):
        self.student_fkid = student_fkid
        self.answer_fkid = answer_fkid
        self.answer_text_fk = answer_text_fk
        self.is_correct = is_correct
    
    def getStudentsAnswers(self):
        try:
            response  =  requests.get("http://localhost:8080/api/studentsAnswers/get")
            return  response.json()
        except requests.ConnectionError as err:
            print(err)


    def getStudentAnswersById(self, student_fkid, answer_fkid):
        try:
            response  =  requests.get(f"http://localhost:8080/api/studentsAnswers/getById/{student_fkid}/{answer_fkid}")
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)

    def getStudentByAnswerId(self, id):
        try:
            response  =  requests.get(f"http://localhost:8080/api/studentsAnswers/getByAnswerId/{id}")
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)

    def getStudentByAnswerId1(self):
        try:
            response  =  requests.get(f"http://localhost:8080/api/studentsAnswers/getByAnswerId1")
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)


    def deleteStudentAnswer(self, student_fkid,answer_fkid):
        try:
            response  =  requests.get(f"http://localhost:8080/api/studentsAnswers/delete/{student_fkid}/{answer_fkid}")
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)

    def createStudentsAnswers(self):
        payload = {
            "student_fkid": self.student_fkid,
            "answer_fkid": self.answer_fkid,
            "answer_text_fk": self.answer_text_fk,
            "is_correct": self.is_correct
        }
        headers = {"Content-type": "application/json" }
        try:
            response  =  requests.post("http://localhost:8080/api/studentsAnswers/create", json=payload, headers=headers)
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)

    def updateStudentAnswer(self):
        payload = {
            "correct": self.is_correct
        }
        headers = {"Content-type": "application/json" }
        try:
            response  =  requests.put(f"http://localhost:8080/api/studentsAnswers/update/{self.student_fkid}/{self.answer_fkid}", json=payload, headers=headers)
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)
            return err