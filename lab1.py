# def aStarAlgo(start_node, stop_node):
    

#     open_set = set(start_node) # {A}, len{open_set}=1
#     closed_set = set()
#     g = {} # store the distance from starting node
#     parents = {}
#     g[start_node] = 0
#     parents[start_node] = start_node # parents['A']='A"

#     while len(open_set) > 0 :
#         n = None

#         for v in open_set: # v='B'/'F'
#             if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
#                 n = v # n='A'

#         if n == stop_node or Graph_nodes[n] == None:
#             pass
#         else:
#             for (m, weight) in get_neighbors(n):
#              # nodes 'm' not in first and last set are added to first
#              # n is set its parent
#                 if m not in open_set and m not in closed_set:
#                     open_set.add(m)      # m=B weight=6 {'F','B','A'} len{open_set}=2
#                     parents[m] = n       # parents={'A':A,'B':A} len{parent}=2
#                     g[m] = g[n] + weight # g={'A':0,'B':6, 'F':3} len{g}=2


#             #for each node m,compare its distance from start i.e g(m) to the
#             #from start through n node
#                 else:
#                     if g[m] > g[n] + weight:
#                     #update g(m)
#                         g[m] = g[n] + weight
#                     #change parent of m to n
#                         parents[m] = n

#                     #if m in closed set,remove and add to open
#                         if m in closed_set:
#                             closed_set.remove(m)
#                             open_set.add(m)

#         if n == None:
#             print('Path does not exist!')
#             return None

#         # if the current node is the stop_node
#         # then we begin reconstructin the path from it to the start_node
#         if n == stop_node:
#             path = []

#             while parents[n] != n:
#                 path.append(n)
#                 n = parents[n]

#             path.append(start_node)

#             path.reverse()

#             print('Path found: {}'.format(path))
#             return path


#         # remove n from the open_list, and add it to closed_list
#         # because all of his neighbors were inspected
#         open_set.remove(n)# {'F','B'} len=2
#         closed_set.add(n) #{A} len=1

#     print('Path does not exist!')
#     return None

# #define fuction to return neighbor and its distance
# #from the passed node
# def get_neighbors(v):
#     if v in Graph_nodes:
#         return Graph_nodes[v]
#     else:
#         return None
# #for simplicity we ll consider heuristic distances given
# #and this function returns heuristic distance for all nodes
 
# def heuristic(n):
#     H_dist = {
#         'A': 11,
#         'B': 6,
#         'C': 99,
#         'D': 1,
#         'E': 7,

#         'G': 0,

#     }

#     return H_dist[n]

# #Describe your graph here
# Graph_nodes = {
#     'A': [('B', 2), ('E', 3)],
#     'B': [('C', 1), ('G', 9)],
#     'C': [],
#     'D': [('G', 1)],
#     'E': [('D', 6)]
# }
# aStarAlgo('A', 'G')




class Graph:
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis

    def get_neighbours(self, v):
        return self.adjac_lis[v]

    def h(self, n):
        H = {'A': 1, 'B': 1, 'C': 1, 'D': 1}
        return H[n]

    def a_star_algorithm(self, start, stop):
        open_lst = set([start])
        closed_lst = set()
        dist = {start: 0}
        prenode = {start: start}

        while open_lst:
            n = min(open_lst, key=lambda x: dist[x] + self.h(x))

            if n == stop:
                reconst_path = []
                while prenode[n] != n:
                    reconst_path.append(n)
                    n = prenode[n]
                reconst_path.append(start)
                reconst_path.reverse()
                print("Path found:", reconst_path)
                return reconst_path

            open_lst.remove(n)
            closed_lst.add(n)

            for m, weight in self.get_neighbours(n):
                if m in closed_lst:
                    continue
                if m not in open_lst or dist[n] + weight < dist[m]:
                    open_lst.add(m)
                    prenode[m] = n
                    dist[m] = dist[n] + weight

        print("Path does not exist")
        return None


adjac_lis = {'A': [('B', 1), ('C', 3), ('D', 7)], 'B': [('D', 5)], 'C': [('D', 12)]}
graph1 = Graph(adjac_lis)
graph1.a_star_algorithm('A', 'D')