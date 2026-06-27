'''
# what is function ?
# A function is a lock of reusable code of specific task.

# why fynctions?
# 1.Avoid Repetition
# 2.Improves redability
# 3.Easy Debug
# 4.Modular programming

# Function definiftion

# def funtion_name(parameters):
#     """Doc Strings"""
#     statements
#     return value
  def-->keyword
  function_name-->identifiers
  parameters --> input to the function
  return -->  output

#function calling:executing the code
function_name() 

functions are two types
                                  that are
                                  /      \
                       built in function   user define function
builtin function : which are already define
example: print()
input()
sum()
mean()
max()

user define functions:we will create our own logic as per our requirements


'''

#creat a function
# def hello():
#     print("hello world")
# #call the function 
# hello()  

#parameters :variables passed during
#the function definition
# def add(a,b):
#     print(a+b)
# #arguments = values passed during function call
# #calling the function
# add(2,3)#2,3--arguments

'''
types of arguments:
1.positional arguments:
arguments passed in order

example:
def multiply(a,b):
    return a*b
#call the function
# multiply(2,3)    

'''

'''
task:creat a function to calculate
simple interest using positional args
'''
# def calculate(p,t,r):
#     print(p*t*r//100)
# calculate(10,14,15)

'''
3.keyword arguments

def sub(a,b):
    print(a-b)
sub (b=5,a=10)    
'''
#task:call the simple interst function
#using keyword arguments
# def calculate(p,t,r):
#     print(p*t*r//100)
# calculate(p=10,t=20,r=25)  

'''
3.default arguments
example:
def student(name="nani"):
    print(f"student name is {name}")
student()
'''
# def student(name="nani"):
#     print(f"student name is {name}")
# student()

# def student(name="nani"):
#     print(f"student name is {name}")
# student("manoj")

# def student(name,branch="cse"):
#     print(f"student name is {name} and branch is {branch}")
# student("manoj")

'''
task:creat a function to calc 
squares by default parameters
'''
# Function to calculate square using default parameter

def square(a,b=2):
    print(a**b)
square(10)

'''
4.variables length arguments
def total(*args):
    print(args)
#call the function 
total(10,20,30,40)    
'''
# def total(*args):
#     print(args)
# #call the function 
# total(10,20,30,40)  

# def total(*args):
#     print(args)
#     print(sum(args))
# #call the function 
# total(10,20,30,40)  

'''
task: creat a function to find sum of any number of values
'''
'''
task: create a function to find sum of any number of values
'''

# def total(*args):
#     print("Sum =", sum(args))

# # function calls
# total(10, 20, 30)
# total(5, 15, 25, 35)
# total(1, 2, 3, 4, 5)

#kwargs --> keyword arguments
# def student_deatils(**kwargs):
#     print(kwargs)
# student_deatils (name="rajesh",branch="cse",rollno="12")  


#create a function to print employee details using kwargs
# def employee_deatils(**kwargs):
#     print(kwargs)
# employee_deatils (name="rajesh",id="23546487",salary="10000")  


#write args and kwargs together
# def together(*args,**kwargs):
#     print(args,kwargs)
# together(name="rajesh",id="23546487",salary="10000")
# together(10,20,30,40) 

'''
return statement : send the value
def add(a,b):
    return a+b
    

result = add(10,20)
print(result)


print            |        return
display the output       send the value
cannot resue         can resue

mutiple return values:
def calculate(a,b):
    return a+b,a-b,a/b
format: tuple

s,sub,div = calculate (20,30)

#     '''
# def calculate(a,b):
#     return a+b,a-b,a/b
# #format: tuple

# s,sub,div = calculate (20,30)
# print(s,sub,div)

# def calculate(a, b, c, d):
#     numbers = [a, b, c, d]

#     minimum = min(numbers)
#     maximum = max(numbers)
#     average = sum(numbers) / len(numbers)

#     return minimum, maximum, average

# # unpack the returned tuple
# minimum, maximum, average = calculate(20, 30, 40, 50)

# print("Min =", minimum)
# print("Max =", maximum)
# print("Avg =", average)

'''
doc string describe
1.what function does
2.parameters
3.return Value
def  add(a,b):
    """ this function adds two numbers and returns result"""
    
    return a+b
print(add.__doc__)    
# '''
# def  add(a,b):
#     """ this function adds two numbers and returns result"""
    
#     return a+b
# print(add.__doc__) 
# print(help(add))

#task: write a docstring for the simple interest program
# def calculate(p,t,r):
#     """ this function calculate three numbers and returns result"""
#     print(p*t*r//100)
# print(calculate.__doc__)

'''
#1.local scope:
#variable declared inside the function
'''
# def test():
#     x =100
#     print(x)
# test() 


#globalscope
# def test():
#     x =100
#     print(x)
# test() 

# x = 200 #global variable
# def show():
#     print(x)
# show()

#accessing the local var outside the function
# x=0
# def update():
#     global x
#     x=x+5
# update() 
# print(x)   
    
'''
task :is without using the global and tell me error
'''    

# x = 0

# def update():
#     x = x + 5

# update()
# print(x)

'''
task:
create a function bank_transaction()
which accepts:
1.account holder (string)
2.balance
3.transaction_type(deposit/withdraw)
4.amount

use:
default arguments
return statements
global balance
print updated balance
'''
# balance = 1000   # global balance

# def bank_transaction(account_holder="Guest",transaction_type="deposit",amount=0):
#     global balance

#     if transaction_type == "deposit":
#         balance += amount
#         print(f"{account_holder} deposited {amount}")

#     elif transaction_type == "withdraw":
#         if amount <= balance:
#             balance -= amount
#             print(f"{account_holder} withdrew {amount}")
#         else:
#             print("Insufficient Balance")

#     return balance


# updated_balance = bank_transaction(account_holder="Narendra",transaction_type="deposit",amount=500
# )

# print("Updated Balance =", updated_balance)

    
# balance = 1000
# def bank_transaction(account_holder,transaction_type,amount=0):
#     global balance
#     if transaction_type=="deposit":
#         balance+=amount
#         print(f"{account_holder} deposited{amount}")
#     elif transaction_type=="withdraw":
#         if amount<=balance:
#             balance-=amount
#             print(f"{account_holder} withdraw {amount}")
#         else:
#             print(f"insufficient balance for { account_holder}")
#     else:
#         print("invalid transaction type")
#     print(f"updated balance {balance}")
#     return balance
# bank_transaction("nani","deposit",500)
                

'''
lambda function: is a small and anonymous function
#function without name 
#define using lambda
can pass any number of argument


normal function

def add(a,b):
    return a+b
#write using lambda
add = lambda a,b:a+b
#calling the function
add (10,20)    
'''
# print((lambda x:x*x)(5))

#max number in 2
#ternary : ?:
#python:a if a>b else b
# max_num = lambda a,b:a if a>b else b
'''
arr = list(map(int,input().split()))

#map():applies the function each element of iterable
map(function,iterable)

example:
def square():
   return x*x
   
nums = [1,2,3,4]
result = list(map(square,nums))
print(result)   '''
# def square(x):
#    return x*x
   
# nums = [1,2,3,4]
# result = list(map(square,nums))
# print(result) 


#write with lamdba
# nums = [1,2,3,4]
# result = list(map(lambda x:x*x,nums))
# print(result) 

#task:given a list of numbers
#convert each number into cubes
#using map() and lambda
'''
what is filter?
select the elements based upon the condation

syntax:
filter (function,iterable)

example:
def is_even(x):
    return x%2==0
list = [1,2,3,4,5]
result=filter(is_even,list)
print(result)    
'''
# def is_even(x):
#     return x % 2 == 0

# nums = [1, 2, 3, 4, 5]

# result = filter(is_even, nums)

# print(list(result))

#task:given with list with frnds names 
#filter the names letter starting with a
# friends = ["anil", "ravi", "arun", "kiran", "akhil"]
# print(list(filter(lambda name: name.startswith('a'), friends)))
'''
what is reduce?
repeatedly applies function
reduce the iterable to single value
syntac:
reduce(function,iterable)
#functools--->module
# from functools import reduce
'''
from functools import reduce

# nums = [1,2,3,4,5]
# result = reduce(lambda a,b:a+b,nums)
# print(result)
from functools import reduce

def add(a, b):
    return a + b

nums = [1, 2, 3, 4, 5]
result = reduce(add, nums)

print(result)