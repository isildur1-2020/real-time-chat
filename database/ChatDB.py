#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 00:08:09 2024

@author: isildur1
"""

import sqlite3

class ChatDB:
    
    def __init__(self):
        self.create()
        # self.dropTables()
        self.createTables()
    
    def create(self):
        try:
            self.conn = sqlite3.connect('realtime_chat.db')
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
        
    def insertUser(self, username, password):
        try:
            self.cursor.execute(
                '''
                INSERT INTO user (username, password)
                VALUES (?, ?)
                ''', (username, password))
            self.conn.commit()
        except Exception as e:
            raise Exception(f"DATABASE INSERT USER: {e}")
            
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
            
    def getMessages(self):
        self.cursor.execute('SELECT * FROM message')
        messages = self.cursor.fetchall()
        return messages
    
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
                ''', (username, password))
            userFound = self.cursor.fetchall()
            return userFound
        except Exception as e:
            print(f"DATABASE GET USER BY CREDENTIALS: {e}")
