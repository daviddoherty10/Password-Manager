import csv
import re

class NewUser:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def make_username():
        while True:
            username = input("Username: ").strip()
            if len(username) < 4:
                print("Invalid username: (char-count must be >= 4)")
            else:
                username_exists = False
                with open("user info.csv", mode="r") as file:
                    csv_reader = csv.DictReader(file)
                    for row in csv_reader:
                        if row["username"] == username:
                            print("Username already exists.")
                            username_exists = True
                            break

                if username_exists:
                    continue

                happy = input("Make this your username? (yes/no) ").lower().strip()
                if happy == "yes":
                    return username


    def make_password():
        while True:
            password = input("Password: ")
            if not password:
                print("Please enter a valid passowrd")
                continue
            elif re.search(r"^[a-z0-9_]+$", password) and 8 <= len(password) <= 25:
                print(end="\n \n")
                return password
            else:
                print("Invalid")
                continue
    

    def add_pass_and_user_to_csv(username, password):       
        with open("user info.csv", mode="a") as file:
            writer = csv.DictWriter(file, fieldnames=["username", "password"])
            writer.writerow({"username": username, "password": password})