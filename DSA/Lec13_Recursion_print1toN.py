
def func (count, n):
    if count == n:
        return
    print(count)
    func(count+1, n)

n = int(input("Enter a number: "))
func(0, n)