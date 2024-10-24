#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:05:37 2024

@author: isildur1
"""
import socket
from server.Message import Message

class ClientConnection:
    MESSAGE_SIZE = 1024
    CLOSE_SIGNAL = "cerrar"
    
    def __init__(self, socketObject: tuple, observeMessage: Message ):
        self.username = ''
        self.observeMessage = observeMessage
        self.client_socket: socket.socket = socketObject[0]
        self.client_address = socketObject[1]
        self.printEvent("CONNECTED")
        
    def setUsername(self, username):
        self.username = username
        
    def sendMessage(self, msg: str) -> None:
        try:
            binaryMessage = msg.encode("utf-8")
            self.client_socket.send(binaryMessage)
        except Exception as e:
            print(f"SEND MESSAGE: {e}")

    def decodeMessage(self, binaryMessage: bytes):
        decodedMessage = binaryMessage.decode("utf-8")
        username, message = decodedMessage.split(":")
        return username, message
            
    def handle(self) -> str:
        try:
            while True:
                binaryMessage = self.client_socket.recv(self.MESSAGE_SIZE)
                username, message = self.decodeMessage(binaryMessage)
                if self.username == '': self.setUsername(username)
                if(message.lower() == self.CLOSE_SIGNAL):
                    self.observeMessage.removeObserver(self)
                    self.sendMessage(self.CLOSE_SIGNAL)
                    break
                self.observeMessage.setContent(self.client_address, username, message)
        except Exception as e:
            print(f"RECEIVE MESSAGE: {e}")
        
    def update(self, message):
        self.sendMessage(message)
    
    def getAddress(self):
        return f"{self.client_address[0]}:{self.client_address[1]}"
        
    def printEvent(self, event, payload = None):
        print("-------------------------------------------------------------")
        print(f"{self.getAddress()} -> {event}")
        if payload != None:
            print(f"PAYLOAD: {payload}")
        print("-------------------------------------------------------------")