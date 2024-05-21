import numpy as np
import matplotlib.pyplot as plt

# define the variables
N = 10000  # population
I0 = 1  # initial inffected people
R0 = 0  # initial recovery people
vaccinated_rates = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6 ,0.7, 0.8, 0.9]  # different vaccination rate

# use plt to draw a figure
plt.figure(figsize=(10, 6))  

# times loop
for vaccinated_rate in vaccinated_rates:
    V = int(vaccinated_rate * N)  # the number of vaccined people
    S0 = N - I0 - R0 - V  # susceptible people

    # Create a variable array
    S = [S0]
    I = [I0]
    R = [R0]
    # define the parametre
    beta = 0.3  
    gamma = 0.05 

    # time loop
    for _ in range(1000):
        # calculate the infected 
        i = beta * I[-1] / N

        # define the recovery rate
        r = gamma

        # chose infeted people and recovery people randomly
        infected_choose = np.random.choice([0, 1], size=S[-1], p=[1 - i, i])
        infected_new = np.sum(infected_choose)

        recovered_choose = np.random.choice([0, 1], size=I[-1], p=[1 - r, r])
        recovered_new = np.sum(recovered_choose)

        # Track the number of susceptible persons, infected persons and recovered persons
        S.append(S[-1] - infected_new)
        I.append(I[-1] + infected_new - recovered_new)
        R.append(R[-1] + recovered_new)

    # draw the graph
    plt.plot(I, label=f"({vaccinated_rate*100}%)")

# show figure name and labels
plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model of different vaccination rate")
plt.legend()
plt.show()