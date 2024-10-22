from threading import Thread
from server.SocketServer import SocketServer
from server.ClientConnection import ClientConnection
    
def main():
    clients = list()
    server = SocketServer(8000).create()
    while True:
        currentClient = ClientConnection(server.accept(), clients)
        clients.append(currentClient)
        thread = Thread(target=currentClient.handle)
        thread.start()
        
if __name__ == "__main__":
    main()