#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 16:10:09 2024

@author: isildur1
"""
import sys
import socket
from utils.Logger import Logger

class Client:
    MESSAGE_SIZE = 1024
    DEFAULT_HOST = "127.0.0.1"
    CLOSE_SIGNAL = "cerrar"
    
    def __init__(self, port, username, host = DEFAULT_HOST):
        self.port = port
        self.username = username
        self.host = host
        self.client = None
        self.create()
        
    def create(self):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((self.host, self.port))
        except Exception as e:
            Logger.log(f"CLIENT {e}")
            
    def send(self, message: str):
        try:
            customMessage = f"{self.username}:{message}"
            binaryMessage = customMessage.encode("utf-8")[:1024]
            self.client.send(binaryMessage)
        except Exception as e:
            Logger.log(f"CLIENT SEND: {e}")
    
    def receive(self, open_thread):
        try:
            if self.client == None: return
            while True:
                binaryMessage = self.client.recv(self.MESSAGE_SIZE)
                message = binaryMessage.decode("utf-8")
                Logger.log(f"{message}")
                if(message.lower() == self.CLOSE_SIGNAL):
                    Logger.log("CLOSING CURRENT CLIENTE")
                    self.client.close()
                    open_thread[0] = False
        except Exception as e:
            Logger.log(f"CLIENT RECEIVE: {e}")