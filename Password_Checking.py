import sys
import time
def password():
    cp=input("Enter password to create: ")
    print("Congrats...! UR Password is:",cp)
    
    cpp=input("Enter password to login: ")
    if cp==cpp:
        print("Welcome to home..")
    else:
        def re():
            c=0
            while(c!=5):
                print("Incorrect password!")
                re=input("Re-Enter password: ")
                if(re==cp):
                    print("Login successfull..")
                    sys.exit(0)
                elif re!=cp:
                    c=c+1
        re()
        
        def pas():
                    print("UR phone is locked for 30Sec")
                    time.sleep(3)
                    password()
                    
        pas()       
password()