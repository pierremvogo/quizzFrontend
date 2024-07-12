import requests


class Answer(object):
    def __init__(self, answer_text="", is_correct=False, question_id=0, student_id=0):
        self.answer_text = answer_text
        self.is_correct = is_correct
        self.question_id = question_id
        self.student_id = student_id
    
    def getAnswer(self):
        try:
            response  =  requests.get("http://localhost:8080/api/answers/get")
            print(response.json())
            return  response.json()
        except requests.ConnectionError as err:
            print(err)

    def getAnswersByPagination(self,offset):
        try:
            response  =  requests.get(f"http://localhost:8080/api/answers/get/pagination/{offset}")
            return  response.json()
        except requests.ConnectionError as err:
            print(err)

    def countAnswer(self):
        try:
            response  =  requests.get(f"http://localhost:8080/api/answers/count")
            return  response.json()
        except requests.ConnectionError as err:
            print(err)


    def getAnswerById(self, id):
        try:
            response  =  requests.get(f"http://localhost:8080/api/answers/getById/{id}")
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)

    def getAnswerByQuestionId(self, id):
        try:
            response  =  requests.get(f"http://localhost:8080/api/answers/getByQuestionId/{id}")
            return response.json()
        except requests.ConnectionError as err:
            print(err)

    def deleteAnswer(self, id):
        try:
            response  =  requests.delete(f"http://localhost:8080/api/answers/delete/{id}")
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)

    def createAnswer(self):
        payload = {
            "answer_text" :  self.answer_text, 
            "is_correct" :   self.is_correct,
            "question_id" : self.question_id
        }
        headers = {"Content-type": "application/json" }
        try:
            response  =  requests.post("http://localhost:8080/api/answers/create", json=payload, headers=headers)
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)

    def updateAnswer(self, id):
        payload = {
            "answer_text" :  self.answer_text, 
            "is_correct" :   self.is_correct,
        }
        headers = {"Content-type": "application/json" }
        try:
            response  =  requests.put(f"http://localhost:8080/api/answers/update/{id}", json=payload, headers=headers)
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)

    async def deleteAllAnswer(self):
        try:
            response  =  requests.delete(f"http://localhost:8080/api/answers/deleteAll")
            print(response.json())
            return response.json()
        except requests.ConnectionError as err:
            print(err)