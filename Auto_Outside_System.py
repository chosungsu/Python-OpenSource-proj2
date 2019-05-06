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
        print("Is this number??(y, n) -> ", number)
        ans2 = input()
        if (ans2 == "y"):
            print("Ok, Thanks! I will give your number to my boss")
        else:                                                                                           print("Sorry I am busy now, so please call back to us")
    else:
        print("Ok! Then call later,please^^")
    print("===========================================")
owner = "JoSungSu"
caller = str(input("What is your name, sir??"))
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
