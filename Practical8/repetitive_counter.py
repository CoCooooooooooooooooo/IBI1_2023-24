
import re
# define the sequence
seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
# define the specific sequence
number1=seq.count('GTGTGT')
number2=seq.count('GTCTGT')
# add up to get the total repeate times
repeat=number1+number2
print("The total number of repeat elements are",repeat)


