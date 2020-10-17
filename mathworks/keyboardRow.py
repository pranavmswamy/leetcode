""" ONE MORE APPROACH"""
"""private int[] map = {2,3,3,2,1,2,2,2,1,2,2,2,3,3,1,1,1,1,2,1,1,3,1,3,1,3};

public String[] findWords(String[] words) {

    String[] w = new String[words.length];	// Store filtered words
    int index = 0;							// Where to insert the filtered words
    for (String s: words)					// for each word in words
        if (checkWord(s.toLowerCase()))		// convert it to lowercase and check if all char
            w[index++] = s;					// occurs in the same row, if it does, add it
    return Arrays.copyOfRange(w, 0, index);	// Simply return a copy of the array from 0
}											// index

private boolean checkWord(String word){		// Check if all chars in the word belong in the
    int row = map[word.charAt(0)-'a'];		// same row. Check first chars row
    for (char c: word.toCharArray()){		// For all the chars in the word
        if (map[c-'a'] != row)				// if that char belongs to a different row,
            return false;					// return false
    }
    return true;							// All chars in same row, return true.
}"""


# Another way
'''
for word in words:
    w = set(word.lower())  
    if (w&a==w) | (w&b==w) | (w&c == w): 
       ans.append(word)
return ans'''


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = set('qwertyuiop')
        second_row = set('asdfghjkl')
        third_row = set('zxcvbnm')
        
        ans = list()
        
        # for each word
        for word_unprocessed in words:
            # convert to lowercase
            word = word_up.lower()
            
            # choose set to check depending on first letter
            chosen_set = None
            first_letter = word[0]
            if first_letter in first_row:
                chosen_set = first_row
            elif first_letter in second_row:
                chosen_set = second_row
            else:
                chosen_set = third_row
            
            # keep flag and keep checking if each letter is in chosen set.
            # if it is not, flag = true and break
            # if flag, then dont add to list and continue with next word
            # if not flag, then word is valid. add unprocessed word to ans
            invalid = False
            for letter in word[1:]:
                if letter not in chosen_set:
                    invalid = True
                    break
            
            if invalid:
                continue
            else:
                ans.append(word_up)
        
        return ans
