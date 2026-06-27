# #functions
# def product(x, y):
#     prod = x*y
#     print(prod)
#     return prod

# product(5, 9)

# def div(p, q):
#     return p%q

# remainder = div(10, 3)
# print(remainder)

# def printer():
#     return print("domain of fn is satisfied")

# printer()

# find avg of 3 no.s
# def avg(x, y, z):
#     return (x + y + z)/3

# Avg = avg(3,4,5)
# print(Avg)


# #built in functions
# print("hi", end = " ")
# print("student")

# def sub(a = 5, b = 3):#default values
#     return a - b
# diff = sub()
# print(diff)

# #1.
# colleges = ["IITs", "NITs","IITs","GFTIs"]
# pens = ["reynolds", "trimax", "pentonic"]
# def length(list):
#     return len(list)
# Len = length(colleges)
# Pen = length(pens)
# print(Len, end = " ")
# print(Pen)

#         ###
# def printer(list):
#     for i in list:
#         print(i)

# printer(colleges)

#2.
# neu = ["a","b","c","d","e"]
# def single_line(list):
# #     for el in list :
# #         print(el, end = " ")

# # single_line(neu)

# #3. ***
# def factorial(n):
#     fact = 1
#     for a in range(1,n+1):
#         fact *= a
#     print(fact)

# factorial(6)

#4.
def converter(D):
    return D*95
rupee = converter(10)

print("it would be rupee", end = " ")
print(rupee)


def identifier(num):
    if(num%2 == 0):
        print("Even")
    if(num%2 != 0):
        print("Odd")
identifier(7)