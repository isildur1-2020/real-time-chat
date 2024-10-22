#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 06:46:15 2024

@author: isildur1
"""
from client.Client import Client
from threading import Thread
from database.ChatDB import ChatDB
import logging

def login():
    try:
        db = ChatDB()
        userExists = None
        while userExists != "Y" and userExists != "n":
            userExists = input("Tiene un usuario creado? (Y/n): ")
        username = input("Ingrese su usuario: ")
        password = input("Ingrese su contraseña: ")
        if userExists == "n":
            db.insertUser(username, password)
        else:
            userFound = db.getUserByCredentials(username, password)
            if len(userFound) == 0:
                raise Exception("Usuario inexistente")
        return username
    except Exception as e:
        raise Exception(f"{e}")

def main():
    firstTime = True
    #arduino_conn = Arduino()
    logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        username = login()
       # arduino_conn.send("Bienvenido")
    except Exception as e:
        logging.info(e)
       # arduino_conn.send("Error")
        return
    
    client = Client("127.0.0.1", 8000, username)
    
    recv_proc = Thread(target=client.receive)
    recv_proc.start()
    
    while True:
        if firstTime:
            db = ChatDB()
            messages = db.getMessages()
            for message in messages:
                customMessage = f"{message[1]} dijo: {message[2]}"
                logging.info(customMessage)
                
        message = input("Escribe un mensaje: ")
        if message != "":
            client.send(message)
        
        firstTime = False
        
    recv_proc.join()
    
if __name__ == "__main__":
    main()