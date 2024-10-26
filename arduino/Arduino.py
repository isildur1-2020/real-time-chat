#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 06:30:30 2024

@author: isildur1
"""
import os
import time
import serial

class Arduino:
    DEVICE = "/dev/cu.usbmodem1401"
    LOCKFILE = "/Users/isildur1/Documents/Isildur1/Docs/Universidad/Jorge Tadeo Lozano/QUINTO/Sistemas_Distribuidos/realtime_app/Chat/arduino/lockfile"
    
    def isBusy(self):
        if(os.path.exists(self.LOCKFILE)):
            print("Arduino is busy")
            return True
        else:
            with open(self.LOCKFILE, 'w') as lockfile:
                lockfile.write(str(os.getpid()))
            print("Arduino is ready to use")
            return False
        
    def removeLockFile(self):
        if(os.path.exists(self.LOCKFILE)):
            os.remove(self.LOCKFILE)

    def send(self, code: str):
        try:
            isBusy = self.isBusy()
            if(not isBusy):
                conn = serial.Serial(Arduino.DEVICE, 9600)
                time.sleep(2)
                conn.write((f"{code}\n").encode())
                conn.close()
                self.removeLockFile()
        except Exception as e:
            print(f"ARDUINO SEND: {e}")