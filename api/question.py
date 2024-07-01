import requests


class Question(object):
    def __init__(self, question_text="", quiz_id=0):
        self.question_text = question_text
        self.quiz_id = quiz_id
    
    async def getQuestion(self):
        try:
            response  =  requests.get("http://localhost:8080/api/questions/get")
            print(response.json())
            return  response.json()
        except requests.ConnectionError as err:
            print(err)


    async def getQuestionById(self, id):
        try:
            response  =  requests.get(f"http://localhost:8080/api/questions/getById/{id}")
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)

    async def deleteQuestion(self, id):
        try:
            response  =  requests.delete(f"http://localhost:8080/api/questions/delete/{id}")
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)

    async def createQuestion(self):
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

    async def updateQuestion(self, id):
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

    async def deleteAllQuestion(self):
        try:
            response  =  requests.delete(f"http://localhost:8080/api/questions/deleteAll")
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)