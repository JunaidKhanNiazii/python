def func(count, n, sum):
    if count == n+1:
        print("Sum of 1 to N numbers is: ", sum)
        return
    sum +=count 
    func (count + 1, n, sum)

n = int(input("Enter a number: "))
func(1, n, 0)


    