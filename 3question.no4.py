

#leap year
'''year = int(input('Enter a year'))

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))

# no parameter and no return type
def add():
    a=int(input('enter a number :'))
    b=int(input('enter a number :'))
    print(a+b)
add()


#parameter and no return type

def sub(a,b):
    print(a-b)
add(4,3)


#no parameter and return type

def mul():
    a = int(input('enter a number :'))
    b = int(input('enter a number :'))
    return(a * b)
c=mul()
print(c)

#with parameter and return type

def div(a,b):
    return a / b
c=div(6,3)
print(c)'''

#write a program to find factorial of a number by using functions

'''num=int(input('enter a number for factorial'))
def factorial(num):
    product = 1
    for i in range(2,num+1):
        product1=product*i
    return num

b=factorial(num)
print(f'the factorial of {num} is {b}')

#WAP to print a multiplication table of a given number by using a function

def mult(num):
    for i in range(1,11):
        pro=num*i
        print(f'{num}*{i}={pro}')

num=int(input('enter number for multiplication'))
mult(num)'''


