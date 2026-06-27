#list
# age = [11,12,13,14,15]
# print(type(age))
# print(age[1])
# print(len(age))


# age[0] = "classic"
# print(age[0])    #lists are mutable unlike strings

# age = [11,12,13,14,15]
# print(age[0:3])

#list methods
# age = [11,12,13,14,15,10]
# # age.append(1)
# # print(age)
# # age.sort()
# # print(age)
# # age.sort(reverse = True) / age.reverse
# # print(age)
# # age.insert(1,9)
# # print(age)
# age.pop(3)
# print(age)

#tuples
# tupple = ("merry","day", "rose", "flower", )
# print(type(tupple))
# print(tupple[0:2])
# print(tupple.index("merry"))
# print(tupple.count("merry"))

# #1.
# movies = [input("enter movie") , 
#           input("enter movie") , 
#           input("enter movie")    ]
# print(movies)
      
#             #OR

# Movies = []
# mov1 = input("enter movie 1")
# mov2 = input("enter movie 2")
# mov3 = input("enter movie 3")

# Movies.append(mov1)
# Movies.append(mov2)
# Movies.append(mov3)

# print(Movies)

# #2. ***
# num1 = ["a" , "b" , "a"]

# var1 = num1.copy()
# var2 = num1.copy()
# var2.reverse()

# if(var1 == var2):
#     print("the list provided is a palindrome")
# else:
#     print("false input")    
 
#3.

students = ("C" , "D" , "A", "A", "B" ,"B", "A")
print(students.count("A"))


students = ["C" , "D" , "A", "A", "B" ,"B", "A"]
students.sort()
print(students)

print("AYAN")