#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 06:46:15 2024

@author: isildur1
"""
from utils.Args import Args
from auth.Login import Login
from threading import Thread
from utils.Logger import Logger
from client.Client import Client
from database.ChatDB import ChatDB

def main():
    PORT = Args.getFirst()
    try:
        username = Login().handle()
    except Exception as e:
        Logger.log(e)
        return
    client = Client(PORT, username)
    
    recv_proc = Thread(target=client.receive)
    recv_proc.start()
    
    firstTime = True
    while True:
        if firstTime: ChatDB().printMessageHistory()
        message = input("Escribe algo: ")
        if message != "": client.send(message)
        firstTime = False
    
if __name__ == "__main__":
    main()