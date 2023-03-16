# name = input("name: " )
# print("hello ", name)
# string literals
# print(f"hello, {name}")
n = input("enter number ")

if int(n) > 0:
    print("number is greater than 0")
elif int(n) == 0:
    print("number is = 0")
else:
    print("number is less than 0")

# data structures
    # list
    # set
    # tuple
    # dictinary

# example of list;

names = ['arman','geeks','qouda','zariyatu','al-amin','ridollah']

# methods and properties a list have.
    # 1. append(the data)
    # 2. sort()

# example of set structure

data_set = set()

data_set.add("arman")
data_set.add("maryam")

# the add method appends data at the begining of the set
# other methods are
    # 1. remove(the value)
    # 2. len(str,list, set)

# loops in pyhon

#code example

for i in [1,2,3,4]:
    print(i)

for i in range(100):
    print(i)

# the dictionary

partners = {"qouda":"kamila", "arman":"zainab"}

print(partners["qouda"])

# functions

# example

# def add(n1,n2):
#     return n1 + n2

# print(add(10,20))

#decorators
#decoratores are used to take functions and modify them by adding some behaviours to them. 
    # it allows functuinal programming paradigm. example below

def anounce(f):
    def wrapper():
        print("hellow")
        f()
        print("done action")
    return wrapper
@anounce   
def Hello():
    print("hello, world")

Hello()
        
        




