class A:
    def __init__(self):
        print("This is Class A")

    @staticmethod
    def info1():
        print("Information about A")


class B:
    def __init__(self):
        print("This is Class B")

    @staticmethod
    def info2():
        print("Information about B")



class C(A, B):
    def __init__(self):
        print("This is Class C")

    @staticmethod
    def info3():
        print("Information about C")


s1 = C()
s1.info2()


