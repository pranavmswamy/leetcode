class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = dict()
        
        for word in strs:
            alps = [0]*27
            for letter in word:
                alps[ord(letter)-96] += 1
            s_w = tuple(alps)
            if s_w in anagram:
                anagram[s_w].append(word)
            else:
                anagram[s_w] = [word]
        
        #print(anagram)
        return list(anagram.values())
