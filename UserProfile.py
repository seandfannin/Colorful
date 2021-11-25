from easygui import *

class UserProfile:
    def __init__(self, fileName):
        self.fileName = fileName #file name should be
        
    def getFileName(self):
        return self.fileName
    
        
    def create(self, name, birthday, userName, password, address, \
               email, therapist,tEmail, emContactName,emContactNumber):
        profile = open(self.fileName, "w")
        
        profile.write("Name: " + name + "\n")
        profile.write("Birthday: " +birthday + "\n")
        profile.write("Address: "+address+ "\n")
        profile.write("User Name: " + userName+"\n")
        profile.write("Password: " + password +"\n")
        profile.write("Email: " + email +"\n")
        profile.write("Emergency Contact Name: " + emContactName + "\n")
        profile.write("Emergency Phone Number: " + emContactNumber + "\n")
        profile.write("Therapist: " + therapist + "\n")
        profile.write("Therapist email: " + tEmail +"\n")
        profile.write("\n")
        profile.close()
        
    def  Log(self, entry,date):
        profile = open(self.fileName, "a")
        profile.write(date + "\n")
        profile.write(entry)
        profile.write("\n")
        profile.close()
        
    def view(self):
        profile= open(self.fileName, "r")
        contents = profile.read()
        print(contents)#Prints the content for viewing later
        profile.close
        
    def copy(self):
        profile = open(self.fileName, "r")
        copy = open("Copy.txt","w")
        for line in profile:#used to make a copy of the  file to prepare to send
            copy.write(line)
            
        profile.close()
        copy.close()
def start():
    choices = ["Create profile", "Log in"]
    msg = "Welcome to Colorful!"
    reply = buttonbox(msg,"Colorful",choices)
    if(reply == "Create profile"):
        msg = "Enter your personal information"
        title = "User Profile"
        fieldNames = ["name", "birthday", "userName", "password", "address","email", "Therapist","Therapist Email", "emContactName","EmContactNumber"]
        fieldValues = []  # we start with blanks for the values
        fieldValues = multenterbox(msg,title, fieldNames)
        profile = UserProfile(fieldValues[0]+".txt")
        profile.create(fieldValues[0],fieldValues[1],fieldValues[2],fieldValues[3],fieldValues[4],fieldValues[5],fieldValues[6],fieldValues[7],fieldValues[8],fieldValues[9])
        message = ""
        title = "How do you feel?"
        output = textbox(message,title)
        profile.log(output)
        #Need to get the userprofile creation to work correctly.
    
    

start()
        
    
    
        
        

