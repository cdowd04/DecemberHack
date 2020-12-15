import time
import webbrowser

def main():
    from datetime import datetime

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    print("Hello and good luck with school today")
    meet1 = str(input("Please enter your first class meet link: "))
    meet2 = input("Please enter your second class meet link: ")
    meet3 = input("Please enter your third class meet link: ")
    meet4 = input("Please enter your fourth class meet link: ")
    meet5 = input("Please enter your fifth class meet link: ")

main()