from database.ChatDB import ChatDB
from arduino.Arduino import Arduino
from arduino.constants import numberMessage, LOGIN_SUCESS
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

    def printClientsConnected(self):
        connectedClients = len(self.clients.keys())
        print(f"CONNECTED CLIENTS {connectedClients}")
        if(connectedClients % 2 == 0):
            Arduino().send(LOGIN_SUCESS)
        Arduino().send(numberMessage(connectedClients))

    def addObserver(self, client):
        self.clients[client.client_address] = client
        self.printClientsConnected()

    def removeObserver(self, client):
        self.clients.pop(client.client_address)
        self.printClientsConnected()

    def notifyObservers(self, current_address: tuple):
        for address, client in self.clients.items():
            if address != current_address:
                message = f"{client.username} dice: {self.message}"
                client.update(message)