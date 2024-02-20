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

    def get_users():
        ret=[]
        with open(self.plik, "r") as f:
            data=json.load(f.read())
            for i in data["users"].keys:
                ret.append({i,data["users"][i]["firstName"],data["users"][i]["lastName"],data["users"][i]["birthDate"],data["users"][i]["group"]})
        return ret

    def check(id):
        with open(self.plik, "r") as f:
            data=json.load(f.read())
            if str(id) in data["users"].keys:
                return True
            return False

    def remove_user(id):
        with open(self.plik, "r") as f:
            data=json.load(f.read())
            del data["users"][id]
            f.write(data)
