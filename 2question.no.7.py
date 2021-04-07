'''
no 5 .for given integer x, print 'True' if it is positive,
print "False" if it is negative and print 'zero' if it is zero'''

x=int(input('Enter any integer number to check if it is +ve,-ve or zer0 :'))
if x>0:
    print('It is a positive integer')
elif x<0:
    print('It is a negative integer')
elif x==0:
    print('It is zero')
