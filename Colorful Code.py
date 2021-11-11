import random #random generator
from PIL import Image #Image opener
import easygui import * #GUI

#Rewards, Finished
def rewards():
    #Rewards is a "glue" type of function that will have the ability to call each of the rewards available.
    #The indiividual rewards are accessable on the homepage as well as after the user logs about their emotions

    #Start of Code:
    print("Congratulations on completing your log!!!")
    print("Would you like a reward?")
    print("Type Y for yes!")
    print("Type N for no!\n")
    
    #Yes or no choice of user
    choice = getYN()
    if choice == "N":
        print("Have a nice day!")
    elif choice == "Y":
        homePage()
    else:
        while choice != "N" or choice != "Y":
            print("Invalid Choice!")
            print("Would you like a reward?")
            print("Type Y for yes!")
            print("Type N for no!\n")
        
            choice = getYN()
            if choice == "N":
                print("Have a nice day!")
            elif choice == "Y":
                homePage()

#Getting choice of user, not integer
def getYN():
    return input("Enter your choice: ").upper()

#Getting choice of user
def getChoice():
    return int(input("Enter your choice: "))

#Invalid Input, loop to choice again?
def invalidInput():
    print("That is not a valid input. Returning to the Homepage!\n")
    homePage()

#Homepage
def homePage():
    print("WELCOME TO COLORFUL!")
    print(compliment)
    print(compChall)
    print("Where would you like to go?\n")
    print("1 for a list of hotlines.")
    print("2 for an inspriational quote.")
    print("3 for a funny video.")
    print("4 for a song.")
    print("5 for a meme or joke.")
    
    choice = getChoice()
    if choice == 1:
        hotline()
    elif choice == 2:
        quotes()
    elif choice == 3:
        videos()
    elif choice == 4:
        songs()
    elif choice == 5:
        memeJoke()
    else:
        invalidInput()
#End of HomePage

#Hotline
def hotline():
    #Hotline numbers can be accessed through the homepage. If the user is in need of a hotline number,
    #then the user can click on the hotline box
    #The user will then get a list of the same hotline numbers that are listed in the SRS paper.

    #Start of Code:
    #List of hotline numbers from the SRS Paper
    print("www.suicidepreventionlifeline.org")
    print("24/7 Crisis Hotline: National Suicide Prevention Lifeline Network (1-800-237-TALK (8255) - Veterans press 1)")
    print("Crisis Text Line (text “TALK” to 741-741)")
    print("Veterans Crisis Line (text to 838255)")
    print("Vets4Warriors (1-855-838-8255)")
    print("SAMHSA Treatment Referral Hotline (Substance Abuse - 1-800-662-HELP (4357))")
    print("RAINN National Sexual Assault Hotline (1-800-656-HOPE (4673))")
    print("National Teen Dating Abuse Helpline (1-866-331-9474)")
    print("The Trevor Project (1-866-488-7386 or text “START” to 678678)")
    print("Trans Lifeline (877-565-8860 for US and 877-330-6366 for Canada)")
    print("National Domestic Violence Hotline (call 1-800-799-7233 or log onto thehotline.org or text “LOVEIS” to 22522)")
    print("StrongHearts Native Helpline (call 1-844-762-8483)\n")
    
    #User has option to go back to the homepage
    print("Press 1 to go back to the homepage!")
    choice = getChoice()
    if choice == 1:
        homePage()
    else:
        invalidInput()
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
        print("Believe you can and you're already halfway there. -Theodore Roosevelt\n")
    elif compQuote == 2:
        print("All our dreams can come true if we have the courage to pursue them. -Walt Disney\n")
    elif compQuote == 3:
        print("Don't worry if you're not where you want to be yet. Great things take time. -Unknown\n")
    elif compQuote == 4:
        print("Be thankful for what you have - you'll end up having more. -Oprah\n")
    elif compQuote == 5:
        print("You are the artist of your own life. Don't hand the paintbrush to anyone else. -Unknown\n")
    elif compQuote == 6:
        print("Strive for progress. Not perfection. - Unknown\n")
    elif compQuote == 7:
        print("Just believe in yourself. Even if you don't, pretend that you do and, at some point, you will. -Venus Williams\n")
    elif compQuote == 8:
        print("Life is like riding a bicycle. To keep your balance, you must keep moving. -Albert Einstein\n")
    elif compQuote == 9:
        print("Happiness is not by chance, but by choice. -Jim Rohn\n")
    elif compQuote == 10:
        print("You're much stronger than you think you are. Trust me. -Superman\n")
    else:
        return "error"
    
    #Printing random quote
    #print(compQuote)
        
    #User has option to go back to the homepage or another quote
    print("Press 1 to go back to the homepage!")
    print("Press 2 to get another quote!")
    choice = getChoice()
    if choice == 1:
        homePage()
    elif choice == 2:
        quotes()
    else:
        invalidInput()
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
    print("Here is the 'how to' view the videos!")
    print("When you get your video rewards, open up a web browser!")
    print("Then, copy and paste the link provided into the search bar!")
    print("After that, press Enter and enjoy the reward!\n")
    
    #Video options
    if compVideo == 1:
        print("Parkour Panda: https://vm.tiktok.com/ZM8jq3hsN/")
    elif compVideo == 2:
        print("Pep-Talk 1: https://vm.tiktok.com/ZM8jqgsWN/")
    elif compVideo == 3:
        print("Tiny Puppy Bark: https://vm.tiktok.com/ZM8jqbnG1/")
    elif compVideo == 4:
        print("Pep-Talk 2: https://vm.tiktok.com/ZM8jqtXB9/")
    elif compVideo == 5:
        print("Pep-Talk 3: https://vm.tiktok.com/ZM8jqcLvq/")
    elif compVideo == 6:
        print("Movie Intro: https://vm.tiktok.com/ZM8jbdpco/")
    elif compVideo == 7:
        print("Super Mario Cat: https://vm.tiktok.com/ZM8jqpQ9b/")
    elif compVideo == 8:
        print("Goat: https://vm.tiktok.com/ZM8jqp4B9/")
    elif compVideo == 9:
        print("Funny Car Noise: https://vm.tiktok.com/ZM8jqbPVe/")
    elif compVideo == 10:
        print("Cat VS Bean bag: https://vm.tiktok.com/ZM8jqE6YT/")
    elif compVideo == 11:
        print("Fluffy Dog: https://vm.tiktok.com/ZM8jqg8MN/")
    elif compVideo == 12:
        print("Horse Mask: https://vm.tiktok.com/ZM8jbd75U/")
    elif compVideo == 13:
        print("Dog is on the way: https://vm.tiktok.com/ZM8jqoUGv/")
    else:
        return "error"
    
    #Printing random video
    #print(compVideo)
        
    #User has option to go back to the homepage or another video
    print("Press 1 to go back to the homepage!")
    print("Press 2 to get another video!")
    choice = getChoice()
    if choice == 1:
        homePage()
    elif choice == 2:
        videos()
    else:
        invalidInput()
#End of Videos

#Songs
def songs():
    #Songs is one of the avaliable rewards. If the user wishes to have an uplighting song to brighten their day,
    #The software will provide a random song from a list with at least 10 different songs.

    #Start of Code:
    #Picks a random uplighting song numbered 1-17
    compSong = random.randint(1,17)
    
    #Song options
    #Links to songs?
    if compSong == 1:
        print("Dynamite by BTS")
        print("Time: 3:19")
        print("Genre: K-Pop\n")
    elif compSong == 2:
        print("People Help the People by Birdy")
        print("Time: 4:17")
        print("Genre: Alternative\n")
    elif compSong == 3:
        print("Something Wild (feat. Andrew McHanon in the Wilderness) by Lindsey Stirling")
        print("Time: 3:45")
        print("Genre: Dance\n")
    elif compSong == 4:
        print("Permission to Dance by BTS")
        print("Time: 3:08")
        print("Genre: K-Pop\n")
    elif compSong == 5:
        print("Fight Song by Rachel Platten")
        print("Time: 3:24")
        print("Genre: Pop\n")
    elif compSong == 6:
        print("All Star by Smash Mouth")
        print("Time: 3:20")
        print("Genre: Alternative\n")
    elif compSong == 7:
        print("Believer by Imagine Dragons")
        print("Time: 3:24")
        print("Genre: Alternative\n")
    elif compSong == 8:
        print("If I Ruled the World (feat. Iyaz) by Big Time Rush")
        print("Time: 3:00")
        print("Genre: Pop\n")
    elif compSong == 9:
        print("Here I Am (End Title) by Brian Adams")
        print("Time: 4:45")
        print("Genre: Soundtrack\n")
    elif compSong == 10:
        print("The Middle by Jimmy Eat World")
        print("Time: 2:53")
        print("Genre: Alternative\n")
    elif compSong == 11:
        print("Classic by MKTO")
        print("Time: 2:53")
        print("Genre: \n")
    elif compSong == 12:
        print("Rocketeer by Far East Movement & Ryan Tedder")
        print("Time: 3:30")
        print("Genre: \n")
    elif compSong == 13:
        print("Dance Again (feat. Pitbull) by Jennifer Lopez")
        print("Time: 3:46")
        print("Genre: \n")
    elif compSong == 14:
        print("Alone Togeter by Fall Out Boy")
        print("Time: 3:21")
        print("Genre: Alternative\n")
    elif compSong == 15:
        print("Good Times by All Time Low")
        print("Time: 3:44")
        print("Genre: \n")
    elif compSong == 16:
        print("Dear Maria, Count Me In by All Time Low")
        print("Time: 3:01")
        print("Genre: \n")
    elif compSong == 17:
        print("The Feels by TWICE")
        print("Time: 3:52")
        print("Genre: K-Pop\n")
    else:
        return "error"
    
    #Printing random song
    #print(compSong)
    
    #User has option to go back to the homepage or another song
    print("Press 1 to go back to the homepage!")
    print("Press 2 to get another song!")
    choice = getChoice()
    if choice == 1:
        homePage()
    elif choice == 2:
        songs()
    else:
        invalidInput()
#End of Songs
        
#Memes & Jokes
def memeJoke():
    #memeJoke is one of the avaliable rewards. If the user wishes to have a funny joke or meme to make them smile.
    #The software will provide a random meme or joke from a list with at least 10 different jokes and memes.
    
    #Start of Code:
    #Picks a random funny meme or joke numbered 1-21
    compMemeJoke = random.randint(1,21)
    
    #Meme or Joke options
    #11 Jokes
    if compMemeJoke == 1:
        print("What do you call a boomerang that won't come back? -A stick!\n")
    elif compMemeJoke == 2:
        print("Why are piggy banks so wise? -They're filled with common cents.\n")
    elif compMemeJoke == 3:
        print("Why couldn't the bicycle stand up by itself? -It was two-tired.\n")
    elif compMemeJoke == 4:
        print("How do celebrities stay cool? -They have many fans.\n")
    elif compMemeJoke == 5:
        print("What did the baby corn say to the mama corn? -Where's POPcorn?\n")
    elif compMemeJoke == 6:
        print("Why do pancakes always win at baseball? -Because they have the best batter.\n")
    elif compMemeJoke == 7:
        print("Want to hear a pizza joke? -Nevermind, it's too cheesy.\n")
    elif compMemeJoke == 8:
        print("I ordered a chicken and an egg on Amazon. -I'll let you know.\n")
    elif compMemeJoke == 9:
        print("How does a penguin build it's house? -Igloos it together.\n")
    elif compMemeJoke == 10:
        print("What do you call a fake noodle? -Impasta!\n")
    elif compMemeJoke == 11:
        print("Whats the differenece between a piano, tuna, and a tube of glue?")
        print("-You can tune a piano but you cant tune a tuna.")
        print("Now you might be asking where the glue is?")
        print("-You may get stuck on that.\n")
        
    #10 Memes
        #In order for pictures to open, you must copy the who path to the meme pictures
        #If not, then it will not work
    elif compMemeJoke == 12:
        meme12 = Image.open(r"C:\Users\brian\Pictures\CS 253 Memes\dog.JPG")
        meme12.show()
    elif compMemeJoke == 13:
        meme13 = Image.open(r"C:\Users\brian\Pictures\CS 253 Memes\worth loving.jpg")
        meme13.show()
    elif compMemeJoke == 14:
        meme14 = Image.open(r"C:\Users\brian\Pictures\CS 253 Memes\rat.jpg")
        meme14.show()
    elif compMemeJoke == 15:
        meme15 = Image.open(r"C:\Users\brian\Pictures\CS 253 Memes\kitty crime.jpg")
        meme15.show()
    elif compMemeJoke == 16:
        meme16 = Image.open(r"C:\Users\brian\Pictures\CS 253 Memes\kitty toy.jpg")
        meme16.show()
    elif compMemeJoke == 17:
        meme17 = Image.open(r"C:\Users\brian\Pictures\CS 253 Memes\kakuna rattata.jpg")
        meme17.show()
    elif compMemeJoke == 18:
        meme18 = Image.open(r"C:\Users\brian\Pictures\CS 253 Memes\yoda.jpg")
        meme18.show()
    elif compMemeJoke == 19:
        meme19 = Image.open(r"C:\Users\brian\Pictures\CS 253 Memes\jimin.jpg")
        meme19.show()
    elif compMemeJoke == 20:
        meme20 = Image.open(r"C:\Users\brian\Pictures\CS 253 Memes\taeyong.jpg")
        meme20.show()
    elif compMemeJoke == 21:
        meme21 = Image.open(r"C:\Users\brian\Pictures\CS 253 Memes\yee haw.jpg")
        meme21.show()
    else:
        return "error"
    
    #Printing random meme or joke
    #print(compMemeJoke)
    
    #User has option to go back to the homepage or another song
    print("Press 1 to go back to the homepage!")
    print("Press 2 to get another meme or joke!")
    choice = getChoice()
    if choice == 1:
        homePage()
    elif choice == 2:
        memeJoke()
    else:
        invalidInput()   
 #End of MemeJoke

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
