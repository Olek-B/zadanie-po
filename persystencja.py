import json

class persystencja:
    def __init__(self, plik_persystencji):
        self.plik = plik_persystencji
    def write(dane):
        with open(self.plik,'rw') as f:
            data=json.load(f.read())
            data["users"][data["newest"]] = dane
            data["last"]=data["last"]+1
            f.write(data)
    def read(self,id):
        with open(self.plik, "r") as f:
            data=json.load(f.read())
            return data["users"][str(id)]
