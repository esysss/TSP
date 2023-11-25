########################################
#  powered with ❤ by Esysss for Saeed #
########################################

import numpy as np
from Greedy import tsp_greedy
from NearestNeighbor import tsp_neighbor
from ExtendedNeighbor import tsp_Eneighbor

matrix1 = np.array([[np.inf, 11, 3, 9, 15, 27],
                  [20, np.inf, 12, 23, 30, 17],
                  [22,8,np.inf,10,16,19],
                  [5,18,2,np.inf,24,26],
                  [13,7,29,25,np.inf,1],
                   [6,21,4,14,28,np.inf]])

matrix2 = np.array([[np.inf, 6,7,7,7,7],
                   [35,np.inf,12,13,13,13],
                   [35,13,np.inf,18,19,19],
                   [35,13,19,np.inf,24,25],
                   [35,13,19,25,np.inf,30],
                   [216,13,19,25,31,np.inf]])

matrix3 = np.genfromtxt('demofile.txt')
for i in range(len(matrix3)):
    matrix3[i,i] = np.inf

print("This is the Greedy approach")
G = tsp_greedy(matrix3, start=1)
# G.draw()
print("the Route is: ", G.route)
print("the cost is: ", G.cost)

print("This is the Nearest neighbor approach")
G = tsp_neighbor(matrix3, start = 1)
# G.draw()
print("the Route is: ", G.route)
print("the cost is: ", G.cost)

print("This is the Extended nearest neighbor approach")
G = tsp_Eneighbor(matrix3, start = 1)
# G.draw()
print("the Route is: ", G.route)
print("the cost is: ", G.cost)