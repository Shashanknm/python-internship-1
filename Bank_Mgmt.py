import random
import sys
d = {}
e = {}
f = {}
#g = {}
#h={}
#i={}
zbal=[]
sbal=[]
bbal=[]
sum1=0
sum2=0
sum3=0
zacc_num = 0
zpas = 0
sacc_num=0
spas=0
bacc_num=0
bpas=0

def z():
    print("Name:", d['name'])
    print('phno:', d['phno'])
    print("ACCOUNT NUMBER is:", zacc_num)
    print("IFSE code is: AS122CSI")
def s():
    print("Name:", e['name'])
    print('phno:', e['phno'])
    print("ACCOUNT NUMBER is:", sacc_num)
    print("IFSE code is: AS122CSI")
def b():
    print("Name:",f['name'])
    print("phno:",f['phno'])
    print("ACCOUNT NUMBER is:", bacc_num)
    print("IFSE code is: AS122CSI")
def c():
    zzbal=sum(zbal)
    print("Total amt:",zzbal)
def l():
    sum2=0
    for i in sbal:
        sum2+=i
        sbal.append(sum2)
    print("Total amt:",sbal)
def m():
    sum3=0
    for i in bbal:
        sum3+=i
        bbal.append(sum3)
    print("Total amt:",bbal)

print("Welcome to the smart banking")

def smart():
    print("1. Create the bank account")
    print("2. Login the bank account")
    print("3. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        def create():
            print("1. Zero balance account")
            print("2. Saving account")
            print("3. Business account")
            print("4. Return to main menu")

            chh = input("Enter your choice: ")

            if chh == "1":
                def zerob():
                    while True:
                        zname = str(input("Enter your name: "))
                        zphno = int(input("Enter your phno: "))
                        ze=int(input("Enter the initial amount to be credited:"))
                        if ze>0:
                            zbal.append(ze)
                        else:
                            print("Enter crt amt")
                            zerob()
                        zname.lower()
                        zname.strip()
                        x = zname[0:2]
                        y = zname[-2:]
                        global zpas
                        zpas = x + y
                        d['name'] = zname
                        d['phno'] = zphno
                        global zacc_num
                        zacc_num = random.randint(100000, 999999)
                        
                        z()
                        print("Your account has been created")
                        print("UR acnt balance is:",ze)
                        print("Your ATM password is in lower case:", zpas)
                        smart()
                        

                zerob()
            elif chh == "2":
                def saving():
                    while True:
                        sname = input("Enter your name: ")
                        sphno = int(input("Enter your phno: "))
                        ze=int(input("Enter the initial amount to be credited:"))
                        if ze>=500:
                            sbal.append(ze)
                        else:
                            print("Enter crt amt")
                            saving()
                        sname.lower()
                        sname.strip()
                        x = sname[0:2]
                        y = sname[-2:]
                        global spas
                        spas = x + y
                        e['name'] = sname
                        e['phno'] = sphno
                        global sacc_num
                        sacc_num = random.randint(100000, 999999)  
                        s()
                        print("Your account has been created")
                        print("UR acnt balance is:",ze)
                        print("Your ATM password is in lower case:", spas)
                        smart()

                saving()
            elif chh=="3":    
                def business():
                    while True:
                    
                        bname=input("enter your name: ")
                        bphno=int(input("enter your phno: "))
                        ze=int(input("Enter the initial amount to be credited:"))
                        if ze>=1000:
                            bbal.append(ze)
                        else:
                            print("Enter crt amt")
                            business()
                        bname.lower()
                        bname.strip()
                        x=bname[0:2]
                        y=bname[-2:]
                        global bpas
                        bpas=x+y
                        f['name']=bname
                        f['phno']=bphno
                        random.randint(100000,999999)
                        b()
                        print("your account has been created")
                        print("UR acnt balance is:",ze)
                        print("your ATM password is in lower case:",bpas)
                        smart()
                business()

            elif chh == "4":
                smart()
           
            else:
                print("Invalid choice")
                create()

        create()

    elif ch == "2":
        print("-----LOGIN-----")
        a = int(input("Enter acc.no: "))
        ap = input("Enter password: ")


        def login():
            if a == zacc_num and ap == zpas:
                print("1. Credit")
                print("2.Debit")
                print("3.Show balance")
                print("4.Go back")
                cb=input("Enter your choice:")
                if cb=="1":
                    cre=int(input(print("Enter ammount to credit")))
                    print(cre,"has been credited to your acnt no:",a)
                    
                    zbal.append(cre)
                    #g['creamt']=cre
                    c()
                    smart()
                elif cb=="2":
                    deb=int(input("Enter the amount to debit:"))
                    if deb<=sum(zbal):
                        print(deb,"has been debited from UR acnt no:",a)
                        ZD=sum(zbal)-deb
                        zbal.clear()
                        print("Remaining balance in ur acnt no:",a,"is",ZD)
                        
                        zbal.append(ZD)
                        smart()
                    else:
                        print("U DON'T HAVE SUFFICIENT BALANCE IN UR ACNT")
                        login()
                elif cb=="3":
                    print("TOTAL AMT IN UR ACNT IS:",sum(zbal))
                    smart()
                elif cb=="4":
                    smart()
                else:
                    print("Invalid choice")
                    login()
            elif a == sacc_num and ap == spas:
                print("1. Credit")
                print("2.Debit")
                print("3.Show balance")
                cb=input("Enter your choice:")
                if cb=="1":
                    dre=int(input(print("Enter ammount to credit")))
                    print(dre,"has been credited to your acnt no:",a)
                    #h['dreamt']=dre
                    
                    sbal.append(dre)
                    l()
                    smart()
                elif cb=="2":
                    deb=int(input("Enter the amount to debit:"))
                    if deb<=sum(sbal):
                        print(deb,"has been debited from UR acnt no:",a)
                        SD=sum(sbal)-deb
                        sbal.clear()
                        print("Remaining balance in ur acnt no:",a,"is",SD)
                        sbal.append(SD)
                        smart()
                    else:
                        print("U DON'T HAVE SUFFICIENT BALANCE IN UR ACNT")
                        login()
                elif cb=="3":
                    print("TOTAL AMT IN UR ACNT IS:",sum(sbal))
                    smart()
                elif cb=="4":
                    smart()
                else:
                    print("Invalid choice")
                    login()
            elif a==zacc_num and ap==zpas:
                print("1. Credit")
                print("2.Debit")
                print("3.Show balance")
                cb=input("Enter your choice:")
                if cb=="1":
                    sre=int(input(print("Enter ammount to credit")))
                    print(sre,"has been credited to your acnt no:",a)
                    #i['sreamt']=sre
                    
                    bbal.append(sre)
                    m()
                    smart()
                elif cb=="2":
                    deb=int(input("Enter the amount to debit:"))
                    if deb<=sum(bbal):
                        print(deb,"has been debited from UR acnt no:",a)
                        BD=sum(bbal)-deb
                        bbal.clear()
                        print("Remaining balance in ur acnt no:",a,"is",BD)
                        sbal.append(BD)
                        smart()
                    else:
                        print("U DON'T HAVE SUFFICIENT BALANCE IN UR ACNT")
                        login()
                elif cb=="3":
                    print("TOTAL AMT IN UR ACNT IS:",sum(bbal))
                    smart()
                elif cb=="4":
                    smart()
                else:
                    print("Invalid choice")
                    login()
            else:
                print("Incorrect acnt no. or password")
                smart()
                
        login()
        
    elif ch=="3":
        sys.exit(0)
    
    else:
        print("Invalid choice")
        smart()

smart()
