from database.ChatDB import ChatDB

class Observable:
    def addObserver(observer):
        pass
    def removeObserver(observer):
        pass
    def notifyObserver(observer):
        pass

class Observer:
    def update(data):
        pass

class Message(Observable):
    message: str
    clients = dict()

    def setContent(self, current_address: tuple, username: str, message: str):
        self.message = message
        ChatDB().insertMessage(username, message)
        self.notifyObservers(current_address)

    def addObserver(self, client):
        self.clients[client.client_address] = client

    def removeObserver(self, client):
        self.clients.pop(client.client_address)

    def notifyObservers(self, current_address: tuple):
        for address, client in self.clients.items():
            if address != current_address:
                message = f"{client.username} dice: {self.message}"
                client.update(message)