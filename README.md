# a python implimentation of huristic TSP problem
Three approaches are used here to solve TSP problem in python
1- Nearest Neighbor Heuristic for the ATSP/STSP
2- Extended Nearest Neighbor Heuristic for the ATSP/STSP
3- Greedy Heuristic for the ATSP

#Definition
Let G = (V; E) be a complete, weighted, directed graph with jVj = n,
and let c : E ! R be the cost function of G.
(a) The Asymmetric Traveling Salesman Problem (ATSP) is the
problem of finding a Hamiltonian cycle (v1; v2; : : : ; vn; v1) with
minimum cost c(vn; v1) + Pn i=−11 c(vi; vi+1).
(b) The Symmetric Traveling Salesman Problem (STSP) is the ATSP
for the special case, that for all edges it holds that the cost of the
edge and its opposite edge is equal, i.e., the graph can be
assumed to be undirected.
