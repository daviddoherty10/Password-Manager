import csv
import re

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
import csv
import re

def make_username():
    while True:
        username = input("Username: ").rstrip()
        if not username:
            print("Please input a valid username")
        elif not re.search(r"\d\w\S", username) or not re.search(r"[a-zA-Z][0-9]\S", username):
            print("Invalid username. Usernames must contain both letters and digits.")
        else:
            with open("user info.csv", mode="r") as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    if row["username"] == username:
                        print("Username already exists.")
                        continue

                    happy = input("Make this your username? (yes/no) ").lower().rstrip()
                    if happy == "yes":
                        return username
                    else:
                        continue  # Exit the loop and reprompt for a new username
                else:
                    return username  # If the loop completes without finding a match, the username is available


    def make_password():
        while True:
            password = input("Password: ")
            if not password:
                print("Please enter a valid passowrd")
                continue
            elif re.search(r"\w\d|\d\w", password):
                return password
            else:
                print("Invalid")
                continue


username = User.make_username() 
password = User.make_password() 
user = User(username, password)      