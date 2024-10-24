from database.ChatDB import ChatDB

class Login:
    NO_EXISTS_USER = 'n'
    EXIST_USER = "Y"

    def __init__(self):
        self.userExists = None
        self.username = ""
        self.password = ""

    def handleInput(self):
        while self.userExists not in [self.NO_EXISTS_USER, self.EXIST_USER]:
            self.userExists = input("Tiene un usuario creado? (Y/n): ")
        self.username = input("Ingrese su usuario: ")
        self.password = input("Ingrese su contraseña: ")

    def createUser(self):
        ChatDB().insertUser(self.username, self.password)
    
    def compareInfo(self):
        userFound = ChatDB().getUserByCredentials(self.username, self.password)
        if len(userFound) == 0 or userFound == None:
            raise Exception("Usuario inexistente")

    def handle(self):
        try:
            self.handleInput()
            if self.userExists == self.NO_EXISTS_USER:
                self.createUser()
            elif self.userExists == self.EXIST_USER:
                self.compareInfo()
            return self.username
        except Exception as e:
            raise Exception(f"{e}")