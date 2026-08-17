class A:
    def __init__(self):
        print("This is Class A")

    @staticmethod
    def info():
        print("Information about A")


class B:
    def __init__(self):
        print("This is Class B")

    @staticmethod
    def info():
        print("Information about B")



class C(A, B):
    def __init__(self):
        print("This is Class C")

    @staticmethod
    def info():
        print("Information about C")


s1 = C()
s1.info()  # here call the c becuase its own pirority is hire then A and B 


