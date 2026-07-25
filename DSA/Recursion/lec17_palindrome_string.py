string = "Hello"

left = 0
right = len(string) -1

def check_plaindrome(string):
    global left, right
    if left == right:
        return "Palindrome"
    elif  string[left] == string[right]:
        left +=1
        right -=1
        return check_plaindrome(string)
    else :
        return "Not a plaindrome"
    
print(check_plaindrome(string))