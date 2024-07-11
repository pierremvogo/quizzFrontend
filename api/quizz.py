import requests


class Quizz(object):
    def __init__(self, title="", description="", student_id=0):
        self.title = title
        self.description = description
        self.student_id = student_id
    
    def getQuizz(self):
        try:
            response  =  requests.get("http://localhost:8080/api/quizzs/get")
            print(response.json())
            return  response.json()
        except requests.ConnectionError as err:
            print(err)

    def getQuizzsByPagination(self,offset):
        try:
            response  =  requests.get(f"http://localhost:8080/api/quizzs/get/pagination/{offset}")
            return  response.json()
        except requests.ConnectionError as err:
            print(err)

    def countQuizz(self):
        try:
            response  =  requests.get(f"http://localhost:8080/api/quizzs/count")
            return  response.json()
        except requests.ConnectionError as err:
            print(err)


    def getQuizzById(self, id):
        try:
            response  =  requests.get(f"http://localhost:8080/api/quizzs/getById/{id}")
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)

    def deleteQuizz(self, id):
        try:
            response  =  requests.delete(f"http://localhost:8080/api/quizzs/delete/{id}")
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)

    def createQuizz(self):
        payload = {
            "title": self.title,
            "description": self.description,
            'student_id': self.student_id
        }
        headers = {"Content-type": "application/json" }
        try:
            response  =  requests.post("http://localhost:8080/api/quizzs/create", json=payload, headers=headers)
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)

    def updateQuizz(self, id):
        payload = {
            "title": self.title,
            "description": self.description,
            'student_id': self.student_id
        }
        headers = {"Content-type": "application/json" }
        try:
            response  =  requests.put(f"http://localhost:8080/api/quizzs/update/{id}", json=payload, headers=headers)
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)

    def deleteAllQuizz(self):
        try:
            response  =  requests.delete(f"http://localhost:8080/api/quizzs/deleteAll")
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)