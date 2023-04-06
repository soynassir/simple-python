# A program to store weight of the user. V1
from time import gmtime, strftime

user_weight = input('Enter your weight: ')

print(f'Your weight is {user_weight}kg')

date_time = strftime("%d %b %Y at %H:%M:%S", gmtime())

with open('data.txt', 'a') as file:
    file.write(f'{date_time} Your weight was {user_weight}kg\n')
