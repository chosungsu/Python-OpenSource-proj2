import random
def Owner(owner):
    print("This company's owner name is ", owner)
def Auto_Callinginroom_System(caller, owner):
    print("Hi,",caller, "Sorry to say you this sad sentences")
    print(owner, " is calling. Will you call later,please??")
    print("===========================================")
def Auto_Seminarinroom_System(caller, owner, whenst, room):
    thistime = whenst + 1
    whenfin = whenst + 2
    print("Time Now : ", thistime)
    print("Hi,",caller, "Sorry to say you this sad sentences")
    print(owner, "is in ", room, "room from ", whenst, " to ", whenfin)
    print("===========================================")
def Auto_Outside_System(caller, owner, whenst, where):
    thistime = whenst + 2
    whenfin = whenst + 3
    print("Time Now : ", thistime)
    print("Hi,",caller, "Sorry to say you this sad sentences")
    print(owner, "is gone to ", where, " from ", whenst, " to ", whenfin)
    print("===========================================")
def End():
    print("Ok! See you later, sir~~")

while (True):
    owner = "JoSungSu"
    Owner(owner)
    caller = str(input("What is your name, sir??"))
    print("===========================================")
    menu = int(input("Choose what will you do with my boss?(1-meet in room, 2-checkmyproj, 3-have dish 4-end) : "))
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
        End()
        break