def Auto_Seminarinroom_System(caller, owner, whenst, room):
    whenfin = whenst + 2
    print("Hi,",caller, "Sorry to say you this sad sentences")
    print(owner, "is in ", room, "room from ", whenst, " to ", whenfin)
    print("===========================================")
owner = "JoSungSu"
whenst = random.choice([10, 14, 17, 20])
room = random.choice([101, 204, 308, 504])
Auto_Seminarinroom_System(caller, owner, whenst, room)