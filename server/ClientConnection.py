#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:05:37 2024

@author: isildur1
"""
import socket
from database.ChatDB import ChatDB

class ClientConnection:
    MESSAGE_SIZE = 1024
    CLOSE_SIGNAL = "cerrar"
    
    def __init__(self, socketObject: tuple, clients: list['ClientConnection']):
        self.username = ''
        self.clients = clients
        self.client_socket: socket.socket = socketObject[0]
        self.client_address = socketObject[1]
        self.printEvent("NEW CONNECTION")
        
    def setUsername(self, username):
        self.username = username
        
    def sendMessage(self, msg: str) -> None:
        try:
            binaryMessage = msg.encode("utf-8")
            self.client_socket.send(binaryMessage)
        except Exception as e:
            print(f"SEND MESSAGE: {e}")

    def sendBroadcast(self, clients: list, message: str):
        message = f"{self.username} dice: {message}"
        print(message)
        for client in clients:
            if client != self:
                client.sendMessage(message)

    def decodeMessage(self, binaryMessage: bytes):
        decodedMessage = binaryMessage.decode("utf-8")
        username, message = decodedMessage.split(":")
        return username, message
            
    def handle(self) -> str:
        try:
            db = ChatDB() 
            while True:
                binaryMessage = self.client_socket.recv(self.MESSAGE_SIZE)
                username, message = self.decodeMessage(binaryMessage)
                if self.username == '': self.setUsername(username)

                if(message.lower() == self.CLOSE_SIGNAL):
                    break
                self.sendBroadcast(self.clients, message)
                db.insertMessage(self.username, message)
        except Exception as e:
            print(f"RECEIVE MESSAGE: {e}")
        finally:
            self.client_socket.close()
        
    def printEvent(self, event, payload = None):
        print("-------------------------------------------------------------")
        print(f"{self.client_address[0]}:{self.client_address[1]} -> {event}")
        if payload != None:
            print(f"PAYLOAD: {payload}")
        print("-------------------------------------------------------------")