import random #random generator
from PIL import Image #Image opener
import easygui import * #GUI

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
    msg = (("WELCOME TO COLORFUL!\n") + ("Where would you like to go?") + (compliment) + (compChall))
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
    title = "Qoutes"
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
    
    # Login function; finished-ish
def login():
    
    # This is the actual passcode login function
    #    For good measure, I decided to ask for the username
    #    as well, so that way the file reader can check
    #    for matching information.
    
    inputFileName = "out.txt"
    inputFile = open(inputFileName, "r", encoding="utf-8")
    
    userName = input("Username: ")
    passcode = int(input("Passcode: "))
