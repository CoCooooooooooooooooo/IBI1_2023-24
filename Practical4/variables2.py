X=1==1 # X is true
Y=3>2 # Y is true
W=(X or Y) and not (X and Y) # "and" means both X and Y are true. 
print(W)
#the truth table
#X  Y  W
#T  T  F
#T  F  T
#F  T  T
#F  F  F