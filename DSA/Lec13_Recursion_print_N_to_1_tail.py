def fuct(count, n):
    if count == n:
        return
    fuct(count+1, n)
    print(count)


fuct(1,5)