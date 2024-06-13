import sys
print("DMART BILLING")
ls=[]
qr=[]
am=[]
ma=['sugar','rice','salt','wheet','spoon','Tcup','plates','fork','shirt','pants','Tshirts','formals']
def mart():
    print("1.shoping")
    print("2.verification")
    print("3.billing")
    print("4.exit")
    ch=int(input("enter the choice"))
    if ch==1:
        def shop():
            print("welcome to shopping")
            print("1.grocery")
            print("2.kitchen")
            print("3.clothes")
            print("4.go to main menu")
            chh=int(input("Enter ur choice"))
            if chh==1:
                def grocery():
                    print("  items     price")
                    print("1.sugar      40/kg ")
                    print("2.rice       50/kg")
                    print("3.salt       20/kg")
                    print("4.wheet      30/kg")
                    print("5.go to shopping menu")
                    while(1):
                        c=int(input("enter your choice"))
                        if c==1:
                           m=int(input("enter the sugar quantity"))
                           sugar=(m*40)
                           ls.append("sugar")
                           qr.append(m)
                           am.append(sugar)
                           
                        elif c==2:
                      
                          n=int(input("enter the rice quantity"))
                          rice=(n*50)
                          ls.append("rice")
                          qr.append(n)
                          am.append(rice)
                          
                        elif c==3:
                           p=int(input("enter the salt quantity"))
                           salt=(p*20)
                           ls.append("salt")
                           qr.append(p)
                           am.append(salt)
                        elif c==4:
                           q=int(input("enter the wheet quantity"))
                           wheet=(q*30)
                           ls.append("wheet")
                           qr.append(q)
                           am.append(wheet)
                        elif c==5:
                          shop()
                          
                grocery()
        
            elif chh==2:
              def kitchen():
                print("welcome to kitchen shopping")
                print("  item        price")
                print("1.spoon         30")
                print("2.Tcup          40")
                print("3.plates         50")
                print("4.fork          20")
                print("5.go to shopping menu")
                while(True):
                      c=int(input("enter your choice"))
                      if c==1:
                           r=int(input("enter the spooon quantity"))
                           spoon=(r*30)
                           ls.append("spoon")
                           qr.append(r)
                           am.append(spoon)
                      elif c==2:
                      
                          s=int(input("enter the Tcup quantity"))
                          Tcup=(s*40)
                          ls.append("Tcup")
                          qr.append(s)
                          am.append(Tcup)
                          
                      elif c==3:
                           t=int(input("enter the plates quantity"))
                           plates=(t*50)
                           ls.append("plates")
                           qr.append(t)
                           am.append(plates)
                      elif c==4:
                           u=int(input("enter the fork quantity"))
                           fork=(u*20)
                           ls.append("fork")
                           qr.append(u)
                           am.append(fork)
                      elif c==5:
                          shop()
              kitchen()
            
            elif chh==3:
              def cloths():
                print("welcome to cloths shopping")
                print("  item        price")
                print("1.shirt         600")
                print("2.pants         400")
                print("3.Tshirt        300")
                print("4.formals       500")
                print("5.go to shopping menu")
                while(True):
                      c=int(input("enter your choice"))
                      if c==1:
                           v=int(input("enter the shirt quantity"))
                           shirt=(v*600)
                           ls.append("shirt")
                           qr.append(v)
                           am.append(shirt)
                      elif c==2:
                      
                          w=int(input("enter the pants quantity"))
                          pants=(w*400)
                          ls.append("pants")
                          qr.append(w)
                          am.append(pants)
                      elif c==3:
                           x=int(input("enter the Tshirts quantity"))
                           Tshirts=(x*300)
                           ls.append("Tshirt")
                           qr.append(x)
                           am.append(Tshirts)
                      elif c==4:
                           y=int(input("enter the formals quantity"))
                           formals=(y*500)
                           ls.append("formals")
                           qr.append(y)
                           am.append(formals)
                      elif c==5:
                          shop()
              cloths()
            elif chh==4:
                mart()
        shop() 
    elif ch==2:
       def verification():
        print("Verification of selected items:")
        available_items = set(ma)  # List of available items in the shop
    
        for item in ls:
            if item in available_items:
                print(f"{item} is available in the shop.")
            else:
                print(f"{item} is not available in the shop.")
    
        return available_items
    
       available_items = verification()
       mart()
           
    
    elif ch==3:
        def billing():
            print("  Items      Quantity      Price")
            for x,y,z in zip(ls,qr,am):
                print(f"   {x}         {y}           {z}   ")
                tm=sum(am)                                           
                
            print("Total amount:              ",tm)
            
                
            
        billing()
        print("Thank you for shopping")
        sys.exit()
    elif ch==4:
        sys.exit()
    else:
        print("Invalid choice")
mart()        


        
