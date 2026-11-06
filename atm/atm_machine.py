class atm:
    def __init__(self):
        self.pin = 1234
        self.balance = 4000
        self.menu()



    def menu(self):
        print("""*************************
        1.Press 1 for balance check
        2.Press 2 for withdrawl
        3.Press 3 for deposit
        4.Press 4 for Pin Change 
        5.Press 5 for Exit
        ***********************************
        """)


        a = int(input("Enter Your Choice:"))
        if a == 4:
            self.change_pin()
        if a == 2:
            self.withdraw()
        if a == 3:
            self.deposit()
        if a == 1:
            self.balance_check()
        if a == 5:
            exit(0)


    def change_pin(self):
        b = int(input("Enter Current Pin:"))
        if b == self.pin:
            c = int(input("Enter New Pin:"))
            self.pin = c
            print("Pin Change Succesfully")
        else:
            print("Wrong Password ")
        self.menu()


    def withdraw(self):
        pin = int(input("Enter Pin:"))
        if pin == self.pin: 
            # self.menu()
            d = int(input("Enter Amount To Withdraw:"))
            if d>=0 and d<=self.balance:
                self.balance = self.balance - d
                print("SUCCESSFULLY WITHDRAWN." \
            "YOUR UPDATED BALANCE IS:",self.balance)
            else:
                print("YOU DONT HAVE ENOUGH BALANCE")
        else:
                    print("WRONG PASSWORD")
        self.menu()



    def balance_check(self):
        pin = int(input("Enter Pin:"))
        if pin == self.pin:
            print("Your Total Balance Is - ",self.balance)
        else:
            print("WRONG PASSWORD")
        self.menu()


    def deposit(self):
        pin = int(input("Enter Pin:"))
        if pin == self.pin:
            q = int(input("Enter Amount To Deposit:"))
            if q>=0:
                self.balance = self.balance + q
                print("""AMOUNT DEPOSITED SUCCESSFUL 
                YOUR UPDATED BALANCE IS:
                """,self.balance)
        else:
            print("WRONG PASSWORD")
        self.menu()

                
x = atm()