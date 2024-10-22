#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 16:10:09 2024

@author: isildur1
"""

import socket
import logging

class Client:
    
    MESSAGE_SIZE = 1024
    
    def __init__(self, host, port, username):
        self.host = host
        self.port = port
        self.username = username
        self.client = None
        self.create()
        logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
        
    def create(self):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((self.host, self.port))
        except Exception as e:
            logging.info(f"CLIENT {e}")
            
    def send(self, message: str):
        try:
            customMessage = f"{self.username}:{message}"
            binaryMessage = customMessage.encode("utf-8")[:1024]
            self.client.send(binaryMessage)
        except Exception as e:
            logging.info(f"CLIENT SEND: {e}")
    
    def receive(self):
        try:
            if self.client == None: return
            while True:
                binaryMessage = self.client.recv(self.MESSAGE_SIZE)
                message = binaryMessage.decode("utf-8")
                logging.info(f"{message}")            
                if message.lower() == "cerrar":
                    break
            self.client.close()
        except Exception as e:
            logging.info(f"CLIENT RECEIVE: {e}")