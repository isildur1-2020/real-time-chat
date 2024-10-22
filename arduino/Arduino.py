#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 06:30:30 2024

@author: isildur1
"""

import serial
import time

class Arduino:
    DEVICE = "/dev/cu.usbmodem1101"
    def __init__(self):
        self.conn = serial.Serial(self.DEVICE, 9600)
        time.sleep(2)

    def send(self, code: str):
        self.conn.write((f"{code}\n").encode())
        respuesta = self.conn.readline().decode('utf-8').strip()
        print(f"ARDUINO -> {respuesta}")
    
    def close(self):
        self.conn.close()