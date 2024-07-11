import requests


class Question(object):
    def __init__(self, question_text="", quiz_id=0):
        self.question_text = question_text
        self.quiz_id = quiz_id
    
    def getQuestion(self):
        try:
            response  =  requests.get("http://localhost:8080/api/questions/get")
            print(response.json())
            return  response.json()
        except requests.ConnectionError as err:
            print(err)


    def getQuestionById(self, id):
        try:
            response  =  requests.get(f"http://localhost:8080/api/questions/getById/{id}")
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)

    def deleteQuestion(self, id):
        try:
            response  =  requests.delete(f"http://localhost:8080/api/questions/delete/{id}")
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)

    def getQuestionsByPagination(self,offset):
        try:
            response  =  requests.get(f"http://localhost:8080/api/questions/get/pagination/{offset}")
            return  response.json()
        except requests.ConnectionError as err:
            print(err)

    def countQuestion(self):
        try:
            response  =  requests.get(f"http://localhost:8080/api/questions/count")
            return  response.json()
        except requests.ConnectionError as err:
            print(err)

    def createQuestion(self):
        payload = {
            "question_text": self.question_text,
            'quiz_id': self.quiz_id
        }
        headers = {"Content-type": "application/json" }
        try:
            response  =  requests.post("http://localhost:8080/api/questions/create", json=payload, headers=headers)
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)

    def updateQuestion(self, id):
        payload = {
            "question_text": self.question_text,
            'quiz_id': self.quiz_id
        }
        headers = {"Content-type": "application/json" }
        try:
            response  =  requests.put(f"http://localhost:8080/api/questions/update/{id}", json=payload, headers=headers)
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)

    def deleteAllQuestion(self):
        try:
            response  =  requests.delete(f"http://localhost:8080/api/questions/deleteAll")
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)