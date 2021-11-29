from easygui import *

def happinessRate():
    
    # This is the output file, where it will record the user's input.
    #    Again, for testing purposes the name is still "out.txt"
    
    outputFileName = "out.txt"
    outputFile = open(outputFileName, "w", encoding="utf-8")
    
    # This is where the user will input their mood rating.
    
    msg = (("Please rate your happiness on a scale from one to ten!") + (" One is the lowest, and ten is the highest."))
    title = "Happiness Rating"
    choices = ["1","2","3","4","5","6","7","8","9","10"]
    choice = buttonbox(msg,title,choices)
    
    if choice == "1":
        outputFile.write("Today's Rating: ")
        outputFile.write(choice)
        
    elif choice == "2":
        outputFile.write("Today's Rating: ")
        outputFile.write(choice)
        
    elif choice == "3":
        outputFile.write("Today's Rating: ")
        outputFile.write(choice)
        
    elif choice == "4":
        outputFile.write("Today's Rating: ")
        outputFile.write(choice)
        
    elif choice == "5":
        outputFile.write("Today's Rating: ")
        outputFile.write(choice)
        
    elif choice == "6":
        outputFile.write("Today's Rating: ")
        outputFile.write(choice)
        
    elif choice == "7":
        outputFile.write("Today's Rating: ")
        outputFile.write(choice)
        
    elif choice == "8":
        outputFile.write("Today's Rating: ")
        outputFile.write(choice)
        
    elif choice == "9":
        outputFile.write("Today's Rating: ")
        outputFile.write(choice)
        
    elif choice == "10":
        outputFile.write("Today's Rating: ")
        outputFile.write(choice)
    
    outputFile.close()
