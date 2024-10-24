from utils.Args import Args
from threading import Thread
from server.SocketServer import SocketServer
from server.ClientConnection import ClientConnection
from server.Message import Message
    
def main():
    try:
        PORT = Args.getFirst()
        server = SocketServer(PORT).create()
        observeMessage = Message()
        while True:
            currentClient = ClientConnection(server.accept(), observeMessage)
            observeMessage.addObserver(currentClient)
            thread = Thread(target=currentClient.handle)
            thread.start()
    except Exception as err:
        print(f"Create server error: {err}")
        
if __name__ == "__main__":
    main()