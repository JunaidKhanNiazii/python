dictionary = {
    "name" : "junaid",
    "age" : 22,
    "Gender" : "male"
}
dictionary2 = {}
for key,value in dictionary.items():
    dictionary2[value] = key
    
print(dictionary2)
    
# keep in mind that the value should be unique otherwise it will overwrite the previous value.