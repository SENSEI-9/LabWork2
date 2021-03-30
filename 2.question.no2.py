'''
2.WAP which accepts marks of four subjects and display total marks, percentage and grade.
Hint:more than 70%-> distinction, more than 60%->first, more than 40%->pass,
less than 40%<- fail
'''

Programming=float(input('Enter the marks of programming :'))
Architecture=float(input('Enter the marks of architecture :'))
Maths=float(input('Enter the marks of Maths :'))
English=float(input('Enter the marks of English :'))

Total_Marks=Programming+Architecture+Maths+English
print(f'your total marks obtained is {Total_Marks}')
Percentage=Total_Marks/4
print(f'Your percentage obtained is {Percentage}%')
if Percentage>70:
    print('Congratulations you have secured distinction')
elif Percentage>60:
    print('Congratulations you have secured first division')
elif Percentage>40:
    print('Congralutions you have passed')
elif Percentage<40:
    print('You have failed')