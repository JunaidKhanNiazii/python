class person1:

    def __init__(self):
        self.__name = False # private attribute
        self.word = "word1 " # public attribute

    def __hello(): # private method
        print("Hello world")
    def newone(self): # public method
        print("Hello" + self.word ,self.__name )

s1 = person1()

# print(s1.__name)
# print(s1.word)
s1.__hello()
# s1.newone()
        