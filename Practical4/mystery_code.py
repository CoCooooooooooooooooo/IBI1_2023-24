# What does this piece of code do?
# Answer:add 1 to progress and a random number from (1,10) each loop and get the total number at the end.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint # import randint function from random module, after which we can draw random number by randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil #import ceil function from math


progress=0
total_random_number=0
while progress<100:
	progress+=1
	n = randint(1,10)
	total_random_number = total_random_number+n

print(total_random_number)
