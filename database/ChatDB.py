#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 00:08:09 2024

@author: isildur1
"""
import sqlite3
import logging

class ChatDB:
    DB_NAME = "realtime_chat.db"
    def __init__(self):
        self.connect()
        logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s - %(levelname)s - %(message)s')
    
    def connect(self):
        try:
            self.conn = sqlite3.connect(self.DB_NAME)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(f"DATABASE CREATE: {e}")
    
    def dropTables(self):
        try:
            self.cursor.execute('''DROP TABLE IF EXISTS user''')
            self.cursor.execute('''DROP TABLE IF EXISTS message''')
            self.conn.commit()
        except Exception as e:
            print(f"DATABASE DROP TABLES: {e}")
        finally:
            self.conn.close()
        
    def createTables(self):
        try:
            self.cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS user (
                    id INTEGER PRIMARY KEY,
                    username VARCHAR(255) UNIQUE NOT NULL,
                    password VARCHAR(255) NOT NULL
                )
                '''
            )
            self.cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS message (
                    id INTEGER PRIMARY KEY,
                    username TEXT,
                    message TEXT
                )
                '''
            )
            self.conn.commit()
        except Exception as e:
            print(f"DATABASE TABLES: {e}")
        finally:
            self.conn.close()
        
    def insertUser(self, username, password):
        try:
            self.cursor.execute(
                '''
                INSERT INTO user (username, password)
                VALUES (?, ?)
                ''', (username, password))
            self.conn.commit()
        except sqlite3.IntegrityError:
            raise Exception("Error: Usuario existente")
        except Exception as e:
            raise Exception(f"DATABASE INSERT USER: {e}")
        finally:
            self.conn.close()
            
    def insertMessage(self, username, message):
        try:
            self.cursor.execute(
                '''
                INSERT INTO message (username, message)
                VALUES (?, ?)
                ''', (username, message))
            self.conn.commit()
        except Exception as e:
            print(f"DATABASE INSERT MESSAGE: {e}")
        finally:
            self.conn.close()
    
    def getUsers(self):
        self.cursor.execute('SELECT * FROM user')
        users = self.cursor.fetchall()
        return users

    def getUserByCredentials(self, username, password):
        try:
            self.cursor.execute(
                '''
                SELECT * FROM user
                WHERE username = ? AND password = ?
                ''',
                (username, password)
            )
            userFound = self.cursor.fetchall()
            return userFound
        except Exception as e:
            print(f"DATABASE GET USER BY CREDENTIALS: {e}")
            return None
        finally:
            self.conn.close()

    def getMessages(self):
        try:
            self.cursor.execute('SELECT * FROM message')
            messages = self.cursor.fetchall()
            return messages[:10]
        except Exception as e:
            print(f"GET MESSAGES: {e}")
            return []

    def printMessageHistory(self):
        messages = self.getMessages()
        for message in messages:
            customMessage = f"{message[1]} dijo: {message[2]}"
            logging.info(customMessage)
        self.conn.close()
