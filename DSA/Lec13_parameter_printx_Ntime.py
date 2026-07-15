

def prt(x, n):
    if n == 0:
        return 
    print(x)
    prt(x, n-1)

prt("junaid", 5)