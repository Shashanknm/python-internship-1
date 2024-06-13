import sys
Inc=[]
Bjp=[]
Jds=[]
def vote():
    print("1.Voting")
    print("2.Results")
    print("3.Go back")
    print("4.exit")
    ch=input(print("Enter ur choice:"))
    if ch=="1":
        input(print("Enter voting I'd number:"))
        def party():
            inc=0
            bjp=0
            jds=0
            print("1.INC")
            print("2.BJP")
            print("3.JDS")
            chh=input(print("Enter party:"))
            if chh=="1":
                inc+=1
                Inc.append(inc)
                print("Thank u for ur vote")
                vote()
            elif chh=="2":
                bjp+=1
                Bjp.append(bjp)
                print("Thank u for ur vote")
                vote()
            elif chh=="3":
                jds+=1
                Jds.append(jds)
                print("Thank u for ur vote")
                vote()
            else:
                print("Invalid choice")
                party()
        party()
    elif ch=="2":
        def result():
            I=[]
            B=[]
            J=[]
            R_INC=sum(Inc)
            I.append(R_INC)
            R_BJP=sum(Bjp)
            B.append(R_BJP)
            R_JDS=sum(Jds)
            J.append(R_JDS)
            party=[]
            votes=[R_INC,R_BJP,R_JDS]
            a="INC"
            b="BJP"
            c="JDS"
            party.append(a)
            party.append(b)
            party.append(c)
            for x,y in zip(party,votes):
                    print(f"  {x}       {y}")
            if R_INC>R_BJP>=R_JDS:
                print("INC PARTY WON THE ELECTION WITH ",I," VOTES")
                sys.exit(0)
            elif R_BJP>R_INC>=R_JDS:
                print("BJP PARTY WON THE ELECTION WITH ",B," VOTES")
                sys.exit(0)
            elif R_JDS>R_INC>=R_BJP:
                print("JDS PARTY WON THE ELECTION WITH ",J," VOTES")
                sys.exit(0)
            elif R_BJP==R_INC==R_JDS==0:
                print("VOTING IS NOT DONE")
                vote()
            elif R_INC==R_BJP:
                print("INC PARTY AND BJP PARTY HAVE EQUAL VOTES..SO RE-ELECTION WILL STARTS")
                vote()
            elif R_BJP==R_JDS:
                print("BJP PARTY AND JDS PARTY HAVE EQUAL VOTES..SO RE-ELECTION WILL STARTS")
                vote()
            elif R_INC==R_JDS:
                print("INC PARTY AND JDS PARTY HAVE EQUAL VOTES..SO RE-ELECTION WILL STARTS")
                vote()
            elif R_INC==R_BJP==R_JDS:
                print("THE ELECTION WAS DRAW...RE-ELECTION WILL STARTS")
                i()
        result()
        vote()
    elif ch=="3":
        i()
    elif ch=="4":
        sys.exit(0)
    else:
        print("Invalid choice...")
        vote()
def i():   
    age=input("Enter your age:")
    try:
        age = int(age)
        if age >= 18:
            print("You can vote")
            vote()
        else:
            print("You are a minor.")
            i()
    except ValueError:
        print("Invalid choice. Please enter a valid age.")
        i()
i()
                 

            
            