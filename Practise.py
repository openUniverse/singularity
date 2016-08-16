# # 1. Define a function max() that takes two numbers as arguments and returns the largest of them.
# # Use the if-then-else construct available in Python.
# # (It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)
#
# def max (a, b):
#     if a>b:
#         return a
#     else:
#         return b
#
# print(max(8, 11))
#
# # 6. Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers.
# # For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.
#
# # n+=x means store n + x in n (means n = n + x)
# # n*=x means store n * x in n
# # = is not equals to it is store in
#
# NumList=[1, 2, 3, 4]
#
# def sum (list):
#     n=0
#     for element in list:
#         n+= element
#     return n
# print (sum(NumList))
#
# def mult (list):
#     n=1
#     for element in list:
#         n*= element
#     return n
# print (mult(NumList))


# 7. Define a function reverse() that computes the reversal of a string (string is a list of characters.
# For example, reverse("I am testing") should return the string "gnitset ma I". (Strings enver need to be reversed, dumb question.
# to do so hwoever, is "snake kobra" [::-1]

print ("snake kobra" [::-1])
pokemon = "snake kobra"
print (pokemon [::-1])

#the follwoing is a more complicated method to teach what each indivual thing in it means

def reverse(list):
    length = len(list) # len gets the length of a list
    newList = [] # creates a new, empty list
    for element in range (0, length): # rangecreates a new list (x, y) from start number (x) to end number (y)
        newList.append(list[(length-1) - element]) # "for containerName in" is a loop method
                                                   # .append is add to newList. A list is x long but python coutns starting from 0
                                                   # so length-1 is the position of the last element.
                                                   # it is building the list start at element 0
                                                   # ending position minus puts the ending element first then the next position is 1
                                                   # so it works backwards
    return "".join(newList) #join the string in newList as string eg turn ["q","w","x"] into [qwx]





# PList= "snake kobra"
#
# print (PList.reverse ())
#
# # def reverse(list):
# #     length = len(list) #len will get the length as a number
# #     RevList = [] #Creates a new, empty list
# #     for element in range(0, length): #creates a new list (x, y) from x to y
# #         tempIndex = (length-1) - element
# #         RevList.apend(list(tempIndex))
# #     return "".join(RevList)

#Splitting Practise

