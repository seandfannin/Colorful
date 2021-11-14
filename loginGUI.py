#Jade Hudgins
#11/13/2021
#Login w/ GUI
#In progress

from easygui import * #GUI

def login():
    title = "Login"
    text = "Username"
    text2 = "Passcode"
    d_text = ""
    
    username = enterbox(text, title, d_text)
    passcode = enterbox(text2,title,d_text)
    length = len(passcode)
    
    while length < 4 or length > 4:
        title = "Login"
        msg = "Invalid passcode. Please try again."
        passcode = enterbox(text2,title,d_text)
        length = len(passcode)
    
    message = "Login Successful"
    output = msgbox(message, title)
        
login()
