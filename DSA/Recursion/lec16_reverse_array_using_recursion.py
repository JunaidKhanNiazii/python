array = [1,2,3,4,5,6,7,8,9,10]

def reverse(arr):
    
    if len(arr) <=0:
        return arr
    
    return [arr[-1] ] + reverse(arr[:-1])

print(reverse(array))