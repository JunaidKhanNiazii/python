def func(count, n):
    if count == 0:
        return
    func(count-1, n)
    print(count)

func(5, 5)