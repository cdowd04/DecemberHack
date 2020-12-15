import time
import webbrowser

def getTime():
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def main():
    print("Good morning and welcome to google meet launcher!")
    print(getTime())

    meet1 = input("Please enter your first class meet link: ")
    meet2 = input("Please enter your second class meet link: ")
    meet3 = input("Please enter your third class meet link: ")
    meet4 = input("Please enter your fourth class meet link: ")
    meet5 = input("Please enter your fifth class meet link: ")

    loop = True
    schedule = input("Is today a half day or full day? (Type \'h\' or \'f\' respectively): ")
    if (schedule == 'f' or schedule =='F'):
        print("The program is now running and will open your google meet links at the right class schedule. Please do not close the program.")
        while(loop):
            time = getTime()
            if (time == "07:45:00"):
                webbrowser.open(meet1, new = 2)
            if (time == "08:52:00"):
                webbrowser.open(meet2, new = 2)
            if (time == "09:59:00"):
                webbrowser.open(meet3, new = 2)
            if (time == "12:07:00"):
                webbrowser.open(meet4, new = 2)
            if (time == "13:14:00"):
                webbrowser.open(meet5, new = 2)
                loop = False
    elif (schedule == 'h' or schedule =='H'):
        print("The program is now running and will open your google meet links at the right class schedule. Please do not close the program.")
        while(loop):
            time = getTime()
            if (time == "08:00:00"):
                webbrowser.open(meet1, new = 2)
            if (time == "08:52:00"):
                webbrowser.open(meet2, new = 2)
            if (time == "09:42:00"):
                webbrowser.open(meet3, new = 2)
            if (time == "10:50:00"):
                webbrowser.open(meet4, new = 2)
            if (time == "11:40:00"):
                webbrowser.open(meet5, new = 2)
                loop = False    
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    print("Your school day is now over or you have entered an invalid response resulting in an error. The program will now end. Have a good day!")
main()