class loan:
    def menu(self):
        print(""" ****************
        SELECT ANY FOLLOWING CHOICE
        1.EMI CALCULATOR
        2.SI CALCULATOR
        ***************************""")


        a = int(input('SELECT ANY FOLLOWING OPTIONS<:>'))
        if a == 2:
            self.si()

        if a == 1:
            self.emi()

        if a == 3:
            exit(0)

        else:
            print("WRONG CHOICE")

    def si(self):
        p = float(input("ENTER THE AMOUNT OF LOAN:"))
        r = float(input("ENTER THE  RATE OF INTEREST:"))
        t = float(input("ENTER TIME IN YEARS:"))
        si1 = (p*r*t)/100
        print('THE SIMPLE INTEREST FOR FOLLWOING AMOUNT IS -->',si1,"Rupee")
        self.menu()



    def emi(self):
        p = float(input("ENTER THE AMOUNT OF LOAN:"))
        ar = float(input("ENTER THE  RATE OF INTEREST/ANNUAL RATE OF INTEREST:"))
        n = float(input("ENTER NUMBER OF MONTHS:"))
        r = ar/12/100
        emi = p*r*(1+r)**n/((1+r)**n-1)
        print("YOUR ESTIMATED EMI IS -->",emi,"Rupee   :  "
              "YOU Have TO PAY THIS AMOUNT EVERY MONTH")
        self.menu()
        
x = loan()
x.menu()