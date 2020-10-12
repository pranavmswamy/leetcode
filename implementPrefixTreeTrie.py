class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.end = False
        self.trie = list()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur_trie = self
        
        # iterate through the word
        for i in range(len(word)):
            # if its children are not initialised, init a 26 size array
            if not cur_trie.trie:
                cur_trie.trie = [None for _ in range(26)]
            
            # if the pos where the char should go is None, means it is being visited for the first time. So only then create a Trie(), because otherwise if you create it everytime it will replace the previous ones.
            if cur_trie.trie[ord(word[i]) - ord('a')] == None:
                cur_trie.trie[ord(word[i]) - ord('a')] = Trie()
            # change cur_trie to the child.
            cur_trie = cur_trie.trie[ord(word[i]) - ord('a')]
        
        # end = True for that position. For this Trie Node, the list will be empty.
        cur_trie.end = True
        # print(cur_trie.end)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur_trie = self
        
        # iterate throught the word
        for i in range(len(word)):
            # if not cur_trie, then that field in the array is none - that prefix never encountered
            # if not cur_trie.trie, then the prefix ends there, and whole word is not present.
            if (not cur_trie) or (not cur_trie.trie):
                return False
            cur_trie = cur_trie.trie[ord(word[i]) - ord('a')]
        
        # reached end, in this node cure_trie.trie may be empty, and .end should be true if word is present.
        return cur_trie.end if cur_trie else False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur_trie = self
        
        for i in range(len(prefix)):
            # if not cur_trie, then that field in the array is none - that prefix never encountered
            # if not cur_trie.trie, then the prefix ends there, and whole word is not present.
            if (not cur_trie) or (not cur_trie.trie):
                return False
            cur_trie = cur_trie.trie[ord(prefix[i]) - ord('a')]
        
        # cur_trie will be None if this node has never been visited before. If some word ended there, then the .end would be True and its children would be an empty list. If some word continued that path, then the children would be a list.
        return True if cur_trie else False
            
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
