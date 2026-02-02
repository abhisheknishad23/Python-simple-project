rent = int(input('Enter the flat amount = '))
food = int(input('Enter the amount of food ordered = '))
electricity_bill = int(input('Enter the total of elecricity bill = '))
charge_per_unit = int(input('Enter the charge per unit = '))
persons = int(input('Enter the number of persons living in room = '))

total_bill = electricity_bill*charge_per_unit
output = (food+rent+total_bill) //persons

print('Each persons bill pay = ', output)