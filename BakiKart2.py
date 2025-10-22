a = 3
truepassword = 6754
userbalance = 1
totaladdedamount = 0
debt = 3
normalsubwayfare = 0.40
snsubwayfare = 0.36
trsubwayfare = 0.30
newrule = 0
moveCount = 0
payments = 0
discounts = 0
user = ''
operations = []
def criticalbalance (userbalance, debt ,payments):
    if  0.30 <= userbalance <=0.39:
        print("Do you want to use emergency debt? (yes / no)")
        offer = input ()
        if offer == "yes":
            userbalance = userbalance - 0.30
            debt = debt + 0.10
            payments = payments + 0.30
    else:
            print("Please increase your balance")
    return userbalance, debt , payments
while a > 0:
    enteredpassword = int(input("Enter your 4 digit password: "))
    if enteredpassword == truepassword:
        while True:
            print("The login was successful")
            print("1-->Show the balance")
            print("2-->Increase the balance")
            print("3-->Make a trip")
            print("4-->Look last operations")
            print("5-->Daily statics")
            print("6-->Parameters")
            print("0-->Exit") 
            selectednumber = int(input("select the number among 1 2 3 4 : "))
            if selectednumber == 1:
                print("Balance: ", userbalance)
                operations.append("showing balance")
            elif selectednumber == 2:
                addedamount = int(input("add the amount you want"))
                operations. append("increasing the balance")
                if totaladdedamount > 100 and addedamount > 100:
                    print("You exceed the limit")
                else:
                    totaladdedamount = totaladdedamount + addedamount
                    if debt > 0:
                        if  debt > addedamount:
                            debt = debt - addedamount
                            addedamount = 0
                        elif debt == addedamount:
                            debt = 0
                            addedamount = 0
                        elif  debt < addedamount:
                            addedamount = addedamount - debt
                            debt = 0
                    userbalance = userbalance+ addedamount
                print("Userbalance :", userbalance)
            elif selectednumber == 3:
                operations.append("usage of subway")
                if userbalance < 0.10:
                    print("Your balance is not enough")
                elif newrule == 1 and user == "telebe":
                    userbalance = userbalance - 0.20
                    print ("Pass was succesful")
                elif newrule == 1 and user == "Retired":
                    userbalance = userbalance - 0.10
                    print ("Pass was succesful")
                elif moveCount == 0:
                    if userbalance >= normalsubwayfare:
                        userbalance = userbalance - normalsubwayfare
                        moveCount = moveCount + 1
                        payments = payments + normalsubwayfare
                        print ("Pass was succesful")
                    else:
                         userbalance ,debt , payments = criticalbalance( userbalance, debt , payments) 
                elif moveCount == 1:
                    if userbalance >= normalsubwayfare:
                        userbalance = userbalance - normalsubwayfare
                        moveCount = moveCount + 1
                        payments = payments + 1
                        print("Pass was succesfull")
                    else: 
                        userbalance, debt, payments= criticalbalance (userbalance ,debt , payments)
                elif  2<= moveCount <=4:
                    if userbalance >= snsubwayfare:
                        userbalance = userbalance - snsubwayfare
                        moveCount = moveCount + 1
                        payments = payments + snsubwayfare
                        discounts = discounts + 0.04
                        print ("Pass was succesful")
                    else:
                        userbalance, debt, payments= criticalbalance (userbalance, debt ,payments)
                print("userbalance : " ,userbalance)
            elif selectednumber == 4:
                print(operations)
                operations.append("looking to operations")
            elif selectednumber == 5:
                print("movecount:", moveCount)
                print("payments:" , payments)
                print("discounts:", discounts)
                print("totaladedamount:", totaladdedamount)
            elif selectednumber == 6:
                operations.append("changing the settings")
                print("do you want to change your status? (yer/ no)")
                yesorno = input("select : yes or no ")
                if yesorno == "yes":
                    newrule = + 1
                    user = input(" Student or Retired ")
                else:
                    continue
                print("Do you want to change your password? (yes / no)")
                yon = input()
                if yon == "yes":
                    b=3
                    while b > 0:
                        yourpassword = int(input("Enter your previous password"))
                        if yourpassword == truepassword:
                            newpassword = int(input("Enter your new 4 digit password"))
                            print("All done")
                            newpassword = truepassword
                        else:
                            print("after 3 wrong passsword your account will be blocked, try one more time")
                            b=b-1
                    if b == 0:
                        print("your account is blocked")
                        break
            elif selectednumber == 7:
                print("Exit...")
                break
            else:
                print("Error")
                break
                



                

                