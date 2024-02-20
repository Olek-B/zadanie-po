import string

class meneger():
    def __init__(self, plik_persystencji):
        self.persystencja = plik_persystencji
        self.allowedLetters = set(string.ascii_lowercase + string.ascii_uppercase+" ")
        self.allowedGroups = set( "user", "premium", "admin")
    def add_user(self, firstName, lastName, birthYear, group):
        if set(firstName) != self.allowedLetters:
            return('nameError')
        if set(lastName) != self.allowedLetters:
            return("lastNameError")
        if birtYear.isdigit() or birthYear < 1900:
            return("birthYearError")
        if group not in self.allowedGroups:
            return("groupError")
        with open(self.persystencja,"w") as f:
            data=f.read()
