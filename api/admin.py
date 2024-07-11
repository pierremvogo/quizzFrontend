import requests

class Admin:
    def __init__(self):
         pass
 
    def getAdminByCode(self, code):
            try:
                response  =  requests.get(f"http://localhost:8080/api/admin/getByCode/{code}")
                print(response.json())
                return response.json()
            except requests.HTTPError as err:
                return err
            except requests.JSONDecodeError as err:
                 return err
            except requests.ConnectionError as err:
                 return err