# find the fabanacci number 
# 0 1 1 2 3 5 8 13 21 34 ....
# using a recursion 
array = [0,1]
length = int(input("Enter size of fabnacci series : ")) - 1
def function(array, size, count):
    
    if count  < size:
        array.append(array[count - 1] + array [count])
        
        return function(array, size, count+1)
    else:
        return array
        
    

print(function(array, length, 1))

