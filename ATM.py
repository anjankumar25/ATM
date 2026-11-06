def atm(a):
    def withdraw(b):
        if b>0 and b<=a:
            cc=a-b
            return cc
        else:
            print("erroe")

        return a
    bal=withdraw(1000)
    print(bal)
    print("withdraw successful")
    def add(z):
        if z>0:
            zv=a+z
            return zv
        else:
            print("invalid")
            return a
    bale=add(100)
    print(bale)
    
    add(2000)
    def check(x):
        print(x)
    check(a)
atm(10000)
