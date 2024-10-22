#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:01:14 2024

@author: isildur1
"""
import socket

class SocketServer:
    FAMILY = socket.AF_INET
    TYPE = socket.SOCK_STREAM
    DEFAULT_HOST = "127.0.0.1"

    def __init__(self, port: int, host: str = DEFAULT_HOST, backlog: int = 0):
        self.host = host
        self.port = port
        self.backlog = backlog

    def create(self) -> socket.socket:
        try:
            server = socket.socket(self.FAMILY, self.TYPE)
            server.bind((self.host, self.port))
            server.listen(self.backlog)
            print("---------------------------------------")
            print(f"LISTENING ON: {self.host}:{self.port}\n")
            return server
        except Exception as e:
            print(f"SERVER: {e}")
            return None