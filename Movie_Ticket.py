import sys
GASG=[]
GASP=[]
GASD=[]
BASG=[]
BASP=[]
BASD=[]
SASG=[]
SASP=[]
SASD=[]
def movies():
        print("  THEATRE           MOVIES")
        print("1.BALA              GANDHADA GUDI")
        print("2.LAKSHMI           BANGARADA MANUSHYA")
        print("3.SARASWATI         SAMPATHIGE SAVAAl")
        print("4.EXIT")
        c=input("Enter UR Choice:")
        a=sum(GASG+GASP+GASD)
        b=sum(BASG+BASP+BASD)
        cc=sum(SASG+SASP+SASD)
        if c=="1" and a!=1200:
            def GG():
                if GASG!=300 and GASP!=400 and GASD!=500:
                    print("1.GOLD CLASS        RS.300")
                    print("2.PLATINIUM CLASS   RS.500")
                    print("3.DIAMOND CLASS     RS.1000")
                    print("4.GO BACK")
                    ch=input("Select Category:")
                    if ch=="1":
                        
                        GGS=sum(GASG) #total seats booked
                        GGAS=300-GGS   #Available seats
                        print("Available Seats:",GGAS)
                        if GGAS!=0:
                            def GGT():
                                GG=0
                                try:
                                    t=int(input("Enter the number of tickets:"))
                                    t=int(t)
                                    if t>0 and t<=GGAS :
                                       GG+=t
                                       GASG.append(GG)
                                       GTA=300*t
                                       print("Thank U for booking ")
                                       print("Movie: GANDADHA GUDI")
                                       print("Seat Category:Gold Class")
                                       print("Total Seats:",t)
                                       print("Total Amount:",GTA)
                                       movies()
                                    else:
                                        print("Invalid choice")
                                        GGT()
                                except ValueError:
                                    print("INVALID CHOICE")
                                    GGT()
                            GGT()
                        else:
                            print("GOLD CLASS WAS FULL")
                            GG()
                    elif ch=="2":
                        GPS=0
                        GPS=sum(GASP)
                        
                        GGAS=400-GPS
                        print("Available Seats:",GGAS)
                        if GGAS!=0:
                            def GPT():
                                GP=0
                                try:
                                    t=int(input("Enter the number of tickets:"))
                                    if t>0 and t<=GGAS:
                                        GP+=t
                                        GASP.append(GP)
                                        GTA=500*t
                                        print("Thank U for booking")
                                        print("Movie: GANDADHA GUDI")
                                        print("Seat Category:Platinum Class")
                                        print("Total Seats:",t)
                                        print("Total Amount:",GTA)
                                        movies()
                                    else:
                                        print("Invalid choice")
                                        GPT()
                                except ValueError:
                                    print("INVALID CHOICE")
                                    GPT()
                            GPT()
                        else:
                            print("PLATINUM CLASS WAS FULL")
                            GG()
                    elif ch=="3":
                        GDS=0
                        GDS=sum(GASD)
                        
                        GGAS=500-GDS
                        print("Available Seats:",GGAS)
                        if GGAS!=0:
                            def GDT():
                                GD=0
                                try:
                                    t=int(input("Enter the number of tickets:"))
                                    if t>0 and t<=GGAS:
                                        GD+=t
                                        GASD.append(GD)
                                        GTA=1000*t
                                        print("Thank U for booking")
                                        print("Movie: GANDADHA GUDI")
                                        print("Seat Category:Diamond Class")
                                        print("Total Seats:",t)
                                        print("Total Amount:",GTA)
                                        movies()
                                    else:
                                        print("Invalid Choice")
                                        GDT()
                                except ValueError:
                                    print("INVALID CHOICE")
                                    GDT()
                            GDT()
                        else:
                            print("DIAMOND CLASS WAS FULL")
                            GG()
                    elif ch=="4":
                        movies()
                    else:
                        print("Invalid choice")
                        GG()
            GG()
        if c=="2" and b!=1200:
            def BM():
                if BASG!=300 and BASP!=400 and BASD!=500:
                    print("1.GOLD CLASS        RS.300")
                    print("2.PLATINIUM CLASS   RS.500")
                    print("3.DIAMOND CLASS     RS.1000")
                    print("4.GO BACK")
                    ch=input("Select Category:")
                    if ch=="1":
                        BGS=sum(BASG) #total seats booked
                        BMAS=300-BGS   #Available seats
                        print("Available Seats:",BMAS)
                        if BMAS!=0:
                            def BGT():
                                BG=0
                                try:
                                    t=int(input("Enter the number of tickets:"))
                                    if t>0 and t<=BMAS :
                                       BG+=t
                                       BASG.append(BG)
                                       BTA=300*t
                                       print("Thank U for booking ")
                                       print("Movie: BANGARADA MANUSHYA")
                                       print("Seat Category:Gold Class")
                                       print("Total Seats:",t)
                                       print("Total Amount:",BTA)
                                       movies()
                                    else:
                                        print("Invalid choice")
                                        BGT()
                                except ValueError:
                                    print("INVALID CHOICE")
                                    BGT()
                            BGT()
                        else:
                            print("GOLD CLASS WAS FULL")
                            BM()
                    elif ch=="2":
                        
                        BPS=sum(BASP)
                        BMAS=400-BPS
                        print("Available Seats:",BMAS)
                        if BMAS!=0:
                            def BPT():
                                BP=0
                                try:
                                    t=int(input("Enter the number of tickets:"))
                                    if t>0 and t<=BMAS:
                                        BP+=t
                                        BASP.append(BP)
                                        BTA=500*t
                                        print("Thank U for booking")
                                        print("Movie: BANGARADA MANUSHYA")
                                        print("Seat Category:Platinum Class")
                                        print("Total Seats:",t)
                                        print("Total Amount:",BTA)
                                        movies()
                                    else:
                                        print("Invalid choice")
                                        BPT()
                                except ValueError:
                                    print("INVALID CHOICE")
                                    BPT()
                            BPT()
                        else:
                            print("PLATINUM CLASS WAS FULL")
                            BM()
                    elif ch=="3":
                        
                        BDS=sum(BASD)
                        
                        BMAS=500-BDS
                        print("Available Seats:",BMAS)
                        if BMAS!=0:
                            def BDT():
                                BD=0
                                try:
                                    t=int(input("Enter the number of tickets:"))
                                    if t>0 and t<=BMAS:
                                        BD+=t
                                        BASD.append(BD)
                                        BTA=1000*t
                                        print("Thank U for booking")
                                        print("Movie: BANGARADA MANUSHYA")
                                        print("Seat Category:Diamond Class")
                                        print("Total Seats:",t)
                                        print("Total Amount:",BTA)
                                        movies()
                                    else:
                                        print("Invalid Choice")
                                        BDT()
                                except ValueError:
                                    print("INVALID CHOICE")
                                    BDT()
                            BDT()
                        else:
                            print("DIAMOND CLASS WAS FULL")
                            BM()
                    elif ch=="4":
                        movies()
                    else:
                        print("Invalid choice")
                        BM()
            BM()
        if c=="3" and cc!=1200:
            def SS():
                if SASG!=300 and SASP!=400 and SASD!=500:
                    print("1.GOLD CLASS        RS.300")
                    print("2.PLATINIUM CLASS   RS.500")
                    print("3.DIAMOND CLASS     RS.1000")
                    print("4.GO BACK")
                    ch=input("Select Category:")
                    if ch=="1":
                        SGS=sum(SASG) #total seats booked
                        SSAS=300-SGS   #Available seats
                        print("Available Seats:",SSAS)
                        if SSAS!=0:
                            def SGT():
                                SG=0
                                try:
                                    t=int(input("Enter the number of tickets:"))
                                    if t>0 and t<=SSAS :
                                       SG+=t
                                       SASG.append(SG)
                                       STA=300*t
                                       print("Thank U for booking ")
                                       print("Movie: SAMPATHIGE SAVAAl")
                                       print("Seat Category:Gold Class")
                                       print("Total Seats:",t)
                                       print("Total Amount:",STA)
                                       movies()
                                    else:
                                        print("Invalid choice")
                                        SGT()
                                except ValueError:
                                    print("INVALID CHOICE")
                                    SGT()
                            SGT()
                        else:
                            print("GOLD CLASS WAS FULL")
                            SS()
                    elif ch=="2":
                        
                        SPS=sum(SASP)
                        SSAS=400-SPS
                        print("Available Seats:",SSAS)
                        if SSAS!=0:
                            def SPT():
                                SP=0
                                try:
                                    t=int(input("Enter the number of tickets:"))
                                    if t>0 and t<=SSAS:
                                        SP+=t
                                        SASP.append(SP)
                                        STA=500*t
                                        print("Thank U for booking")
                                        print("Movie: SAMPATHIGE SAVAAl")
                                        print("Seat Category:Platinum Class")
                                        print("Total Seats:",t)
                                        print("Total Amount:",STA)
                                        movies()
                                    else:
                                        print("Invalid choice")
                                        SPT()
                                except ValueError:
                                    print("INVALID CHOICE")
                                    SPT()
                            SPT()
                        else:
                            print("PLATINUM CLASS WAS FULL")
                            SS()
                    elif ch=="3":
                        
                        SDS=sum(SASD)
                        
                        SSAS=500-SDS
                        print("Available Seats:",SSAS)
                        if SSAS!=0:
                            def SDT():
                                SD=0
                                try:
                                    t=int(input("Enter the number of tickets:"))
                                    if t>0 and t<=SSAS:
                                        SD+=t
                                        SASD.append(SD)
                                        STA=1000*t
                                        print("Thank U for booking")
                                        print("Movie: SAMPATHIGE SAVAAl")
                                        print("Seat Category:Diamond Class")
                                        print("Total Seats:",t)
                                        print("Total Amount:",STA)
                                        movies()
                                    else:
                                        print("Invalid Choice")
                                        SDT()
                                except ValueError:
                                    print("INVALID CHOICE")
                                    SDT()
                            SDT()
                        else:
                            print("DIAMOND CLASS WAS FULL")
                            SS()
                    elif ch=="4":
                        movies()
                    else:
                        print("Invalid choice")
                        SS()
            SS()
        elif c=="4":
            sys.exit(0)
        elif c=="1" and a==1200:
            print("HOUSE FULL!!...")
            movies()
        elif c=="2" and b==1200:
            print("HOUSE FULL!!...")
            movies()
        elif c=="3" and cc==1200:
            print("HOUSE FULL!!...")
            movies()
        else:
            print("INVALID CHOICE")
            movies()

movies()
            