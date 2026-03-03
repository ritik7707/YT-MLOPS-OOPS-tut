class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()



    def menu(self):
        user_input = input("""Welcome to chatbook ! How would you like to proceed
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. press any other key to exit""")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.post()
        elif user_input == "4":
            pass
        else:
            exit()

    def signup(self):
        email = input("enter your e-mail here -> ")
        pwd = input("enter your password here -> ")
        self.username = email
        self.password = pwd
        print("You have sign up successfully !!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username =="" and self.password == "":
            print("Please signup first by pressing 1 in the main menu")
        else:
            username = input("enter the email/username here -> ")
            pwd = input("enter your password here -> ")
            if self.username== username and self.password ==pwd:
                print("You have sign in successfully")
                self.loggedin = True
            else:
                print("Please input correct credentials")
        print("\n")
        self.menu()

obj = chatbook()