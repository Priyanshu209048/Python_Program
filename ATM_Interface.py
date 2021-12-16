balance=340000
password=1111
i=10000

while i>=0:
    print("Welcome to SAITM bank")
    print("1.Withdraw money")
    print("2.Update password")
    print("3.Exit")
    opt=int(input("select Withdraw money, Update password, Exit:"))
    if opt==1:
        password=int(input("Enter password:"))
        if password==1111:
            money_withdraw=int(input("Withdraw money:"))
            if balance>=money_withdraw:
                print("selcet yes or no")
                select=input()
                if select=="yes":
                    print("Please collect your money:",money_withdraw)
                    print("do you want se your balance:")
                    print("select yes or no")
                    select=input()
                    if select=="yes":
                        Total_balance = balance-money_withdraw
                        print("Total balance",Total_balance)
                    elif select=="no":
                        print("exit")
                elif select=="no":
                    print("exit")
            else:
                print("Insufficient Amount")
                continue
        else:
            print("Wrong password")
            
    elif opt==2:
        Password=int(input("Enter previous password:"))
        if Password==1111:
            New_password=input("Enter new password:")
            Confirm_password=input("Enter confirm password:")
            if New_password==Confirm_password:
                print("Password updated")
            else:
                print("Does not match")
        else:
            print("Your password do not match")
            
    elif opt==3:
        print("Exit")
        break
