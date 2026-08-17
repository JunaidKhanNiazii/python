dictionary = {
    "name" : "junaid",
    "age" : 22,
    "Gender" : "male"
}
dictionary2 = {
    "name1" : "Ahmad",
    "age1" : 21,
    "Gender1" : "male",
    "new " : "one"
}

dictionary.update(dictionary2)

print(dictionary)
#if the key is already present in the dictionary then it will update the value otherwise it will add a new key value pair.