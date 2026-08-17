
count = 0

def prt(count):
    count +=1
    if count < 4:
        prt(count)
    print("Junaid", count)

prt(count)