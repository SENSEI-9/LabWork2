'''
5. If name is less than 3 characters
long - name must be at least 3 characters
otherwise if it's more than
50 characters - name must be maximum of 50 characters
otherwise - name look good!
'''
name=input('Enter your name :')
a=len(name)
if a<3:
    print('Your characters name must be long')
elif a>51:
    print('Your character must be not more than 50 characters')
elif a>3 and a<51:
    print('Your name look good')
