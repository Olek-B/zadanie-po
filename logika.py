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
    def get_user(id):
        return self.persystencja.read(id)
