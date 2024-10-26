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
from arduino.Arduino import Arduino
from arduino.constants import LOGIN_ERROR, LOGIN_SUCESS

def main():
    open_thread = [True]
    PORT = Args.getFirst()
    try:
        username = Login().handle()
        Arduino().send(LOGIN_SUCESS)
    except Exception as e:
        Logger.log(e)
        Arduino().send(LOGIN_ERROR)
        return
    client = Client(PORT, username)
    recv_proc = Thread(target=client.receive, args=(open_thread,))
    recv_proc.start()
    firstTime = True
    while open_thread[0]:
        if firstTime: ChatDB().printMessageHistory()
        message = input("Escribe algo: ")
        if message != "": client.send(message)
        firstTime = False
    
if __name__ == "__main__":
    main()