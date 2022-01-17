
from typing import Counter
import time
import art
import random
title=art.text2art("Omar: Class President")
print (title)
print ("RING RING, Omar slowly crawls out of his bed. Omar does not like waking up in the morning. ")
print ("You head to school")
print ("You and Charlie walk into the classroom. The teacher says that there is a new position that students can run for.")
time.sleep(1)
print ( "It is called the class president, and they are elected by their fellow students. Charlie tells you that you would make a great class president.")
time.sleep(1)
choices={"posters", "debate"}
electionscore=0

while len(choices) > 0:
    userchoice=input (" There are two ways of increasing your odds of winning, putting up posters or working on your debate skills. Would you like to put up posters or work on debate skills? ")
    if "poster" in userchoice.lower() and "posters" in choices: 
        extrafalses=[False,False,False,False,False,False,False,False,False]
        start_time=time.time()
        seconds=20
        userpoints=0
        anagram=["kind","kid","kiss","kin","in","sin","send","sink","nine"]
        print ("If you have an large vocubarly you are able to pack more of an punch. You will be provided with an word and will have to find as many words that you can create using the letter of that word in 15 seconds. This will change the number of posters you get. Type a word at time and quickly because you only have 15 seconds. ")
        time.sleep(1.5)
        start_time=time.time()
        elapsed_time=0
        while elapsed_time < seconds:
            elapsed_time=time.time()-start_time
            if elapsed_time < seconds:
                print("You have spent " + str(int(elapsed_time))  + " seconds")
            userinput=input ("What many words can you make with Kindness: ")
            if userinput.lower() in anagram:
                    print ("You got an word")
                    userpoints+=1
                    anagram.remove(userinput)
        posterstatus=extrafalses[0:userpoints]
        print ("Game Over! You got", userpoints, "words")
        # posterstatus.append(extraposters)
        print ("You will get", len(posterstatus), "Posters") 
        position = 0
        poster="something"
        postercounter=len(posterstatus)
        print ("There is before you a hallway, with bullentin boards for you to put posters up between each room. ")
        while postercounter>0:
            poster=input("Do you want to put an poster up? Yes or No ")
            if "yes" in poster.lower() and posterstatus[position] is False:
                print("You put up the poster")
                posterstatus[position]=True
                postercounter+=-1
            elif "no" in poster.lower():
                print ("You decide not to put up an poster.")
            elif "yes" in poster.lower() and posterstatus[position] is True:
                print ("That spot is filled with an poster")
            else:
                print ("Not an Valid Answer. You did not put up a poster!")
            userposition=input("Would you like to go down this hallway. Forwards or Backwards: ")
            if postercounter==0: 
                print ("You put up all of the posters!")
            elif "forwards" in userposition.lower():
                print ("You moved forwards")
                position+=1
            elif "backwards" in userposition.lower():
                print ("You moved backwards")
                position-=1
            else:
                print ("That is not an valid response. You have not moved.")
        if position==-1: 
            print ("You got bored and deciced to leave the hallway")
        electionscore=(posterstatus.count(True))*2
        choices.remove("posters")
    elif "debate" in userchoice.lower() and "debate" in choices:   
        start_time=time.time()
        seconds=10
        userpoints=0
        listA=["1F600", "1F606",'1F4A3', "1F4AC"]
        listB=["1F643", "1F4A3", "1F605","1F602"]
        listC=["1F917", "1F610", "1F644", "1F925"]
        listD=["1F925", "1F976", "1F92F", "1F60E"]
        listE=["1F61F", "1F633", "1F628", "1F62D"]
        listF=["1F631","1F61E","1F62B", "1F628"]
        counter=0
        secondcounter=0
        emojicounter=1
        numberofgames=3
        userpoints=3
        print ("In an debate, you need to be quick on your feet. Now you will play an emoji verison of the game Spot! There are two lists of emoji's with one emoji being shared between both lines.  ")
        time.sleep(2)
        start_time=time.time()
        elapsed_time=0
        while elapsed_time < seconds:
            while numberofgames!=0 and userpoints==numberofgames:
                if numberofgames==3:
                    list1=listA
                    list2=listB
                    answer=3
                elif numberofgames==2:
                    list1=listC
                    list2=listD
                    answer=4
                else:
                    list1=listE
                    list2=listF
                    answer=3
                print ("First Group: ")
                while counter!=4:
                    list1[counter]=int(list1[counter],16) 
                    print (emojicounter, chr(list1[counter]))
                    counter+=1
                    emojicounter+=1
                print ("Second Group: ")
                if counter==4:
                    while secondcounter!=4:
                        list2[secondcounter]=int(list2[secondcounter],16)
                        print (chr(list2[secondcounter]))
                        secondcounter+=1
                        emojicounter+=1
                userguess=int(input ("What is the number of of the emoji in the first group?: "))
                elapsed_time=time.time()-start_time
                while userguess != answer: 
                    print("that is not the correct answer")
                    userguess=int(input ("What is the number of of the emoji in the first group?: "))
                    elapsed_time=time.time()-start_time
                print ("Good Job")
                userpoints+=-1
                userinput=()
                secondcounter=0
                counter=0
                emojicounter=1
                numberofgames+=-1
            elapsed_time=time.time()-start_time
        print("You have spent: " + str(int(elapsed_time))  + " seconds")
        if elapsed_time>seconds and numberofgames==0:
            print ("You beat all of the games!")
        elif elapsed_time>seconds:
            print ("You ran out of time")
        elif numberofgames==0:
            print ("You beat all of the games!")
        if userpoints==3:
            electionscore+=0
        if userpoints==2:
            electionscore+=5
        if userpoints==1:
            electionscore+=10
        if userpoints==0:
            electionscore+=15
        choices.remove("debate")
    elif "poster" in userchoice.lower():
        print ("You have already played that game.")
    elif "debate" in userchoice.lower():
        print ("You have already played that game.")
    else:
        print ("Not an valid answer! Poster or Debate")
print ("Today is the election day, you are excited and scared as all of the students put together their votes. ")
time.sleep(.5)
print ("The teacher calls you away and tells you that you have: ")
time.sleep(2)
election=random.randint(1,30)
if electionscore>=election:
    print ("YOU HAVE WON THE ELECTION!!!")
elif electionscore<election:
    print ("You have lost the election, the teacher tells you that you were close to winning.")

        
                    
        



