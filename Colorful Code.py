import random #random generator
import re
#from PIL import Image #Image opener
from easygui import * #GUI

#Rewards, Finished
def rewards():
    #Rewards is a "glue" type of function that will have the ability to call each of the rewards available.
    #The indiividual rewards are accessable on the homepage as well as after the user logs about their emotions

    #Start of Code:
    #Message box
    msg = "Congratulations on completing your log!!!\n Would you like a reward?"
    title = "Please confirm"
    if ynbox(msg, title): 
        homePage()
    else:
        if ccbox("Have a nice day!", "Confirm"):
            pass

#Getting choice of user, not integer
def getYN():
    return input("Enter your choice: ").upper()

#Getting choice of user
def getChoice():
    return int(input("Enter your choice: "))

#Invalid Input
def invalidInput():
    print("That is not a valid input. Returning to the Homepage!\n")
    homePage()

#Homepage
def homePage():  
    #Message box
    compliments()
    challenge()
    msg = (("WELCOME TO COLORFUL!\n") + ("Where would you like to go?"))
    title = "Homepage"
    choices = ["Hotlines", "Quotes", "Videos", "Songs", "Memes", "Jokes"]
    choice = buttonbox(msg, title, choices)
    if choice == "Hotlines":
        hotline()
    elif choice == "Quotes":
        quotes()
    elif choice == "Videos":
        videos()
    elif choice == "Songs":
        songs()
    elif choice == "Memes":
        memes()
    elif choice == "Jokes":
        jokes()
    else:
        return "error"
#End of HomePage

#Hotline, Finished
def hotline():
    #Hotline numbers can be accessed through the homepage. If the user is in need of a hotline number,
    #then the user can click on the hotline box
    #The user will then get a list of the same hotline numbers that are listed in the SRS paper.

    #Start of Code:
    #List of hotline numbers from the SRS Paper
    message = (("www.suicidepreventionlifeline.org\n") + ("24/7 Crisis Hotline: National Suicide Prevention Lifeline Network (1-800-237-TALK (8255) - Veterans press 1)\n") +
               ("Crisis Text Line (text “TALK” to 741-741)\n") + ("Veterans Crisis Line (text to 838255)\n") + ("Vets4Warriors (1-855-838-8255)\n") + 
               ("SAMHSA Treatment Referral Hotline (Substance Abuse - 1-800-662-HELP (4357))\n") + ("RAINN National Sexual Assault Hotline (1-800-656-HOPE (4673))\n") +
               ("National Teen Dating Abuse Helpline (1-866-331-9474)\n") + ("The Trevor Project (1-866-488-7386 or text “START” to 678678)\n") +
               ("Trans Lifeline (877-565-8860 for US and 877-330-6366 for Canada)\n") +
               ("National Domestic Violence Hotline (call 1-800-799-7233 or log onto thehotline.org or text “LOVEIS” to 22522)\n") +
               ("StrongHearts Native Helpline (call 1-844-762-8483)\n"))
    
    #Message box
    #User has option to go back to the homepage
    title = "Hotlines"
    choices = ["Homepage"]
    choice = buttonbox(message, title, choices)
    if choice == "Homepage":
        homePage()
    else:
        return "error"
#End of Hotlines

#Quotes
def quotes():
    #Quotes is one of the avaliable rewards. If the user wishes to have an inspirational quote to brighten their day,
    #The the software will provide a random quote from a list with at least 10 different quotes.

    #Start of Code:
    #Picks a random inspirational quote numbered 1-10
    compQuote = random.randint(1,10)
    
    #Quote options
    if compQuote == 1:
        message = ("Believe you can and you're already halfway there. -Theodore Roosevelt\n")
    elif compQuote == 2:
        message = ("All our dreams can come true if we have the courage to pursue them. -Walt Disney\n")
    elif compQuote == 3:
        message = ("Don't worry if you're not where you want to be yet. Great things take time. -Unknown\n")
    elif compQuote == 4:
        message = ("Be thankful for what you have - you'll end up having more. -Oprah\n")
    elif compQuote == 5:
        message = ("You are the artist of your own life. Don't hand the paintbrush to anyone else. -Unknown\n")
    elif compQuote == 6:
        message = ("Strive for progress. Not perfection. - Unknown\n")
    elif compQuote == 7:
        message = ("Just believe in yourself. Even if you don't, pretend that you do and, at some point, you will. -Venus Williams\n")
    elif compQuote == 8:
        message = ("Life is like riding a bicycle. To keep your balance, you must keep moving. -Albert Einstein\n")
    elif compQuote == 9:
        message = ("Happiness is not by chance, but by choice. -Jim Rohn\n")
    elif compQuote == 10:
        message = ("You're much stronger than you think you are. Trust me. -Superman\n")
    else:
        return "error"
    
    #Message box
    #User has option to go back to the homepage or another quote
    title = "Quotes"
    choices = ["Quotes", "Homepage"]
    choice = buttonbox(message, title, choices)
    if choice == "Quotes":
        quotes()
    elif choice == "Homepage":
        homePage()
    else:
        return "error"
#End of Quotes

#Videos
def videos():
    #Videos is one of the avaliable rewards. If the user wishes to have a funny
        #video to brighten their day,
    #The software will provide a random video from a list with at least 10 different videos.

    #Start of Code:
    #Picks a random funny video numbered 1-13
    compVideo = random.randint(1,13)
    
    #Instruction to use videos
    #print("Here is the 'how to' view the videos!")
    #print("When you get your video rewards, open up a web browser!")
    #print("Then, copy and paste the link provided into the search bar!")
    #print("After that, press Enter and enjoy the reward!\n")
    
    #Video options
    if compVideo == 1:
        message = ("Parkour Panda: https://vm.tiktok.com/ZM8jq3hsN/")
    elif compVideo == 2:
        message = ("Pep-Talk 1: https://vm.tiktok.com/ZM8jqgsWN/")
    elif compVideo == 3:
        message = ("Tiny Puppy Bark: https://vm.tiktok.com/ZM8jqbnG1/")
    elif compVideo == 4:
        message = ("Pep-Talk 2: https://vm.tiktok.com/ZM8jqtXB9/")
    elif compVideo == 5:
        message = ("Pep-Talk 3: https://vm.tiktok.com/ZM8jqcLvq/")
    elif compVideo == 6:
        message = ("Movie Intro: https://vm.tiktok.com/ZM8jbdpco/")
    elif compVideo == 7:
        message = ("Super Mario Cat: https://vm.tiktok.com/ZM8jqpQ9b/")
    elif compVideo == 8:
        message = ("Goat: https://vm.tiktok.com/ZM8jqp4B9/")
    elif compVideo == 9:
        message = ("Funny Car Noise: https://vm.tiktok.com/ZM8jqbPVe/")
    elif compVideo == 10:
        message = ("Cat VS Bean bag: https://vm.tiktok.com/ZM8jqE6YT/")
    elif compVideo == 11:
        message = ("Fluffy Dog: https://vm.tiktok.com/ZM8jqg8MN/")
    elif compVideo == 12:
        message = ("Horse Mask: https://vm.tiktok.com/ZM8jbd75U/")
    elif compVideo == 13:
        message = ("Dog is on the way: https://vm.tiktok.com/ZM8jqoUGv/")
    else:
        return "error"
    
    #Message box
    #User has option to go back to the homepage or another video
    title = "Videos"
    choices = ["Videos", "Homepage"]
    choice = buttonbox(message, title, choices)
    if choice == "Videos":
        videos()
    elif choice == "Homepage":
        homePage()
    else:
        return "error"
#End of Videos

#Songs
def songs():
    #Songs is one of the avaliable rewards. If the user wishes to have an uplighting song to brighten their day,
    #The software will provide a random song from a list with at least 10 different songs.

    #Start of Code:
    #Picks a random uplighting song numbered 1-17
    compSong = random.randint(1,17)
    
    #Song options
    if compSong == 1:
        message = ("Dynamite by BTS, Time: 3:19, Genre: K-Pop")
    elif compSong == 2:
        message = ("People Help the People by Birdy, Time: 4:17, Genre: Alternative")
    elif compSong == 3:
        message = ("Something Wild (feat. Andrew McHanon in the Wilderness) by Lindsey Stirling, Time: 3:45, Genre: Dance")
    elif compSong == 4:
        message = ("Permission to Dance by BTS, Time: 3:08, Genre: K-Pop")
    elif compSong == 5:
        message = ("Fight Song by Rachel Platten, Time: 3:24, Genre: Pop")
    elif compSong == 6:
        message = ("All Star by Smash Mouth, Time: 3:20, Genre: Alternative")
    elif compSong == 7:
        message = ("Believer by Imagine Dragons, Time: 3:24, Genre: Alternative")
    elif compSong == 8:
        message = ("If I Ruled the World (feat. Iyaz) by Big Time Rush, Time: 3:00, Genre: Pop")
    elif compSong == 9:
        message = ("Here I Am (End Title) by Brian Adams, Time: 4:45, Genre: Soundtrack")
    elif compSong == 10:
        message = ("The Middle by Jimmy Eat World, Time: 2:53, Genre: Alternative")
    elif compSong == 11:
        message = ("Classic by MKTO, Time: 2:53, Genre: Pop")
    elif compSong == 12:
        message = ("Rocketeer by Far East Movement & Ryan Tedder, Time: 3:30, Genre: Pop")
    elif compSong == 13:
        message = ("Dance Again (feat. Pitbull) by Jennifer Lopez, Time: 3:46, Genre: Pop")
    elif compSong == 14:
        message = ("Alone Togeter by Fall Out Boy, Time: 3:21, Genre: Alternative")
    elif compSong == 15:
        message = ("Good Times by All Time Low, Time: 3:44, Genre: Alternative")
    elif compSong == 16:
        message = ("Dear Maria, Count Me In by All Time Low, Time: 3:01, Genre: Alternative")
    elif compSong == 17:
        message = ("The Feels by TWICE, Time: 3:52, Genre: K-Pop")
    else:
        return "error"
    
    #Message box
    #User has option to go back to the homepage or another song
    title = "Songs"
    choices = ["Songs", "Homepage"]
    choice = buttonbox(message, title, choices)
    if choice == "Songs":
        songs()
    elif choice == "Homepage":
        homePage()
    else:
        return "error"
#End of Songs
        
#Jokes, Finished
def jokes():
    #Joke is one of the avaliable rewards. If the user wishes to have a funny joke to make them smile.
    #The software will provide a random joke from a list with at least 10 different jokes.
    
    #Start of Code:
    #Picks a random funny joke numbered 1-11
    compJoke = random.randint(1,11)
    
    #Joke options
    #11 Jokes
    if compJoke == 1:
        message = ("What do you call a boomerang that won't come back? -A stick!\n")
    elif compJoke == 2:
        message = ("Why are piggy banks so wise? -They're filled with common cents.\n")
    elif compJoke == 3:
        message = ("Why couldn't the bicycle stand up by itself? -It was two-tired.\n")
    elif compJoke == 4:
        message = ("How do celebrities stay cool? -They have many fans.\n")
    elif compJoke == 5:
        message = ("What did the baby corn say to the mama corn? -Where's POPcorn?\n")
    elif compJoke == 6:
        message = ("Why do pancakes always win at baseball? -Because they have the best batter.\n")
    elif compJoke == 7:
        message = ("Want to hear a pizza joke? -Nevermind, it's too cheesy.\n")
    elif compJoke == 8:
        message = ("I ordered a chicken and an egg on Amazon. -I'll let you know.\n")
    elif compJoke == 9:
        message = ("How does a penguin build it's house? -Igloos it together.\n")
    elif compJoke == 10:
        message = ("What do you call a fake noodle? -Impasta!\n")
    elif compJoke == 11:
        message = (("Whats the differenece between a piano, tuna, and a tube of glue?") + ("-You can tune a piano but you cant tune a tuna.") +
                   ("Now you might be asking where the glue is?") + ("-You may get stuck on that.\n"))
    else:
        return "error"

    #Message box
    #User has option to go back to the homepage or another joke
    title = "Jokes"
    choices = ["Jokes", "Homepage"]
    choice = buttonbox(message, title, choices)
    if choice == "Jokes":
        jokes()
    elif choice == "Homepage":
        homePage()
    else:
        return "error"
#End of Jokes

#Memes, Finished
def memes():
    #Meme is one of the avaliable rewards. If the user wishes to have a funny meme to make them smile.
    #The software will provide a random meme from a list with at least 10 different memes.
    
    #Start of Code:
    #Picks a random funny meme numbered 1-10
    compMeme = random.randint(1,10)
    
    #10 Memes
        #In order for pictures to open, you MUST copy the WHOLE path to the meme pictures
        #If not, then it will not work
    if compMeme == 1:
        image = (r"C:\Users\brian\Pictures\CS 253 Memes\dog.JPG")
        message = "Dog"
    elif compMeme == 2:
        image = (r"C:\Users\brian\Pictures\CS 253 Memes\worth loving.jpg")
        message = "Worth Loving"
    elif compMeme == 3:
        image = (r"C:\Users\brian\Pictures\CS 253 Memes\rat.jpg")
        message = "Rat"
    elif compMeme == 4:
        image = (r"C:\Users\brian\Pictures\CS 253 Memes\kitty crime.jpg")
        message = "Kitty Crime"
    elif compMeme == 5:
        image = (r"C:\Users\brian\Pictures\CS 253 Memes\kitty toy.jpg")
        message = "Kitty Toy"
    elif compMeme == 6:
        image = (r"C:\Users\brian\Pictures\CS 253 Memes\kakuna rattata.jpg")
        message = "Kakuna Rattata"
    elif compMeme == 7:
        image = (r"C:\Users\brian\Pictures\CS 253 Memes\yoda.jpg")
        message = "Yoda"
    elif compMeme == 8:
        image = (r"C:\Users\brian\Pictures\CS 253 Memes\jimin.jpg")
        message = "Jimin"
    elif compMeme == 9:
        image = (r"C:\Users\brian\Pictures\CS 253 Memes\taeyong.jpg")
        message = "Taeyong"
    elif compMeme == 10:
        image = (r"C:\Users\brian\Pictures\CS 253 Memes\yee haw.jpg")
        message = "Yee Haw"
    else:
        return "error"
    
    #Message box
    #User has option to go back to the homepage or another meme
    title = "Memes"
    choices = ["Memes", "Homepage"]
    choice = buttonbox(message, title, image=image, choices=choices)
    if choice == "Memes":
        memes()
    elif choice == "Homepage":
        homePage()
    else:
        return "error" 
 #End of Memes

#Beginning of Daily Compliment    
    # This is the compliments randomizer.
    #    This randomizer gives a random compliment.
    #    This is a two-part randomizer, based loosely on the mind of
    #    when we would program dice randomizers.
    
def complimentRandomizer():
    # This is just the randomizer. Nothing too special, moving along.
    return random.randint(1,10)

def compliments():
    # This is where the magic happens.
    #    The complimentRandomizer function gets called here.
    
    compliment = complimentRandomizer()
    print("Daily Compliment: ")
    
    # Then, based on the computer randomization,
    #    the program prints a different compliment!
    
    if compliment == 1:
        message = ("You look stellar today!")
        
    elif compliment == 2:
        message = ("You're incredibly smart, you can do anything you put your mind to!")
        
    elif compliment == 3:
        message = ("You're so kind!")
        
    elif compliment == 4:
        message = ("You light up the room!")
        
    elif compliment == 5:
        message = ("You're someone's reason to smile!")
        
    elif compliment == 6:
        message = ("You're an inspiration!")
        
    elif compliment == 7:
        message = ("You're making a difference!")
        
    elif compliment == 8:
        message = ("You are enough!")
        
    elif compliment == 9:
        message = ("You're something really special!")
        
    elif compliment == 10:
        message = ("You are perfect just the way you are!")
      
    # Fail-safe, just in case.
    else:
        message = ("Error")
        
    #Outputs the daily compliment
    output = msgbox(message)
  #End of compliement

#Daily Challenege
def challenge():
    #Present at least 10 healthy challenges for the user to try
    #The user can't change this

    #Start fo code:
        #Picks a random inspirational quote numbered 1-10
    compChall = random.randint(1,10)
    
    #Challenge options
    if compChall == 1:
        message = ("Take a 10 minute walk!\n")
    elif compChall == 2:
        message = ("Drink 8 bottles of water today!\n")
    elif compChall == 3:
        message = ("Read a chapter of a book!\n")
    elif compChall == 4:
        message = ("Take some deep breaths!\n")
    elif compChall == 5:
        message = ("Take a cat nap!\n")
    elif compChall == 6:
        message = ("Color a picture!\n")
    elif compChall == 7:
        message = ("Write down a list of things you are greatful for!\n")
    elif compChall == 8:
        message = ("Take a bubble bath!\n")
    elif compChall == 9:
        message = ("Do some yoga!\n")
    elif compChall == 10:
        message = ("Look in the mirror and say,'I am valuable and worthy!'\n")
    else:
        return "error"
    
    #Printing random challenge
    #print(compChall)
    
    #Outputs the daily challenge
    output = msgbox(message)

#User Profile Code

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
        
    def Log(self, entry,date):
        profile = open(self.fileName, "a")
        profile.write(date + "\n")
        profile.write(entry)
        profile.write("\n")
        profile.close()
        
    def view(self):
        profile= open(self.fileName, "r")
        contents = profile.read()
        print(contents)#Prints the content for viewing later
        profile.close()
        
    def copy(self):
        profile = open(self.fileName, "r")
        copy = open("Copy.txt","w")
        for line in profile:#used to make a copy of the  file to prepare to send
            copy.write(line)
            
        profile.close()
        copy.close()
        
    def happinessRate(self):#I added this to the userProfile Class so that way it will write to the correct file ~Sean
    
    # This is the output file, where it will record the user's input.
    #    Again, for testing purposes the name is still "out.txt"
    

        outputFile = open(self.fileName, "a", encoding="utf-8")
    
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
        
#Hannah Lawson
#Complete

from uszipcode import Zipcode, SearchEngine, SimpleZipcode
#from easygui import *

    
def zipCode():
    text = "Enter zipcode"
    title = "Zipcode"
    d_text = ""

    userZip = enterbox(text, title, d_text)
   # userZip= input("Enter your zipcode: ")
    search = SearchEngine()
    zipcode = search.by_zipcode(userZip)
    city= zipcode.major_city
    #print(city)
    
#prints out name and phone number
# for local therapist
#only a few places, can add more later
    
    if city== "Daniels" or city== "Beckley":
        message=("Laurel Mountain Psychological, Inc  \n (304)-894-8930")
    elif city== "Princeton" or city=="Athens":
        message=("The Gibson Counseling Center \n (304)-487-9996")
    elif city== "Martinsburg" or city=="Shepherdstown":
        message=("Psychological Consulting Inc \n (304)-263-9095")        
    elif city== "Bluefield":
        message=("Brain Matters Therapy \n (276)-970-9747")
    elif city== "Wheeling" or city=="Weirton":
        message=("Muir Robin \n (304)-233-1200")        
    elif city== "Charleston" or city== "Saint Albans":
        message=("KPCC Counseling \n (304)-346-9689")
    elif city== "Morgantown":
        message=("Fremouw-Sigley Psychological \n (304)-598-2300")        
    elif city== "Tazewell" or city== "Cedar Bluff":
        message=("Carilion Clinic \n (276)-988-8765")
    elif city== "Bastian" or city== "Pearisburg":
        message=("Bland County Medical Clinic \n (276)-688-4331")
    else: 
        message=("Try another close city")
    
        
    msg = ("City: "+ city + "  " + message)
    title = "Therapist Search!"
    choices = ["Back to Homepage!", "Try Again"]
    choice = buttonbox(msg, title, choices)
    if choice == "Back to Homepage!":
        homePage()
    elif choice == "Try Again":
        zipCode()
    else:
        zipCode()        
        


        
def start():
    choices = ["Create profile", "Login"]
    msg = "Welcome to Colorful!"
    reply = buttonbox(msg,"Colorful",choices)
    if(reply == "Create profile"):
        msg = "Enter your personal information"
        title = "User Profile"
        fieldNames = ["name", "birthday", "userName", "password", "address","email", "Therapist","Therapist Email", "emContactName","EmContactNumber"]
        fieldValues = []  # we start with blanks for the values
        fieldValues = multenterbox(msg,title, fieldNames)
        profile = UserProfile(fieldValues[2]+".txt")#using the username to create the profile
        profile.create(fieldValues[0],fieldValues[1],fieldValues[2],fieldValues[3],fieldValues[4],fieldValues[5],fieldValues[6],fieldValues[7],fieldValues[8],fieldValues[9])
        profile.happinessRate()
        message = ""
        title = "How do you feel?"
        output = textbox(message,title)
        profile.Log(output)
        
        #Trigger Search
        items=['hurt','burden','kill','hate living','no one loves me','lonely','knife',
        'gun','rope','hanging','unimportant','panic','dead','anxious','killed','scared',
        'overwhelmed','tense','pain','abandon','control','rejected','betrayed',
        'disappointment','insecure'] #words you are looking for

        file=open(fieldValues[2] + '.txt','r')# May change txt file
        content=file.read()
        #save the read output so the reading always starts from begining
        for i in items:
            lis=re.findall(i,content)
            if len(lis)==0:
                print('Not Found')
            elif len(lis)==1:
                print('Found Once')
            elif len(lis)==2:
                print('Found Twice')
            else:
                print('Found',len(lis),'times')
                
    elif(reply == "Login"):
        title2 = "Login"
        text = "Username"
        text2 = "Passcode"
        d_text = ""
    
        username = enterbox(text, title2, d_text)
        passcode = enterbox(text2,title2,d_text)
        length = len(passcode)
    
        while length < 4 or length > 4:
            title = "Login"
            msg2 = "Invalid passcode. Please try again."
            passcode = enterbox(text2,title2,d_text)
            length = len(passcode)
            
    
    
    message2 = "Login Successful"
    outputSuccess = msgbox(message2, title2)
    
    choices2 = ["Yes","No"]
    msg3 = "Would you like to make a log?"
    reply2 = buttonbox(msg3,"Colorful",choices2)
    if (reply2 == "Yes"):
        date = enterbox("what is today's date?", "Colorful","Date:")
        profile = UserProfile(username + ".txt")
        profile.happinessRate()
        message3 = ""
        title = "How do you feel?"
        output2 = textbox(message3,title)
        profile.Log(output2,date)
        rewards()
        
    elif (reply2 == "No"):
        homePage()

 

start()
 
