def Auto_Callinginroom_System(caller, owner):
    print("Hi,",caller, "Sorry to say you this sad sentences")
    print(owner, " is calling in room. Will you call later,please??")
    print("Or will you leave your phone number to him??(y, n) : ")
    answer = input()
    if (answer == "y"):
            number = input("번호 입력 : ")
            ans2 = input("Is this your phone number??(y,n) -> ")
            if (ans2 == "y"):
                print("Ok, Thanks! I will give your number to my boss^^")
            else:
                print("Sorry, I am busy now. Please call back")
    else:
            print("Ok! Then call later,please^^")
    print("===========================================")
owner = "JoSungSu"
caller = str(input("What is your name, sir??"))
Auto_Callinginroom_System(caller, owner)
