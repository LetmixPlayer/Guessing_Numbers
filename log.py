import os
import sys
def init():
    a = open("log.txt", "w")
    a.close()

def log(message : str):
    a = open("log.txt", 'a')
    a.write('\n' + message)
    a.close()
    try:
        if (sys.argv[0] == "DebLet"): print(message)
    except:
        pass

def clear():
    try:
        os.remove("log.txt")
    except:
        pass