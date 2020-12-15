#waits between periods

import time as t
import webbrowser
import re

def getTime():
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S") 
    stringWithoutColon = ''
    for char in current_time:
        if (current_time.index(char) !=2 and current_time.index(char) !=5):
            stringWithoutColon += char
    return int(stringWithoutColon)


def openFile():
    f = open('file.txt','r')
    links = []
    for line in f:
        line = line.rstrip()
        x = re.findall('.*Period\s*\d:\s*(\S+).*', line)
        if (len(x)>0):
            links.append(x)
    return links

def main():
    
    print("Good morning and welcome to google meet launcher!")
    print("The current time is: {0}".format(getTime()))

    links = openFile()

    loop = True
    schedule = input("Is today a half day or full day? (Type \'h\' or \'f\' respectively): ")
    if (schedule == 'f' or schedule =='F'):
        print("The program is now running and will open your google meet links at the right class schedule. Please do not close the program.")
        while(loop):
            time = getTime()
            if (time > 74400 and time <74500):
                webbrowser.open(links[0][0], new = 2)
            t.sleep(60)
            loop = False
        
        t.sleep(3900)
        webbrowser.open(links[1][0], new = 2)
        t.sleep(3900)
        webbrowser.open(links[2][0], new = 2)
        t.sleep(3900)
        webbrowser.open(links[3][0], new = 2)
        t.sleep(3900)
        webbrowser.open(links[4][0], new = 2)


         
            
    elif (schedule == 'h' or schedule =='H'):
        print("The program is now running and will open your google meet links at the right class schedule. Please do not close the program.")
        while(loop):
            time = getTime()
            if (time == "08:00:00"):
                webbrowser.open(links[0][0], new = 2)
            if (time == "08:52:00"):
                webbrowser.open(links[1][0], new = 2)
            if (time == "09:42:00"):
                webbrowser.open(links[2][0], new = 2)
            if (time == "10:50:00"):
                webbrowser.open(links[3][0], new = 2)
            if (time == "11:40:00"):
                webbrowser.open(links[4][0], new = 2)
            if (time >= "11:41:00"):  
                loop = False   
            time.sleep(60)
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")

main()