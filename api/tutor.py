import requests

class Tutor:
    def __init__(self):
         pass
 
    def getTutorByCode(self, code):
            try:
                response  =  requests.get(f"http://localhost:8080/api/tutor/getByCode/{code}")
                print(response.json())
                return response.json()
            except requests.HTTPError as err:
                return err
            except requests.JSONDecodeError as err:
                 return err
            except requests.ConnectionError as err:
                 return err