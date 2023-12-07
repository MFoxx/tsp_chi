from input import read_file
import copy

class AdjacencyList:
    def __init__(self, path):
        self.lines = read_file(path)
        self.node_num = self.lines[-1][1]
        self.graph = {node: set() for node in range(1, self.node_num + 1)}

        self.create_graph()

    def create_graph(self):
        for n1, n2, w in self.lines:
            self.graph[n1].add((n2, w))
            self.graph[n2].add((n1, w))

    def get_graph(self):
        return self.graph
    
    def get_node_val(self, node):
        return self.graph[node]
    
    def get_weight(self, node1, node2):
        minVal = min([node1, node2])
        maxVal = max([node1, node2])
        for node in self.graph[minVal]:
            if node[0] == maxVal:
                return node[1]
        
        return None
    
    def calculate_price(self, path):
        price = 0
        for idx, node in enumerate(path):
            if idx + 1 < len(path):
                price += self.get_weight(node, path[idx + 1])
            else:
                price += self.get_weight(node, path[0])
        
        return price
    

    def print(self):
        for keys,values in self.graph.items():
            print(keys)
            print(values)


class CheapestInsertion:
    def __init__(self, path):
        self.lines = read_file(path)
        self.list = AdjacencyList(path)
        # self.list.print()
        self.strart_node = 1
        self.visited = [1]
        self.path = [1]
        self.sub_path = [[1]]
        self.price = 0
        self.graph = self.list.get_graph()
        self.i = 1
        self.j = None
        self.k = None
        self.solved = False
        
        
    def find_next(self):
        print('-----------------')
        print("Finding next")
        print('-----------------')
        if self.j is None:
            print('J in none')
            minWeight = 0
            currNode = 0
            for node in self.graph[self.strart_node]:
                if node[1] < minWeight or minWeight == 0:
                        minWeight = node[1]
                        currNode = node[0]
                if node[1] == minWeight and node[0] < currNode:
                    minWeight = node[1]
                    currNode = node[0]
            
            print('Found next insertion: ', currNode, ' with weight: ', minWeight)
            return currNode
        else:
            print('J is not none')
            # variable to hold the currect price of the insertion
            currWeight = None
            solutions = []
            # look at every node in the path and its next neighbor
            for idx, i in enumerate(self.path):
                print("New i node: ", i)
                # find the index of the next node in the path
                newInx = idx + 1 if idx + 1 < len(self.path) else 0
                j = self.path[newInx] 
                print('New j node: ', j)
                # get the base weight between the two nodes in graph
                W_ij = self.list.get_weight(i, j)
                print('Base weight: ', W_ij)
                
                # look at the unvisited nodes = k
                for k in self.graph:
                    if k not in self.visited:
                        print('New k node: ', k)
                        # get the weights between the connecting nodes and the unvisited node
                        W_ik = self.list.get_weight(i, k)
                        W_kj = self.list.get_weight(k, j)
                        
                        print('Weight between i and k: ', W_ik)
                        print('Weight between k and j: ', W_kj)
                        print('Calculating ', W_ik, ' + ', W_kj, ' - ', W_ij)
                        # calculate the new weight
                        W = W_ik + W_kj - W_ij
                        print('Weight for K: ', W)
                        if (currWeight is None):
                            print('Found new best K through k None with weight: ', W)
                            currWeight = W
                            solutions.append((k, W, i, j))
                            self.i = i
                            self.j = j
                            self.k = k
                        elif W == currWeight:
                            print('Found same best K through k: ', k, ' with weight: ', W)
                            currWeight = W
                            solutions.append((k, W, i, j))
                            self.i = i
                            self.j = j
                            self.k = k
                        elif W < currWeight:
                            print('Found new best K through k: ', k, ' with weight: ', W)
                            currWeight = W
                            solutions = [(k, W, i, j)]
                            self.i = i
                            self.j = j
                            self.k = k
                            
            sol = min(solutions)
            self.i = sol[2]
            self.j = sol[3]
            self.k = sol[0]
            currWeight = sol[1]
            print('Result of find next is i: ', self.i, ' j: ', self.j, ' k: ', self.k, ' with weight: ', currWeight)
            return self.k

        
    def insert(self, node):
        print('-----------------')
        print('Insertion')
        print('-----------------')
        if (len(self.path) == 1):
            print('Inserting first node: ', node)
            self.path.append(node);
            self.visited.append(node)
            self.sub_path.append(copy.deepcopy(self.path))
            self.j = node
        else:
            print('Inserting every other node')
            print('Inserting node: ', node)
            # insert the node into the path
            # find the index of the node to be inserted
            idx = self.path.index(self.j)

            # if the idx is zero then the node is inserted at the end of the path
            if idx == 0:
                idx = len(self.path)
            
            # insert the node into the path
            self.path.insert(idx, node)
            print('New path: ', self.path)
            # update the visited nodes
            self.visited.append(node)
            print('New visited nodes: ', self.visited)
            # update the sub paths
            self.sub_path.append(copy.deepcopy(self.path))
            print('New sub paths: ', self.sub_path)
            
            # check if graph is solved
            if len(self.graph) == len(self.visited):
                print('Graph is solved')
                self.solved = True
            else:
                print('Graph is not solved')
        
    def solve(self):
        print('Solving cheapest insertion')
        while (not self.solved):
            next = self.find_next()
            self.insert(next)
        
        self.price = self.list.calculate_price(self.path)        
        
    def get_results(self):
        return self.path, self.price, self.sub_path
    
    def record_results(self):
        results = self.get_results()
        
        with open('results.txt', 'w') as f:
            f.write(str(results[1]))
            f.write("\n")
            
            f.write(",".join(map(str, results[0])))
        
    

def find_path(file_path):
    algo = CheapestInsertion(file_path)
    algo.solve()
    
    print('Path: ', algo.get_results()[0])
    print('Total price: ', algo.get_results()[1])
    print('Sub paths: ', algo.get_results()[2])
    
    algo.record_results()

    return algo.get_results()        

if __name__ == "__main__":
    file_path = "data/e15.txt"
    find_path(file_path)
