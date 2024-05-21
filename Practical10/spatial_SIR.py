# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# make array of all susceptible population
population = np.zeros((100, 100))  
#population = np.zeros((100, 100), dtype=int)
check = population[4, 12]  

outbreak = np.random.choice(range(100), 2)  
population[outbreak[0], outbreak[1]] = 1  



beta = 0.3  
gamma = 0.05 


for t in range(100):
    # find infected points
    infectedIndex = np.where(population==1)

    # visualise the population
    current_population = population.copy 

    # loop through all infected points
    for i in range(len(infectedIndex[0])):
        # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        # infect each neighbour with probability beta
        # infect all 8 neighbours (this is a bit finicky, is there a better way?):
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                # don't infect yourself! (Is this strictly necessary?)
                if (xNeighbour,yNeighbour) != (x,y):
                # make sure I don't fall off an edge
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        # only infect neighbours that are not already infected!
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]

    # aplly the recovery
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        if np.random.rand() < gamma:  # recovery rate
            population[x, y] = 2  # the recovery people are set as 2

# visualise the population state
plt.figure(figsize=(6, 4), dpi=150)
# apply different color to distinguish the state of the population
cmap = plt.cm.get_cmap('viridis', 3)  # Gets a color map of length 3 to distinguish the three states
plt.imshow(population, cmap=cmap, interpolation='nearest')  # Use custom color mapping
plt.show()
