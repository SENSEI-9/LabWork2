'''
4.If temperature is greater than 30,
it's a hot day otherwise if
it's less than 10;
it's a cold day; otherwise,
it's neither hot nor cold.
'''

temperature=int(input('Enter the temperature :'))
if temperature>30:
    print('it is a hot day')
elif temperature<10:
    print('It is a cold day')
else:
    print('It is neither hot nor cold')