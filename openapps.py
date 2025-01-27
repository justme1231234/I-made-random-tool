import subprocess
import os
import json


logo = """
 █████    ██████   ██████    ███████████      ███████████
░░███    ░░██████ ██████    ░░███░░░░░███    ░█░░░███░░░█
 ░███     ░███░█████░███     ░███    ░███    ░   ░███  ░ 
 ░███     ░███░░███ ░███     ░██████████         ░███    
 ░███     ░███ ░░░  ░███     ░███░░░░░███        ░███    
 ░███     ░███      ░███     ░███    ░███        ░███    
 █████ ██ █████     █████ ██ █████   █████ ██    █████   
░░░░░ ░░ ░░░░░     ░░░░░ ░░ ░░░░░   ░░░░░ ░░    ░░░░░         

I made random tool
              --[made by justme1231234]--
"""

choice = "0"
choice2 = "0"

while True:
    print(logo)
    print("1. Run a program")
    print("2. Exit")
    try:
        choice = input("Enter your choice: ")
    except EOFError:
        choice = "1"

    #rename the "yourprogram" to the program you want to open

    if choice == "1":
        print("1. yourprogram")
        print("2. yourprogram")
        print("3. yourprogram")
        print("4. yourprogram")
        print("5. yourprogram")
        print("6. yourprogram")
        print("7. yourprogram")
        try:
            choice2 = input("Enter your choice: ")
        except EOFError:
            choice2 = "5"
        if choice2 == "1":
            subprocess.run(["open", "-a", "yourprogram"])
        elif choice2 == "2":
            subprocess.run(["open", "-a", "yourprogram"])
        elif choice2 == "3":
            subprocess.run(["open", "-a", "yourprogram"])
        elif choice2 == "4":
            subprocess.run(["open", "-a", "yourprogram"])
        elif choice2 == "5":
            subprocess.run(["open", "-a", "yourprogram"])
        elif choice2 == "6":
            subprocess.run(["open", "-a", "yourprogram"])
        elif choice2 == "7":
            subprocess.run(["open", "-a", "yourprogram"])
    if choice == "2":
        print("Goodbye! thank you for using")
        break
