class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # initial thought - dag and check for cycle.
        # if cycle present, return false
        
        # Topological Sort algorithm-
        # while nodes in graph:
        #   select node with no incoming edges, add it to top_sort_list
        #   repeat
        #   if no node found with no incoming edges, then cycle is present, so
        #   topological sort not possible, so it is not a DAG. So return false.
        # if all nodes processed, DAG present. return True
        
        # forward (x -> y) adj list
        adjList = dict()
        
        # number of incoming edges array
        incoming_edges = [0]*numCourses
        
        for outgoing, incoming in prerequisites:
            incoming_edges[incoming] += 1
            
            if outgoing in adjList:
                adjList[outgoing].append(incoming)
            else:
                adjList[outgoing] = [incoming]
            
            if incoming not in adjList:
                adjList[incoming] = list()
        
        
        
        start_nodes = list()
        for i in range(len(incoming_edges)):
            if i not in adjList:
                adjList[i] = list()
            if incoming_edges[i] == 0:
                start_nodes.append(i)
        
        # print(adjList)
        # print(start_nodes)
        
        while start_nodes:
            next_start_nodes = list()
            for node in start_nodes:
                for neighbor in adjList[node]:
                    incoming_edges[neighbor] -= 1
                    if incoming_edges[neighbor] == 0:
                        next_start_nodes.append(neighbor)
            start_nodes = next_start_nodes
        
        if sum(incoming_edges) == 0:
            return True
        else:
            return False
