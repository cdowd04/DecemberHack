import time
import webbrowser

def getTime():
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def main():
    print("Good morning and welcome to google meet launcher!")
    print("The current time is: {0}".format(getTime()))

    meet1 = input("Please enter your first class meet link (make sure its the entire link): ")
    meet2 = input("Please enter your second class meet link (make sure its the entire link): ")
    meet3 = input("Please enter your third class meet link (make sure its the entire link): ")
    meet4 = input("Please enter your fourth class meet link (make sure its the entire link): ")
    meet5 = input("Please enter your fifth class meet link (make sure its the entire link): ")

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
            if (time >= "13:15:00"):  
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
            if (time >= "11:41:00"):  
                loop = False   
    else:
        print("EROR: You have entered an invalid response to the type of day schedule!!!")
    print("You are now past your last period class or you have entered an invalid response. The program will now end. Have a good day!")
main()