import random
<<<<<<< HEAD
def Owner(owner):
    print("This company's owner name is ", owner)
=======

def Owner(caller, owner, loc):
    print("This company's owner name is ", owner)
    print("Our company is located in ", loc) 
    print(caller, "Welcome to my company!! Wait a minute, please^^")
    print("===========================================")
>>>>>>> 8dd2cf42c23f4dfee330cf0d1e527d841626c6de
def Auto_Callinginroom_System(caller, owner):
    print("Hi,",caller, "Sorry to say you this sad sentences")
    print(owner, " is calling in room. Will you call later,please??")
    print("Or will you leave your phone number to him??(y, n) : ")
    answer = input()
    if (answer == "y"):
            number = input("번호 입력 : ")
            print("Is this your number??(y, n) -> ", number)
            ans2 = input()
            if (ans2 == "y"):
                print("Ok, Thanks! I will give your number to my boss^^")
            else:
                print("Sorry, I am busy now. Please call back")
    else:
            print("Ok! Then call later,please^^")
    print("===========================================")
def Auto_Seminarinroom_System(caller, owner, whenst, room):
    thistime = whenst + 1
    whenfin = whenst + 2
    print("Time now : ", thistime)
    print("Hi,",caller, "Sorry to say you this sad sentences")
    print(owner, "is in ", room, "room from ", whenst, " to ", whenfin)
    print("Or will you leave your phone number to him??(y, n) : ")
    answer = input()
    if (answer == "y"):
            number = input("번호 입력 : ")
            print("Is this your number??(y, n) -> ", number)
            ans2 = input()
            if (ans2 == "y"):
                print("Ok, Thanks! I will give your number to my boss")
            else:
                print("Sorry, I am busy now. Please call back")
    else:
            print("Ok! Then call later,please^^")
    print("===========================================")
def Auto_Outside_System(caller, owner, whenst, where):
    thistime = whenst + 2
    whenfin = whenst + 3
    print("Time now : ", thistime)
    print("Hi,",caller, "Sorry to say you this sad sentences")
    print(owner, "is gone to ", where, " from ", whenst, " to ", whenfin)
    print("Or will you leave your phone number to him??(y, n) : ")
    answer = input()
    if (answer == "y"):
        number = input("번호 입력 : ")
        print("Is this your number??(y, n) -> ", number)
        ans2 = input()
        if (ans2 == "y"):
            print("Ok, Thanks! I will give your number to my boss")
        else:
            print("Sorry, I am busy now. Please call back")
    else:
        print("Ok! Then call later,please^^")
    print("===========================================")
<<<<<<< HEAD
def End():
    print("Ok! See you later, sir~~")
=======
def End(caller, loc):
    print("Ok! See you later, ", caller, "~~")
    print("When you are free visit our company^^")
    print("Our company is located in ", loc)
>>>>>>> 8dd2cf42c23f4dfee330cf0d1e527d841626c6de

while (True):
    owner = "Jo Sung Su"
    caller = str(input("What is your name, sir??"))
    loc = "No-Won-Gu"
    Owner(caller, owner, loc)
    print("===========================================")
    menu = int(input("Choose what will you do with my boss?(1-meet in room, 2-checkmyproj, 3-have dish, 4-end) : "))
    print("===========================================")
    if (menu == 1) :
        Auto_Callinginroom_System(caller, owner)
        continue
    if (menu == 2) :
        whenst = random.choice([10, 14, 17, 20])
        room = random.choice([101, 204, 308, 504])
        Auto_Seminarinroom_System(caller, owner, whenst, room)
        continue
    if (menu == 3) :
        whenst = random.choice([9, 12, 15, 17, 20])
        where = ["GangNam", "DongJak", "Jongro"]
        whereIndex = random.randrange(0, len(where))
        if (whereIndex == 0):
            where = "GangNam"
        if (whereIndex == 1):
            where = "DongJak"
        if (whereIndex == 2):
            where = "Jongro"
        Auto_Outside_System(caller, owner, whenst, where)
        continue
    if (menu == 4) :
<<<<<<< HEAD
        End()
=======
        End(caller, loc)
>>>>>>> 8dd2cf42c23f4dfee330cf0d1e527d841626c6de
        break
