import time
import skilstak.colors as c
print(c.clear)
def hello(message): 
    print(c.red + 'Hello ' + message + c.reset)
    time.sleep(0.1)
def nyan(message):
    while True:
        print(c.rc() + "Hello, " + message, end = " ")
def multi(message):
    while True:
        print(c.clear + c.multi(message))
