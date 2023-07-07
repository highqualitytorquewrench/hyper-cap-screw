#First gotta install some packages
#pip install numpy networkx scipy

#Need stuff.  Hurray for import!!!
import numpy as np
import networkx as nx
from scipy.spatial import distance
from scipy.optimize import linear_sum_assignment

#Beginning infinite definitions
def calculate_distance_matrix(coordinates):
    """Calculate the Euclidean distance matrix for a set of 2D coordinates."""
    return distance.cdist(coordinates, coordinates, 'euclidean')

def minimum_spanning_tree(distance_matrix):
    """Find the minimum spanning tree of a complete, weighted and undirected graph."""
    G = nx.from_numpy_array(distance_matrix)
    return nx.minimum_spanning_tree(G)

def find_odd_degree_nodes(MST):
    """Find the nodes with odd degree in the minimum spanning tree."""
    return [v for v, d in MST.degree() if d % 2 == 1]

def minimum_weight_perfect_matching(MST, odd_nodes, distance_matrix):
    """Find the minimum weight perfect matching."""
    G = nx.Graph()
    G.add_nodes_from(odd_nodes)
    for i in range(len(odd_nodes)):
        for j in range(i+1, len(odd_nodes)):
            G.add_edge(odd_nodes[i], odd_nodes[j], weight=distance_matrix[odd_nodes[i], odd_nodes[j]])
    mate = nx.max_weight_matching(G, True)
    return mate

def combine_MST_and_MPM_to_form_Eulerian(MST, MPM):
    """Combine the minimum spanning tree and minimum weight perfect matching to form Eulerian graph."""
    return nx.MultiGraph(list(MST.edges()) + list(MPM))

def eulerian_to_hamiltonian(eulerian_graph):
    """Convert a Eulerian circuit to a Hamiltonian circuit."""
    return list(nx.algorithms.eulerian_circuit(eulerian_graph))

def two_opt_improvement(tour, distance_matrix):
    """Improve the tour using the 2-opt algorithm."""
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 1):
            for j in range(i + 1, len(tour)):
                old_dist = distance_matrix[tour[i - 1]][tour[i]] + distance_matrix[tour[j]][tour[(j+1)%len(tour)]]
                new_dist = distance_matrix[tour[i - 1]][tour[j]] + distance_matrix[tour[i]][tour[(j+1)%len(tour)]]
                if new_dist < old_dist:  # Swap if it reduces the distance
                    tour[i:j+1] = reversed(tour[i:j+1])  # Reverse the segment
                    improved = True
    return tour

def christofides(coordinates):
    """Christofides algorithm."""
    n = len(coordinates)
    distance_matrix = calculate_distance_matrix(coordinates)
    MST = minimum_spanning_tree(distance_matrix)
    odd_nodes = find_odd_degree_nodes(MST)
    MPM = minimum_weight_perfect_matching(MST, odd_nodes, distance_matrix)
    eulerian_graph = combine_MST_and_MPM_to_form_Eulerian(MST, MPM)
    hamiltonian_circuit = eulerian_to_hamiltonian(eulerian_graph)
    tour = [node[0] for node in hamiltonian_circuit] + [hamiltonian_circuit[0][0]]  # Making it a cycle
    improved_tour = two_opt_improvement(tour, distance_matrix) # <--- Here
    return improved_tour

#Now the actual testing of this system

coordinates = np.random.rand(25, 2)
solution = christofides(coordinates)
print(coordinates) #These are the randomly generated coorinates
print(solution) #This is the path *between* the randomly generated coordinates, not the coordinates themselves.  (Defining the edges)

#NOW DOING SUPER COOL THINGS WITH GRAPHING HOPEFULLY
import matplotlib.pyplot as plt #psych you thought we were done importing hehe

def plot_solution(coordinates, solution):
    """Plot the 2D space and the path found by the Christofides algorithm."""
    plt.figure()
    # plot the locations as points
    plt.scatter(coordinates[:, 0], coordinates[:, 1])
    # plot the path
    for i in range(len(solution) - 1):
        start = coordinates[solution[i]]
        end = coordinates[solution[i + 1]]
        plt.plot([start[0], end[0]], [start[1], end[1]], 'r-')
    # close the tour
    start = coordinates[solution[-1]]
    end = coordinates[solution[0]]
    plt.plot([start[0], end[0]], [start[1], end[1]], 'r-')
    plt.show()

# plot the solution
plot_solution(coordinates, solution)