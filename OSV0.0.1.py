import time
from tkinter import Tk, Label

user = "ADMIN"
window = Tk()
window.title("Welcome to PYOS")

def clock():
    while True:
        current_time = time.strftime("%H:%M:%S")
        print(current_time, end="\r")
        time.sleep(1)

print ("BIOS VER 0.0.1") 
time.sleep(1) 
print ("SEARCHING FOR BOOT DEVICES") 
time.sleep(0.5) 
print ("ssd found: 1TB ssd-PYOS") 
time.sleep(0.3) 
print ("cd-rom found: blank") 
time.sleep(1) 
print ("no other devices found") 
time.sleep(0.4) 
print ("booting from ssd") 
time.sleep(0.7) 
print ("initializing services") 
time.sleep(4)
print ("NOTICE:no GUI installed. bypassing and running in text mode")
time.sleep(0.6)
print ("welcome to PYOS" , user , "!") 
print ("more coming soon! this is only ver 0.0.1")

if __name__ == "__main__":
    try:
        clock()
    except KeyboardInterrupt:
        pass
