#High Tech Virtual Helper made by Edmond Niu and Cian Dowd

import time as t
import webbrowser
import re

#checks current time and returns it as an int (eg. 7:45:23 would return as 74523)
def getTime():
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S") 
    stringWithoutColon = ''
    for char in current_time:
        if (current_time.index(char) !=2 and current_time.index(char) !=5):
            stringWithoutColon += char
    return int(stringWithoutColon)


#Opens the file and extracts the links, returned in a list format
def openFile():
    f = open('links.txt','r') #opens the text file
    links = []
    for line in f: #iterates through the text file
        line = line.rstrip()
        x = re.findall('.*Period\s*\d:\s*(\S+).*', line) #regular expressions function designed to extract just the link
        if (len(x)>0):
            links.append(x)
    return links #returns a list of links

def main():
    
    #print welcome message
    print("Good morning and welcome to google meet launcher! Make sure your google meet links are in the links.txt file")
    print("The current time is: {0}".format(getTime()))

    #gathers list of class links
    links = openFile()

    loop = True
    schedule = input("Is today a half day or full day? (Type \'h\' or \'f\' respectively): ") #Asks user for bell schedule (half or full)
    
    #full day schedule
    if (schedule == 'f' or schedule =='F'):
        print("The program is now running and will open your google meet links at the right class schedule. Please do not close the program.")
        
        #checks at minute intervals until the time of the first class is reached; then opens up the first meet link
        while(loop):
            time = getTime()
            if (time > 74400 and time <74500):
                webbrowser.open(links[0][0], new = 2)
            t.sleep(60)
            loop = False
        
        #waits 67 (or 127 min for lunch break) minutes before opening the next link in the user's browser (67 = time between full day high tech periods)
        t.sleep(4020)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(4020)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(7620)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(4020)
        webbrowser.open(links[4][0], new = 2)

    #half day schedule
    elif (schedule == 'h' or schedule =='H'):
        print("The program is now running and will open your google meet links at the right class schedule. Please do not close the program.")
        
        #checks at minute intervals until the time of the first class is reached; then opens up the first meet link
        while(loop):
            time = getTime()
            if (time > 75900  and time <80000):
                webbrowser.open(links[0][0], new = 2)
            t.sleep(60)
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")
            loop = False
        
        #waits 51 minutes before opening the next link in the user's browser (51 = time between half day high tech periods)
        t.sleep(3060)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(4260)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3060)
        webbrowser.open(links[4][0], new = 2)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    
    #print program end and credits messages
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
    print("Project by: Cian & Edmond")

main()