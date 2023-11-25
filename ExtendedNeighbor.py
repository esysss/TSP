import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


class tsp_Eneighbor:
    def __init__(self,matrix,start = 1):
        self.mat = matrix
        self.original = matrix
        self.start = start - 1
        self.startr = start
        self.final = [start]
        self.route = [[i] for i in range(1, len(matrix)+1)]
        self.cost = 0
        self.greedy()
        self.route_rotate()
        self.cost_compute()

    def draw(self):
        temp = self.original.copy()
        temp[temp == np.inf] = 0
        graph = nx.from_numpy_array(temp, create_using=nx.DiGraph())
        nx.draw_networkx(graph)
        plt.show()

    def greedy(self):

        while len(self.route) > 1:
            j = self.mat[self.start,:].argmin()
            i = self.mat[:,self.start].argmin()
            if self.mat[self.start,j] < self.mat[i, self.start]:
                i = self.start
                self.final = self.final + self.route[j]
            else:
                j = self.start
                self.final = self.route[i] + self.final
            self.start = -1
            self.node_updater(i, j)
            self.matrix_updater(i, j)

    def node_updater(self,i,j):
        nodei = self.route[i]
        nodej = self.route[j]
        self.route.remove(nodei)
        self.route.remove(nodej)
        self.route.append(self.final)

    def matrix_updater(self,i,j):
        new_mat = np.delete(self.mat,(i,j),axis=0)
        new_mat = np.delete(new_mat,(i,j),axis=1)

        mat = np.zeros((new_mat.shape[0]+1,new_mat.shape[0]+1))
        mat[:new_mat.shape[0],:new_mat.shape[1]] = new_mat

        for index,value in enumerate(list(self.route)):
            q = self.route[index][-1]
            p = self.route[-1][0]
            mat[index,-1] = self.original[q-1,p-1]

            q = self.route[-1][-1]
            p = self.route[index][0]
            mat[-1,index] = self.original[q-1,p-1]

        mat[-1,-1] = np.inf
        self.mat = mat

    def route_rotate(self):
        self.route = list(np.roll(self.route[0], -self.route[0].index(self.startr)))
        self.route.append(self.startr)

    def cost_compute(self):
        for i in range(len(self.route)-1):
            self.cost += self.original[self.route[i]-1,self.route[i+1]-1]