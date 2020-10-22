class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # find number of connected components in the network
        # number of connections reqd = number of connected components - 1
        # this is a simple graph connected components question
        
        # if the number of connections are less than n-1, then it is not possible to connect all n components. So return false
        
        if len(connections) < n-1:
            return -1
        
        # construct adjList
        adjList = dict()
        
        # add all comps to adjList
        for i in range(n):
            adjList[i] = list()
        
        for u,v in connections:
            adjList[u].append(v)
            adjList[v].append(u)
        
        def dfs(computer, visited, adjList):
            visited.add(computer)
            for child in adjList[computer]:
                if child not in visited:
                    dfs(child, visited, adjList)
                    
        count = 0
        visited = set()
        for computer in adjList:
            if computer not in visited:
                count += 1 # found a disconnected comp
                dfs(computer, visited, adjList)
        
        return count-1
