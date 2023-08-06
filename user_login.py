import csv

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def username():
        while True:
            username = input("Username: ").rstrip()
            with open("user info.csv") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["username"]:
                        return True
                    else:
                        print("Incorrect username!")
                        continue


    def password():
        while True:
            password = input("Password: ").rstrip()
            with open("user info.csv") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["password"] == password:
                        print("Access Granted")
                        return True
                    else:
                        print("Incorrect password!")
                        continue