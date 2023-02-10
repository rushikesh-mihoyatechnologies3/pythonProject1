########## interview programs ##################






# import math
# 1. Write a program to swap two numbers.


# a = 20
# b = 30

# atemp = b

# b = a

# print(f'a ={atemp}\n b = {b}')

# a,b = b,a

# print(f'a ={a}\n b = {b}')


# a = a + b

# b = a-b
# a =a-b

# print(f'a ={a}\n b = {b}')


###################################################################################################


# 2. How to check number is prime or not.


# num = 2

# # If given number is greater than 1
# if num > 1:

# # Iterate from 2 to n / 2
#     for i in range(2, int(num/2)+1):

#         # If num is divisible by any number between
#         # 2 and n / 2, it is not prime
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")

# else:
#     print(num, "is not a prime number")


# number  = int(input("please entered valid no for checking is it is prime or not : "))


# if number > 1:

#     for i in range(2,int(number/2)+1):

#         if (number%i)==0:
#             print(f"{number} given number is not a prime number")
#             break
#     else:
#         print(f'{number} is a prime number')

# else:
#     (f"{number} number is not a prime number")


######################################################################################################################


# 3. How to find factorial of a number


# we find factorial of number by 2 methods


# by using function recurtion

# number = input("please entered valued number : ")

# def factorialfuncton(number : int):

#     if number ==1 or number ==0:

#         return 1

#     else:

#         return number*factorialfuncton(number-1)


# value = factorialfuncton(int(number))

# print(value)


# second method

# counter = 6
# result = 1

# while counter >= 1:

#     result = result*counter
#     counter = counter-1

# print(result)


#############################################################################################################


# 6. How to find maximum and minimum elements in an array or list?


# from curses.ascii import isdigit


# alist = [2,15,14,46,84,75,64,2,1,100]


# maxnumber = max(alist)
# minnumber = min(alist)

# print(f" max number in list : {maxnumber} \n minimum number in list = {minnumber}")


# 5. How to find the sum of elements in an array or list ?

# alist = [2,15,14,46,84,75,64,2,1,100]
# strvariable = "hdhjshdjh12gs45dnd54dhd856d"
# sum = 0

# for item in alist:

#     sum = sum + item

# print(sum)

# counter = 1

# sum = 0


# for item in strvariable:

#     if item.isdigit() == True:


#         sum =sum + int(item)

# print(sum)

#############-----------------------
# import re
# # By using regular expresssion
# strvariable = "hdhjshdjh12gs45dnd54dhd856d"
# sum = 0
# matcher = re.findall('\d',strvariable)

# for i in matcher:

#     sum = sum + int(i)

# print(sum)


####################################################################################

# 7. How to find the length of the list?

# strvariable = "hdhjshdjh12gs45dnd54dhd856d"


# print(f'length of given string is = {len(strvariable)}')


#############################################################################################


# 8. How to swap first and last elements in the list


# alist = [2,15,14,46,84,75,64,2,1,1000]


# def swipfunction(a=list):

#     a[0],a[-1]= a[-1],a[0]

#     print(a)

# swipfunction(alist)


# 9. How to swap any two elements in the list?

# alist = [2,15,14,46,84,75,64,2,1,1000]


# def Anyswipe( a : list = [0]):

#     a.reverse

#     print(a)

# Anyswipe(alist)


#################################################################


# 10. How to remove the Nth occurrence of a given word list


# alist = [2,15,14,46,84,75,64,2,1,10,14,2,10,21,14]


# adictinary = {}


# for element in alist:


#     if element in adictinary:

#         adictinary[element] = adictinary[element]+1

#     else:

#         adictinary[element] = 1

# print(adictinary)


# 11. How to search an element in the list?


# alist = [2,15,14,46,84,75,64,2,1,10,14,2,10,21,14]


# def search(glist:list,pattern):

#     for i in range(len(glist)):

#         if glist[i] == pattern:

#             return(f"given pattern is present in alist ")


#     return(f" pattern is not present in list ")


# result = search(alist,14)

# print(result)

# ****************************************************************************************************************************************


# How to search an element in the list?

# alist = [2,15,14,46,84,75,64,2,1,10,14,2,10,21,14]

# Element = int(input("please enter a list element : "))


# if Element in alist:
#     print(f"{Element} isExist")

# else:
#    print(f"{Element} Does not Exist")


#######################################################################

# 12. How to clear the list?

# alist = [2,15,14,46,84,75,64,2,1,10,14,2,10,21,14]


# def clarfunction(a:list):

#     a.clear()

#     return(a)

# result = clarfunction(alist)
# print(result)

###################################################################
# 13. How to reverse a list?


# alist = [2,15,14,46,84,75,64,2,1,10,14,2,10,21,14]


# def reversefunction(a:list):

#     a.reverse()

#     print(a)

# reversefunction(alist)


####################################################


# 14. How to clone or copy a list?

# alist = [2,15,14,46,84,75,64,2,1,10,14,2,10,21,14]


# def clonefunction(a:list):

#     a.copy()
#     print(a)

# clonefunction(alist)


##############################################################################################


# 15. How to count occurrences of an element in a list?


# alist = [2,15,14,46,84,75,64,2,1,10,14,2,10,21,14]


# adict = {}


# for element in alist:

#     if element in adict:

#         adict[element] = adict[element]+1

#     else:

#         adict[element] = 1

# print(adict)


##########################################################################################

# 17. How to multiply all the numbers in the list? 18. How to find the smallest and largest numbers on the list?

# alist = [2,15,14,46,84,75,64,2,1,10,14,2,10,21,14]

# userinput = int(input("please entered a number which you want to multiply a given list : "))

# for element in alist:

#     print(f" Element in list multiply by given user input No. : {userinput} = {element*userinput} ")


#################################################

# 18. How to find the smallest and largest numbers on the list?

# alist = [2, 15, 14, 46, 84, 75, 64, 2, 1, 10, 14, 2, 10, 21, 14]

# def MaxMInfunction(a:list):

#     print(f'Max number in given list = {max(a)}')
#     print(f'Min number in given list = {min(a)}')

# MaxMInfunction(alist)


###################################################################################################################


# 19. How to find the second largest number in a list?

# alist = [2,15,14,46,84,75,64,2,1,10,14,2,10,21,14]


# def secondhighestNumber(a:list):

#     (a.sort())
#     print(a[-2])

# secondhighestNumber(alist)


# 20. How to check string is palindrome or not?

# palindrome meanse when we see string left to right or right to left it seen like same

'''What is palindrome string examples?
A string is called a palindrome string if the reverse of that string is 
the same as the original string. For example, radar , level , etc. Similarly, 
a number that is equal to the reverse of that same number is called a palindrome number.
For example, 3553, 12321, etc'''

# def checkpalidrome(inputstr : str) :

#     if inputstr[::-1] == inputstr:

#         print("given string is palindrom")

#     else:

#         print("given string is not palidrome")


# checkpalidrome("rever")


##############################################################################################

# 21. How to reverse words in a string?


# string = "rushikesh"


# def reveresestringFuncion(a:str):

#     print(a[::-1])


# reveresestringFuncion(string)


######################################################################################


# 22. How to find a substring in a string?


# string = str(input("please entered valid string : "))

# substring = str(input("please entered valid substring : "))

# if substring in string:

#     print(f" {substring} given substring is present in {string}")

# else:

#     print(f"{substring}is not present in given {string}")

# *************************************************************************8

# or by using re

# import re

# string = str(input("please entered valid string : "))

# substring = str(input("please entered valid substring : "))


# matcher = re.search(substring,string)

# if matcher != None:

#     print(f" the given {substring} is present in given {string}")

#     print(f"the starting index of given {substring} = {matcher.start()} \n the ending  index of given {substring} = {matcher.end()}")

# else:
#     print(f" the given {substring} is not present in given {string}")

##################################################################################

# 23. How to find the length of a string?


# string = "rushikesh"


# def Findlength(a:str):

#     print(len(a))

# Findlength(string)


# 24. How to check if the string contains any special character?

# import re

# stringvaribale = input("please entered valid string")


# matchers = re.finditer('\W',stringvaribale)     # we use also [^a-zA-Z1-9]

# for m in matchers:

#     print(f"the index of given string is  ={m.start()} \n the special charecter from given string = {m.group()}" )


# 25. Check for URL in a string

# string = "hfh"

# import re

# matcher = re.finditer('www.','')


# # for m in matcher:

# matcher.


#####################################


# 26. to find the number in string
# import re

# stringvariable = "hdhfkf2d3j5k6d39383"
# sum = 0
# matcher = re.findall('\d',stringvariable)

# for m in matcher:

#     print(f"the number in given string = {m}")


###################################
# import re
# string = "hfhcmcj5477@4bfhjk8r6"


# matcher =  re.findall("[^a-zA-Z1-9]",string)
# sum = 0
# for m in matcher:

#     print(f"special charecter from given string = {m}")


################################################################

# write febanisi series
# try :
#     feb0 = 0

#     feb1 = 1

#     number = int(input('please entered valid number :'))


#     for element in range(0,number):

#         newfeb = feb0+feb1
#         feb0 = feb1
#         feb1 = newfeb
#         print(feb0 , end=' ')

# except Exception as e:
#     print(f"please give valid input error  : {e}")


###################################3

# how to find second accurance in given input string

# string  = input('please entered valid string :')

# substring = input("please entered valid substring : ")

# firstaccurance = string.find(substring)
# secondaccurance = string.find(substring,firstaccurance+1)
# print(f' first accurance of given string = {firstaccurance}')
# print(f' second accurance of given string = {secondaccurance}')


###################################################################
# how to remove dulicate record
# alist = [51,12,34,32,22,2,31,12]
# newlist = []
# for i in alist:

#     if i not in newlist:

#         newlist.append(i)
# print(newlist)


#####################


# delete duplicate from the string and keep only unique value

# astring =  'rushikesh'

# a = ''

# for char in astring:
#     if char not in a:
#         a = a + char
# print(a)

#####################################################################

# delete duplicate from the list and keep only unique value

# astring = 'rushikesh'


# new = ''


# for i in astring:

#     if i not in new:

#         new = new+i
# print(new)


# string is balanced or not

# def isbalanced(s):
#   c= 0
#   ans=False
#   for i in s:
#     if i == "(":
#      c += 1
#     elif i == ")":
#      c-= 1
#     if c < 0:
#      return ans
#     if c==0:
#      return not ans
#   return ans
# s=""
# print("Given string is balanced :",isbalanced(s))


# ### how to find uniq words in file.


# file = open("path of file")

# words = file.open()

# words = words.split()

# newlist = []

# for word in words:

#   if word not in newlist:

#      newlist.append(word)

# print(newlist)


###############################################
# anumber = 453
# reveres = 0
# while anumber !=0:
#     reveres = (reveres*10) + (anumber%10)

#     anumber = anumber//10
# print(reveres)


####################################################################
# Q.  Reverse String Without Changing Place of Special Characters

# astring = 'rushikesh@'

# samplelist = list(astring)

# i = 0
# j = len(samplelist)-1

# while i < j:

#     if not samplelist[i].isalpha():
#         i = i +1
#     elif not samplelist[j].isalpha():
#         j = j-1
#     else:
#         samplelist[i],samplelist[j] = samplelist[j],samplelist[i]
#         i = i +1
#         j = j -1

# newastring = ''.join(samplelist)

# print(newastring)


#########################################################################


# # Program to determine whether one string is a rotation of another

# def rotating(a,b):


#     if len(a) != len(b):

#         return False
#     else:
#         new = a+a

#         if b in new:
#             return True
#         else:
#             return False

# avaribel = 'deabc'

# bvaribale = 'abcde'

# if (rotating(avaribel,bvaribale)):

#     print('yes')
# else:
#     print("not")

print('hello')


# how to swipe charecter without special

astring = 'rushikesh@'

listSample= list(astring)

i = 0
j = len(listSample) - 1

while i < j:
    if not listSample[i].isalpha():
        i += 1
    elif not listSample[j].isalpha():
        j -= 1
    else:
        # swap the element in the list
        # if both elements are alphabets
        listSample[i], listSample[j] = listSample[j], listSample[i]
        i += 1
        j -= 1

# convert list into string
# by concatinating each element in the list
print(listSample)
strOut = ''.join(listSample)
print(strOut)


print('hello this is pull request")

print('hello this is pull request")

      print('hello this is pull request")

print('dhdhjdjdj')

