def Auto_Outside_System(caller, owner, whenst, where):
    whenfin = whenst + 3
    print("Hi,",caller, "Sorry to say you this sad sentences")
    print(owner, "is gone to ", where, " from ", whenst, " to ", whenfin)
    print("===========================================")
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