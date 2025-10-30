a = 3
username = "Medina"
userpassword = "MedinA129"
balance = 500
import time
while a > 3:
    print("Welcome to our ShoppingWeb!!!")
    enteredusername = input("Please enter your username:   ")
    enteredpassword = int(input("Please enter your password:  "))
    if userpassword == enteredpassword and username == enteredusername :
        while True:
            selectednumber = input("Select a number among: 1 2 3 4 5 6 7 ")
            print("1-->Catagories")
            print("2-->Basket")
            print("3-->Favorites")
            print("4-->History")
            print("5-->Settings")
            print("6-->Show my balance")
            print("7-->Exit")
            if selectednumber == "1":
                print()


    a=a-1
    if a == 0:
        time.sleep(10)
