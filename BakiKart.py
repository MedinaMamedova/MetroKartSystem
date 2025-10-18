a = 3
password = 8975
userbalance = 50
debt = 10
moveCount = 0
operations = []
payments = 0
discounts = 0
plusbalance = 0
newrule = 0
def criticalbalance (balance , debt ,payment ,userbalance):
    if 0.30 <= balance <= 0.39:
        print("balansiniz yetersizdir : (teklif : 0.30 + -0.10)")
        print("teklifi qebul edirsinizse 1 duymesine basin")
        offer = int(input())
        if offer == 1:
            debt = debt + 0.10
            userbalance = userbalance - 0.30
            payments = payments + 0.30
    else:
        print("balansinizi artirin")
    return debt , userbalance , payments

while a > 0:
    enteredpassword = int(input(" 4 reqemli kodu daxil edin: "))
    if enteredpassword == password:
        print("1-->Balansı göstər")
        print("2--> Balans artır")
        print("3-->Gediş et (turniketi keç)")
        print("4-->Son əməliyyatlara bax")
        print("5-->Günlük statistika")
        print("6-->Parametrlər")
        print("0-->Çıxış")
        selectednumber = int(input("select a number : 1 2 3 4 5 6 0 "))
        if selectednumber == 1:
            print(userbalance)
            operations.append("Balansi gostermek")
        elif selectednumber == 2:
            addedamount = int(input("Elave edeceyiniz meblegi daxil edin"))
            if newrule == 0:
                if addedamount < 100:
                    plusbalance = plusbalance + addedamount
                    if addedamount > 0:
                        if debt > 0:
                            if debt > addedamount:
                                debt = debt - addedamount
                            elif debt == addedamount:
                                debt = 0
                            else:
                                userbalance = userbalance + (addedamount - debt)
                                debt = 0
                        else:
                            userbalance = userbalance + addedamount
                else:
                    print("100-den kicik mebleg daxil edin")
            operations.append("Balansi artirma")
        elif selectednumber == 3:
            frsubwayfare = 0.40
            snsubwayfare = 0.36
            trsubwayfare = 0.30
            if user == "Telebe":
                frsubwayfare = snsubwayfare = trsubwayfare = studentsale
            elif user == "Pensioner":
                frsubwayfare = snsubwayfare = trsubwayfare = pensionersale
            if moveCount == 0:
                if userbalance >= frsubwayfare:
                    userbalance = userbalance - frsubwayfare
                    moveCount = moveCount + 1
                    payments = payments + frsubwayfare
                else:
                    c = criticalbalance ('balance')
                    continue
            elif  2<= moveCount <=4:
                if userbalance >= snsubwayfare:
                    userbalance = userbalance - snsubwayfare
                    moveCount = moveCount + 1
                    payments = payments + snsubwayfare
                    discounts = discounts + 0.04
                else:
                    c = criticalbalance ('balance')
            else:
                if userbalance >= trsubwayfare:
                    userbalance = userbalance - trsubwayfare
                    moveCount = moveCount + 1
                    payments = payments + trsubwayfare
                    discounts = discounts + 0.10
                else:
                    c = criticalbalance ('balance')
            operations.append("Metroya giris")
        elif selectednumber == 4:
            print("N sec")
            print(operations)
        elif selectednumber == 5:
            print("Artirilan mebleg: ", plusbalance)
            print("Umumi odenis:" ,payments)
        elif selectednumber == 6:
            print("Umumi gedis sayi:", moveCount)
            print("Butun endirimler: ", discounts)
            print("Butun odenisler : ", payments)
            print("Parametrleri deyis: 1 ve ya 2")
            print("1-->Balans artirma limitinin deyisdirlmesi")
            print("2-->Endirim rejiminin secilmesi")
            selectednumber2 = int(input("1 ve ya 2 reqemlerinden birini secin :"))
            if selectednumber2 == 1:
                newrule = newrule + 1
            else:
                user = input("Musteri kimdir : Pensiyoner yoxsa Telebe" )
                if user == "Telebe":
                    studentsale == 0.20
                else:
                    pensionersale == 0.15
    else:
        a=a-1
        






               
            

