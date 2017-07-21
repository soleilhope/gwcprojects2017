
from random import *


#Create the list of words you want to choose from.
meats = ["steak","squid","calamari","roast beef","oxdail","chicken wings","chicken tenders","orange chicken","mongolian beef","barbeque ribs"]
sides = ["french fries","rice cake","salad","mashed potatoes","hawaiian roll"]
dessert = ["hot sundae","triple chocolate cake","vanilla ice cream","italian ice"]
drinks = ["soda","sweet tea","water","lemonade"]
#Generates a random integer.
x = randint(0, len(meats)-1)
y = randint(0, len(sides)-1)
z = randint(0, len(dessert)-1)
a = randint(0, len(drinks)-1)


print(meats[x])
print(sides[y])
print(dessert[z])
print(drinks[a])
