#in this we use the concept of if else operator. 

num1 = int (input("Enter your first number "))
num2 = int (input("Enter your 2nd number "))
operator =  input("Enter your Operator ")

if operator == '+':
    answer = num1 + num2
elif operator == '-':
    answer = num1 - num2
elif operator == '*':
    answer = num1 * num2
elif operator == '/':
    answer = num1 / num2
else:
    print ("Wrong operator")

print(answer)
