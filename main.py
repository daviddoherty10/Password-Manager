from new_user import NewUser

def main():
    login_or_create()


def login_or_create():
    ...


def creating_new_user():
    username = NewUser.make_username()
    password = NewUser.make_password()
    NewUser.add_pass_and_user_to_csv(username, password)


def login():
    ...



if __name__ == "__main__":
    main()