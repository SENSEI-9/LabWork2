'''
3. Price of a house is $1M.
if buyer has good credit,
they need to put down 10% otherwise
they need to put down 20%.
Print the down payment
'''
price_of_the_house=1000000
credit=input('Do you need good credit(yes or no):')
if credit=="yes":
    credit=True
if credit==True:
    price_of_the_house_w=(price_of_the_house*(10/100))
else:
    price_of_the_house_w=(price_of_the_house*(20/100))
print(f'The down payment is ${price_of_the_house_w}')


