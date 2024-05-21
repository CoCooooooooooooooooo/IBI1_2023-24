# import necessary libraries
import numpy as np
import matplotlib . pyplot as plt

#define the basic variables of the model
S_array=[]
I_array=[]
R_array=[]
N = 10000  # Total population
S = N - 1  # Susceptible individuals (initially all but one)
I = 1  # Infected individuals (initially one)
R = 0  # Recovered individuals (initially none)
beta=0.3
gamma=0.05

# Time course simulation
time_points = 1000  # Number of times to simulate
for t in range(1, time_points + 1):
    # Calculate the number of new infections
    new_infections = beta * S * I / N
    # Update the variables
    S -= new_infections
    I += new_infections
    # Some infected individuals recover
    I -= gamma * I  
    R += gamma * I 
    # Use append to keep track of the populations over time
    S_array.append(S)
    I_array.append(I)
    R_array.append(R)

S_around_value = np.around(S)
I_around_value = np.around(I)
R_around_value = np.around(R)

# Check the final state of the populations
print(f"Final number of Susceptible: {S_around_value}")
print(f"Final number of Infected: {I_around_value}")
print(f"Final number of Recovered: {R_around_value}")

# Plotting the results
plt.plot(range(1, time_points + 1), S_array, label='Susceptible')
plt.plot(range(1, time_points + 1), I_array, label='Infected')
plt.plot(range(1, time_points + 1), R_array, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('SIR Model')
plt.legend()
plt.show()
# save the picture as a file
plt . figure ( figsize =(6 ,4) , dpi=150)
