class Solution:
    # BIDIRECTIONAL BFS SEARCH
    
    # Method to generate children
    def generateMutatedGenes(self, parentGene):
        parentGene = list(parentGene)
        mutatedGenes = list()
        for i in range(len(parentGene)):
            for child in self.children[parentGene[i]]:
                mutatedGene = parentGene[:]
                mutatedGene[i] = child
                mutatedGene_str = "".join(mutatedGene)
                if mutatedGene_str in self.bank_set:
                    mutatedGenes.append(mutatedGene_str)
        
        return mutatedGenes
    
    # Method to do one level of iteration of bfs
    # PASS THE CURRENT QUEUE WHICH IS BEING EXPANDED, AND PASS BOTH VISITED SETS
    # Expand each node at the frontier and return the new frontier.
    # if by chance a node at the frontier is already present in the 'other' bfs's set, then we found the connection. return true
    # else, return false and the next level frontier
    def oneIterationBfs(self, queue, queue_visited, other_visited):
        
        nextLevelQueue = list()
        for gene in queue:
            # IMP - IF YOU CHECK OTHER_VISITED HERE, THEN YOU ARE CHECKING AT THE FRONTIER LEVEL. SO WHEN FOUND, ONLY RETURN COUNT1+COUNT2 SINCE THE EDGE HAS BEEN ALREADY TRAVERSED
            if gene in other_visited:
                return True, list()

            for child in self.generateMutatedGenes(gene):
                # IMP - IF YOU CHECK OTHER VISITED HERE, THEN YOU ARE CHECKING AT THE NEW EXPANDING FRONTIER LEVEL. SO WHEN FOUND, YOU HAVE TO RETURN COUNT1+COUNT2 + 1 SINCE THERE IS THAT ONE FURTHER EXPANDING CONNECTING EDGE.
                if child not in queue_visited:
                    queue_visited.add(child)
                    nextLevelQueue.append(child)

        return False, nextLevelQueue
    
    
    # method to alterate bfs at each step
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        if not bank: return -1
        
        self.bank_set = set(bank)
        
        if end not in self.bank_set:
            return -1
        
        '''
        8 char long strings
        each char can be mutated to a, g, c, t
        so each gene has 24 mutations
        '''
        
        self.children = dict()
        self.children['A'] = ['C', 'G', 'T']
        self.children['C'] = ['A', 'G', 'T']
        self.children['G'] = ['C', 'A', 'T']
        self.children['T'] = ['A', 'G', 'C']
        
        visited_start = set()
        visited_end = set()
        start_count = 0
        end_count = 0
        start_queue = [start]
        end_queue = [end]
        
        # alterate bfs rounds at each step.
        while True:
            start_found, start_queue = self.oneIterationBfs(start_queue, visited_start, visited_end)
            
            if start_found:
                return start_count + end_count
            # At any point, if new frontier is empty, we traversed the entire graph but couldnt find a connection to the other bfs
            elif len(start_queue) == 0:
                return -1
            else:
                start_count += 1
            
            #print(start_count)
            
            end_found, end_queue = self.oneIterationBfs(end_queue, visited_end, visited_start)
            
            if end_found:
                return start_count + end_count
            # At any point, if new frontier is empty, we traversed the entire graph but couldnt find a connection to the other bfs
            elif len(end_queue) == 0:
                return -1
            else:
                end_count += 1
            
            #print(end_count)
        
        return -1
