import sys
print("PIZZA HUT")
ls=[]
qr=[]
am=[]
def F_D():
    print("1.ORDER")
    print("2.PAYMENT")
    print("3.EXIT")
    ch=input("Enter UR Choice")
    if ch=="1":
        def order():
            print("MENU")
            print("1.PIZZA")
            print("2.BURGER")
            print("3.NOODELS")
            print("4.GO BACK")
            chh=input("Enter ur choice")
            if chh=="1":
                def pizza():
                    p={1:['1','Veg Pizza','150'],
                       2:['2','Special Veg Pizza','200'],
                       3:['3','Mini Pizza','100'],
                       4:['4','Menu',' ']}
                    print("{:<20}{:<20}{:<20}".format("SL_NO","FOODS","PRICE"))
                    for key,value in p.items():
                        SL_NO,FOODS,PRICE=value
                        print("{:<20}{:<20}{:<20}".format(SL_NO,FOODS,PRICE))
                    while(1):
                        c=input("enter your choice")
                        if c=="1":
                            def VP():
                               m=input("Enter the Veg Pizza quantity")
                               if m.isdigit() :
                                       VPizza=int(m)*150
                                       ls.append("Veg Pizza")
                                       qr.append(m)
                                       am.append(VPizza)
                               else:
                                   print("Invalid choice")
                                   VP()
                            VP()
                        elif c=="2":
                            def SP():
                              n=input("Enter the Special Veg Pizza quantity")
                              if n.isdigit() :
                                  SPizza=int(n)*200
                                  ls.append("Special Veg Pizza")
                                  qr.append(n)
                                  am.append(SPizza)
                              else:
                                  print("Invalid Choice")
                                  SP()
                            SP()
                        elif c=="3":
                            def MP():
                               p=int(input("Enter the Mini Pizza quantity"))
                               if p.isdigit() :
                                   MPizza=int(p)*100
                                   ls.append("Mini Pizza")
                                   qr.append(p)
                                   am.append(MPizza)
                               else:
                                   print("Invalid choice")
                                   MP()
                            MP()
                        elif c=="4":
                             order()
                        else:
                            print("Invalid choice")
                            pizza()
                          
                pizza()
        
            elif chh=="2":
              def burger():
                b={1:['1','Veg Burger','100'],
                   2:['2','Special Veg Burger','130'],
                   3:['3','Cheese Burger','150'],
                   4:['4','Menu',' ']}
                print("{:<20}{:<20}{:<20}".format("SL_NO","FOODS","PRICE"))
                for key,value in b.items():
                    SL_NO,FOODS,PRICE=value
                    print("{:<20}{:<20}{:<20}".format(SL_NO,FOODS,PRICE))
                while(1):
                      c=input("enter your choice")
                      if c=="1":
                          def VB():
                              r=input("Enter the Veg Burger quantity")
                              if r.isdigit() :
                                   VBurger=int(r)*100
                                   ls.append("Veg Burger")
                                   qr.append(r)
                                   am.append(VBurger)
                              else:
                                  print("Invalid choice")
                                  VB()
                          VB()
                      elif c=="2":
                          def SB():
                              s=input("Enter the Special Veg Burger quantity")
                              if s.isdigit() :
                                  SBurger=int(s)*130
                                  ls.append("Secial Veg Burger")
                                  qr.append(s)
                                  am.append(SBurger)
                              else:
                                  print("Invalid choice")
                                  SB()
                          SB()
                      elif c=="3":
                          def CB():
                               t=input("Enter the Cheese Burger quantity")
                              # try:
                               #    t=int(t)
                               if t.isdigit() :
                                   CBurger=int(t)*150
                                   ls.append("Cheese Burger")
                                   qr.append(t)
                                   am.append(CBurger)
                               else:
                                    print("Invalid choice")
                                    CB()
                          CB()
                      elif c=="4":
                          order()
                      else:
                          print("Invalid choice")
                          burger()
              burger()
            
            elif chh=="3":
              def noodels():
                n={1:['1','Veg Noodels','100'],
                   2:['2','Special Veg Noodels','150'],
                   3:['3','Cheese Noodels','170'],
                   4:['4','Menu',' ']}
                print("{:<20}{:<20}{:<20}".format("SL_NO","FOODS","PRICE"))
                for key,value in n.items():
                    SL_NO,FOODS,PRICE=value
                    print("{:<20}{:<20}{:<20}".format(SL_NO,FOODS,PRICE))
                while(1):
                      c=input("enter your choice")
                      if c=="1":
                          def VN():
                               v=input("Enter the Veg Noodels quantity")
                               if v.isdigit() :
                                   VNoodels=int(v)*100
                                   ls.append("Veg Noodels")
                                   qr.append(v)
                                   am.append(VNoodels)
                               else:
                                    print("Invalid choice")
                                    VN()
                          VN()
                      elif c=="2":
                          def SN():
                              w=input("Enter the Special Veg Noodels quantity")
                              if w.isdigit() :
                                  SNoodels=int(w)*150
                                  ls.append("Special Veg Noodels")
                                  qr.append(w)
                                  am.append(SNoodels)
                              else:
                                 print("Invalid choice")
                                 SN()
                          SN()
                      elif c=="3":
                           def CN():
                               x=input("Enter the Cheese noodels quantity")
                               if x.isdigit() :
                                   CNoodels=int(x)*170
                                   ls.append("Cheese Noodels")
                                   qr.append(x)
                                   am.append(CNoodels)
                               else:
                                 print("Invalid choice")
                                 CN()
                           CN()
                      elif c=="4":
                             order()
                      else:
                          noodels()
              noodels()
            elif chh=="4":
                F_D()
            else:
                print("Invalid choice")
                order()
        order() 
    elif ch=="2":
       def pay():
            if not ls:
                print("You need to place an order first.")
                F_D()
            else:

                print("  Items               Quantity              Price")
                for x, y, z in zip(ls, qr, am):
                    print("{:<20}{:<20}{:<20}".format(x, y, z))
                    print(f"   {x}         {y}           {z}   ")
                    tm = sum(map(int, am))
    
                    print("Total amount:                              ", tm)
    
                    def payment():
                        pay=input("Want to pay? if YES click 'Y' else 'N' ")
                        if pay=="Y":
                            input("Enter Address:")
                            input(print("Enter UPI Number:"))
                            print('THANK YOU!!..UR FOOD WILL BE DELIVERED SOON..')
                            sys.exit(0)
                        elif pay=="N":
                            F_D()
                        else:
                            print("Invalid choice")
                            payment()
        
                    payment()

       pay()
    elif ch=="3":
        sys.exit()
    else:
        print("Invalid choice")
        F_D()
F_D()        


        
