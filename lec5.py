# while loops
# charge = 1
# while charge <= 4 :
#     print("minimal electric field", charge)
#     charge += 1
  
# force = 5
# while force>=1:
#     print(force)
#     force -= 1

# # #1.
# i = 1
# while i <= 100:
#     print(i)
#     i += 1
    
#2.
# x = 100
# while x >= 1:
#     print(x)
#     x -= 1

#3.
# n = 6
# letnumber = 1
# while letnumber <= 10 :
#     print(n * letnumber)
#     letnumber += 1

#4.
# x = 1
# while x <= 10:
#    print(x*x)
#    x += 1

#5.
# squares = [1,4,9,16,25,36,49,64,81,100]
# num = 0
# while num < 10:
#    print(squares[num])
#    num += 1

#6. ***
# squares = (1,4,9,16,25,36,49,64,81,100)
# y = 49
# x = 0
# while x < len(squares):
#     if(squares[x] == y):
#         print("found" , x)

#     x += 1

#break and continue
# a = 0
# while a <= 5:
#     print(a)
#     if(a == 4):
#         break
#     a += 1

#     squares = (1,4,9,16,25,36,49,64,81,100)
# y = 49
# x = 0
# while x < len(squares):
#     if(squares[x] == y):
#         print("found" , x)
#         break
#     else:
#         print("finding")

#     x += 1

# x = 0
# while x <= 8:
#     if(x == 4):
#      x += 1
#      continue  #acts as skip
#     print(x)
#     x += 1
    
# a = 1      #print odd no.s
# while a <= 10:
#    if(a%2 == 0):
#       a += 1
#       continue
#    print(a)
#    a += 1

# a = 1      #print even no.s
# while a <= 10:
#    if(a%2 != 0):
#       a += 1
#       continue
#    print(a)
#    a += 1

# for loops

# list = [1, 2, 3, 4, 5]
# for val in list:
#     print(val)

# physics = "electrostats"
# for char in physics:
#     if(char == "t"):
#         print('found')
#         break
#     print(char)
# else:
#    print("loop ended")
    
#7.
# squares = [1,4,9,16,25,36,49,64,81,100]
# for val in squares:
#     print(val)

#8. **
# squares = (1,4,9,16,25,36,49,64,81,100,81)
# x = 81
# idx = 0
# for el in squares:
#     if(el == x):
#         print("number found at",idx)
#         break
#     idx += 1
        
#range fn
# for i in range(10):  #range(stop)
#     print(i)

# #range(start,stop,stepsize)

# for i in range(1,8,3):  
#     print(i)

#print even no.s 1-10
# for i in range(2,11,2):
#     print(i)

#9.
# for i in range(1,101):  
#   print(i)

#10.
# for i in range(100,0,-1):  
#   print(i)

#11.
# n = 5
# for i in range(1,11,1):
#     print(n*i)

#pass statement
# for i in range (3):
#      pass

# print("WD = -PdV")

#12.(using for) *??
# n = 4
# sum = 0
# for val in range(1,n+1):
#     sum += val

# print(sum)

#(using while)
# n = 4
# sum = 0
# x = 1
# while x <= n:
#     sum += x
#     x += 1

# print(sum)

#13. *??
# n = 4
# factorial = 1
# for i in range(1,n+1):
#     factorial *= i


# print(factorial)

#(using while loop)
n = 4
factorial = 1
i =1
while i <= n:
    factorial*=i
    i += 1
print(factorial)    
