import string
import persystencja

class meneger:
    def __init__(self):
        self.persystencja = persystencja.persystencja("./data.json")
        self.allowedLetters = set(string.ascii_lowercase + string.ascii_uppercase+" ")
        self.allowedGroups = set( "user", "premium", "admin")
    def add_user(self, firstName, lastName, birthYear, group):
        if set(firstName) != self.allowedLetters:
            return('nameError')
        if set(lastName) != self.allowedLetters:
            return("lastNameError")
        if birthYear.isdigit() or birthYear < 1900:
            return("birthYearError")
        if group not in self.allowedGroups:
            return("groupError")
        self.persystencja.write({"firstName":firstName,"lastName":lastName,"birthYear":birthYear,"group":group})
    def get_user(self, id):
        if self.persystencja.check(id):
            return self.persystencja.read(id)
        return("idError")
    def get_users(self):
        return self.persystencja.get_users()
    def remove_user(self,id):
        if self.persystencja.check(id):
            self.persystencja.remove_user(id)
            return True
        return("idError")
    def change_user(self, id, firstName=None, lastName=None, birthYear=None,group=None):
        if set(firstName) != self.allowedLetters and firstName != None:
            return('nameError')
        if set(lastName) != self.allowedLetters and lastName != None:
            return("lastNameError")
        if (birthYear.isdigit() or birthYear < 1900) and birthYear != None:
            return("birthYearError")
        if group not in self.allowedGroups and group != None:
            return("groupError")
        self.persystencja.change_user({"firstName":firstName,"lastName":lastName,"birthYear":birthYear,"group":group})
