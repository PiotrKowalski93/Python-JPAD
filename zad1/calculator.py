# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 12:53:53 2018

"""
import datetime
import fnmatch
import os
import sys

now = datetime.datetime.now()
today = datetime.date.today()
fileName = str(today) +str(now.hour)+'-'+str(now.minute)+'-'+str(now.second)+'.txt';

def __getFunName(x):
    return {
        0: 'dodawanie',
        1: 'odejmowanie',
        2: 'mnozenie',
        3: 'dzielenie',
        4: 'modulo'
    }.get(x, 'unknown')    
    
def __addLogToFile(operacja, wynik,a,b):
    plik = open(fileName,'a')
    plik.write('Operacja: ' +  __getFunName(operacja) + ' na liczbach: ' + str(a) + ', ' + str(b) + ', wynik: ' + str(wynik) +'\n')
    plik.close()

def add(a,b):
    __checkInputFormat(a,b)
    __addLogToFile(0,a+b,a,b)
    print('Result: ' + str(a+b))
    return a+b

def subtract(a,b):
    __checkInputFormat(a,b)
    __addLogToFile(1,a-b,a,b)
    print('Result: ' + str(a-b))
    return a-b

def multiply(a,b):
    __checkInputFormat(a,b)
    __addLogToFile(2,a*b,a,b)
    print('Result: ' + str(a*b))
    return a*b

def divide(a,b):
    __checkInputFormat(a,b)
    try:
        __addLogToFile(3,a/b,a,b)
    except ZeroDivisionError:
        print('\n Second parameter cannot be 0 !!!! \n')
        sys.exit(0)
    print('Result: ' + str(a/b))
    return a/b

def modulo(a,b):
    __checkInputFormat(a,b)
    try:
        if b==0:
            raise Exception('\n Second parameter cannot be 0 !!!! \n')
    except Exception as e:
        print(str(e))
        sys.exit(0)   
    __addLogToFile(4,a%b,a,b)
    print('Result: ' + str(a%b))
    return a%b

def readLogFile(fname=fileName):
     plik = open(fname,'r')
     print ('\n' + plik.read())
     plik.close()

def __getFileByDate(date):
    fileNameList = []
    i=1
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, str(date)+'*.txt'):
            print('file name no ' + str(i) + ': ' + file)
            fileNameList.append(file)
            i=i+1
    if len(fileNameList)==0:
        print('No logs for given date --> ' + str(date) +'\nDate format should be: YYYY-MM-DD')
    return fileNameList

def readLogsFromDate(date):
    fileNameList = __getFileByDate(date)
    for name in fileNameList:
        print('\n' + name)
        readLogFile(name)
        print (' --------------------------\n')
        
def __checkInputFormat(a,b):
    while True:
        try:
            float(a)
            float(b)
            break
        except ValueError:
            print('\n Both parameters have to be numbers!!!! \n')
            sys.exit(0)
     