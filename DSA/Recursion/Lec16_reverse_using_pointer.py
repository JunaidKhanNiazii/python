array = [0,1,2,3,4,5,6,7,8,9,10]

def reverse(array, left, right):
    if left >= right:
        return array, left, right
    
    array[left], array[right] = array[right ], array[left]
    
    left +=1
    right -=1
    return reverse(array, left, right)
    
    
    
    

array , left , right = reverse(array, 0 , 10)
print (array)
print (left, right)
