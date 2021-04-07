'''given three integers, print the smallest one. (three integers should be user input)'''
a=int(input('enter first number'))
b=int(input('enter second number'))
c=int(input('enter third number'))
if a<b and a<c:
    print('a is the smallest number among them')
elif b<a and b<c:
    print(' b is the smallest number among them')
else:
    print('c is the smallest number among them')