# def p(a, b):
#     if b is 0:
#         return a
#     else:
#         return a * p(a, b -1)
#
# w = 5
# print(p(w, 8))
# # 5*(2 - 1)
#
# def universe(input, apples, bread):
#     if input == "hello":
#         print("hi")
#     else:
#         print("f u")
#     if apples == "red":
#         print("yum")
#     else:
#         print("boo")
#     if bread == "old":
#          print("throw it away")
#
#
#
#
# universe("hello", "bread", "old")

#


# synonymsForHello = ['hey', 'hi']
# sforgood = ['great', 'good']
# anylist = [synonymsForHello, sforgood]
#
# def printList( items ):
#         for item in items
#             print(item)

# index 0 1 2  3
# list = "snake kobra"
#
# def reverse(list):
#     length = len(list)  #get length of a list
#     newList = [] # create a new empty list
#     for element in range(0,length ): # range means create a list from the start number to the en# d number i.e. [0,1,2,..., length]
#         newList.append( list[(length-1) - element]) # append is add it to a new list
#     return "".join(newList) #["q","w","e","r","t"]
#
# print("".join(["q","w","e","r","t"]))
# print("-".join(["q","w","e","r","t"]))
# print(" ".join(["q","w","e","r","t"]))
#
# print("Whatever you put in here".join(["q","w","e","r","t"]))
#
aString = "Anything between quotes"
#
print( aString )

theStsringCapitalzies = aString.capitalize()

print(theStsringCapitalzies)

print(aString)#notice how it hasn't changed

aString = "My name is * and I have * cats and * dog"
print( aString )

arrayOfStrings = aString.split("*")
print(arrayOfStrings)#this would be our pattern

letSayUserSaidThis = "My name is Bob and I have 2 cats and 1 dog"
#to get the name and number of each animal we can split again!


print( letSayUserSaidThis.split(arrayOfStrings[0])[1].split()[0])
print( letSayUserSaidThis.split(arrayOfStrings[0])[1].split())
print( letSayUserSaidThis.split(arrayOfStrings[0])[1])
print( letSayUserSaidThis.split(arrayOfStrings[0]))
print( letSayUserSaidThis.split())

numberOfCat = letSayUserSaidThis.split(arrayOfStrings[1])[1].split()[0]
numberOfDogs = letSayUserSaidThis.split(arrayOfStrings[2])[1].split()[0]

#any list is [1,23,34,5], ['1','2','d']
#a string is anything between quotes"asdfasdf"
print(name)
print(numberOfCat)
print(numberOfDogs)