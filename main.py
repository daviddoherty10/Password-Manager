from new_user import NewUser
from user_login import User

def main():
    login_or_create()


def login_or_create():
    openning_message = """Login or if you don't have an
account you can create one. (login/create/quit)"""
    print(openning_message)
    login__create = input("> ")
    if login__create == "login":
        login()
    elif login__create == "create":
        creating_new_user()
    elif login__create == "quit":
        quit()

def creating_new_user():
    username = NewUser.make_username()
    password = NewUser.make_password()
    NewUser.add_pass_and_user_to_csv(username, password)
    login_or_create()


def login():
    if User.username() == True:
        User.password()
        login_or_create()



if __name__ == "__main__":
    main()