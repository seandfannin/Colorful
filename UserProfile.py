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

        
        
        

