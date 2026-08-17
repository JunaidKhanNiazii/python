def func (count, n, sum):
    if count == n + 1:
        return sum
    sum +=count
    return func (count + 1, n, sum)

print(func (1, 10, 0))
