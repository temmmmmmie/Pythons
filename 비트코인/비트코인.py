import random
#시스템---------------------------
def all():
    have = []
    global 초기자본

    def lose():
        print("파산했습니다!")
        print("다시 하시겠습니까? y/n")
        re = input()
        if re == "y":
            all()
        elif re == "n":
            exit()
    
    def know():
        global 초기자본
        if 초기자본 < 0:
            lose()
        print("a는" + str(A))
        print("b는" + str(B))
        print("c는" + str(C))
        print("현재"+ str(have) + "와 " + str(초기자본) + "원을 보유하고 있습니다")
        print("어떤 것을 매수 하시겠습니까?" )
        x = input()
        buy(x)

    def buy(x):
        global 초기자본
        if 초기자본 < 0:
            lose()
        if x == "a":
            print("A를 매수했습니다")
            초기자본 = 초기자본 - A
            have.append("a")
        elif x == "b":
            print("B를 매수했습니다")
            초기자본 = 초기자본 - B
            have.append("b")
        elif x == "c":
            print("C를 매수했습니다")
            초기자본 = 초기자본 - C
            have.append("c")
        elif x == " ":
            pass
        else:
            print("잘못 입력했습니다")
            buy(x)
        sell()   


    def sell():
        global 초기자본
        if 초기자본 < 0:
            lose()
        print("어떤 것을 매도 하시겠습니까?")
        y = input()
        if y == "a":
            if "a" in have:
                have.remove("a")
                print("A를 매도했습니다")
                초기자본 = 초기자본 + A
            else:
                print("A가 없습니다")
                sell()
        elif y == "b":
            if "b" in have:
                have.remove("b")
                print("B를 매도했습니다")
                초기자본 = 초기자본 + B
            else:
                print("B가 없습니다")
                sell()
        elif y == "c":
            if "c" in have:
                have.remove("c")
                print("C를 매도했습니다")
                초기자본 = 초기자본 + C
            else:
                print("C가 없습니다")
                sell()
        elif y == " ":
            pass
        else:
            print("잘못 입력했습니다")
            sell()
        upordown()


    def upordown():
        global A
        global B
        global C
        global 초기자본
        if 초기자본 < 0:
            lose()
        a = random.randint(-200, 200)
        b = random.randint(-5000, 5000)
        c = random.randint(-10000, 10000)
        A = A+a
        B = B+b
        C = C+c
        if A < 0:
           A = 0
        if B < 0:
           B = 0
        if C < 0:
           C = 0
        know()


    global A
    global B
    global C

    A = 1000
    B = 1000
    C = 1000

    초기자본 = input("초기자본을 입력하세요 ")
    초기자본 = int(초기자본)
    know()
all()

