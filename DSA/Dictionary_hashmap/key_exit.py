dictionay = {
    "name":"junaid",
    "age": 20,
    "city": "lahore"
}
check = input("Enter key to check: ")
if check in dictionay:
    print("Key exists")
else:
    print("Key does not exist")