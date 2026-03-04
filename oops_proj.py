class chatbook:

    __user_id = 1

    def __init__(self):
        self.__name = "Default name"
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        self.username = ""
        self.password = ""
        self.loggedin = False
        # self.menu()

    @staticmethod
    def get_id():
        return chatbook.__user_id
    
    @staticmethod
    def set_id(value):
        chatbook.__user_id = value

    def get_name(self):
        return self.__name
    
    def set_name(self,value):
        self.__name = value


    def menu(self):
        user_input = input("""Welcome to chatbook ! How would you like to proceed
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. press any other key to exit
                           -> """)
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.message()
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

    def my_post(self):
        if self.loggedin ==True:
            txt = input("Enter your message here -> ")
            print(f"Following content has been posted -> {txt}")
        else:
            print("You need to signin first to post something...")
        print("\n")
        self.menu()
    
    def message(self):
        if self.loggedin == True:
            message = input("Write a message here -> ")
            friend = input("whom do you want to send this message -> ")
            print(f"Your message has been sended to {friend}")
        else:
            print("You need to signin first to send a message...")
        print("\n")
        self.menu()

# user1 = chatbook()