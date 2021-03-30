'''
Weight converter:
 input the weight of a person in either kg or lbs.
 if the person provides his/her
 weight in kg then convert it into lbs
 else convert it to kg.
'''

KG=float(2.20462)
Weight=float(input('Enter your weight :'))
kg_or_lbs=input('What is your weight at (kg or lbs):')
if kg_or_lbs=="kg":
    weight1=Weight*KG
    print(f'your weight is {weight1}lbs')
elif kg_or_lbs=="lbs":
    weight2=Weight/KG
    print(f'your weight is {weight2}kg')

