import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        
        for s in strs:
            # Create an array of 26 zeros
            count = [0] * 26 
            
            # Map each character to its alphabetical index (a=0, b=1, etc.)
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            # Tuples are hashable and can be used as dict keys
            res[tuple(count)].append(s)
            
        return list(res.values())