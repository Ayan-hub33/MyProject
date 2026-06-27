#escape sequence characters
# str = "this is a string.\n we are learning"
# print(str)
# # # \t = tab space
# # \n = next

# str1 = "this is lecture no.2"
# str2 = "let's learn"
# final = str1 + " " + str2
# print(final)#concatination

# print(len(str1))#length

# str = "Mathematics and Computing"
# print(str[12])#indexing
# print(str[1:8])#slicing
# print(str[0:len(str)])#for complete str
# # [:]=[0:0]

#string functions
# str = "mathematics and Computing" 
# print(str.endswith("ing"))
# print(str.capitalize())
# str1 = str.capitalize()
# print(str1)
# print(str.replace("a","p"))
# print(str.find("l"))
# print(str.count("math"))

# #1.
# str = input("write first name :")
# print(len(str))

#Conditional statements
# subject = "biology"
# if(subject == "chemistry"):     #indentation-prper spacing
#  print("it is very scoring\ni used to practice it often.")
# elif(subject == "physics"):
#  print("intersting yet can be challenging")
# elif(subject == "maths"):
#  print("concentration is the key")
# else:
#  print("you're at the wrong place.")

# marks = int(input("enter your marks"))
# if(marks >= 90):
#     print("grade A")
# elif(90>marks>=80):
#     print("grade B") 
# elif(80>marks>=70):
#     print("grade C") 
# elif(marks<70):
#     print("grade D")

# #nesting
# age = int(input("enter your age"))
# if(age >= 18):
#     if(age >= 80):
#          print("not eligle")
#     else:
#      print("eligible")    
# else:
#  print("not eligible")   

#2. **
# num = int(input("enter number"))
# if(num%2 == 0):
#     print("number is even")

# else:
#     print("number is odd")

# #3. **
# x = int(input("no. 1 :"))
# y = int(input("no. 2 :"))
# z = int(input("no. 3 :"))

# if(x>y and x>z):
#     print("X is greatest")
# elif(y>x and y>z):
#     print("Y is greatest") 
# elif(z>x and z>y):
#     print("Z is greatest")       

x = int(input("enter number"))
if(x%7 == 0):
    print("it is div. by 7")

elif(x%7 != 0):
    print("it is not div. by 7")    