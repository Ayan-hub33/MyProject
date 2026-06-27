#dictionary
# lifejournal =  {
#     "key" : "value",
#     "sri chaitanya" : "TNT-B",
#     "aakash" : "ER-05",
#     "JEE MAINS rank"  : 36425,
#     "JEE ADV rank" : 44321,
#     "subjects" : ["PHYSICS" , "CHEMISTRY", "MATHS"] ,
#     12.32 : 41
# }

# print(lifejournal["key"])
# lifejournal["key"] = "Ayan"
# lifejournal["achievement"] = "cracked every exam"
# print(lifejournal)

# emptydict = {}
# emptydict["name"] = "Ayan"
# print(emptydict)

# dic1 = { 
#     "name" : "abc",
#     "dic2" : {     
#   "who" : "when",        #nested dict
#   "where" : "whose",
#   "why" : "we"

# }
# }
# print(dic1["dic2"])
# print(dic1["dic2"]["who"])

#dict methods

# lifejournal =  {
#     "key" : "value",
#     "sri chaitanya" : "TNT-B",
#     "aakash" : "ER-05",
#     "JEE MAINS rank"  : 36425,
#     "JEE ADV rank" : 44321,
#     "subjects" : ["PHYSICS" , "CHEMISTRY", "MATHS"] ,
#     12.32 : 41
# }
 
# print(lifejournal.keys()) 
# print(list(lifejournal.keys()))
# print(len(lifejournal)) #to convert to list
# print(len(list(lifejournal.keys())))
# print(lifejournal.values())
# print(lifejournal.items())
# print(list(lifejournal.items()))
# tupple = list(lifejournal.items())
# print(tupple[3])
# print(lifejournal["aakash"])
# print(lifejournal.get("sri chaitanya")) #preferred
# lifejournal.update({"college" : "PEC"})
# print(lifejournal)

#sets

# set9 = {"a", "b", "c", "d", "e", 5 ,4}
# print(set9)

# set1 = {} #emptydictionary
# set2 = set() #emptyset

# # #set-methods
# A = {"a", "b", "c", "d", "e", 5 , 4}
# # A.add(2)
# # A.add(('1', '2', '3'))
# # A.remove(5)
# # # A.clear()
# # print(A.pop())  #pops random value
# # print(A)
# B = {1, 2, 3, 4 ,5}
# print(A.union(B))
# print(A.intersection(B))

# #1.
# dictionary = {
#     "table" : ["a peice of furniture" , "list of facts and figures"],
#     "cat" : "a small animal",
# }
# print(dictionary)

#2.
# classrooms = {"python","python","python", "java", "javascript","javascript","c++","c++", "c"}
# print(len(classrooms))

#3.

# subjects = {}
# a = float(input("enter physics marks :"))
# subjects.update({"physics" : a})
# b = float(input("enter chemistry marks :"))
# subjects.update({"chemistry" : b})
# c = float(input("enter maths marks :"))
# subjects.update({"maths" : c})
# print(subjects)

#4.
set0 = set()
set0.add(int(9))
set0.add("9.0")
print(set0)

