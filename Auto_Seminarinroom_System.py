import random
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
owner = "JoSungSu"
caller = str(input("What is your name, sir??"))
whenst = random.choice([10, 14, 17, 20])
room = random.choice([101, 204, 308, 504])
Auto_Seminarinroom_System(caller, owner, whenst, room)
