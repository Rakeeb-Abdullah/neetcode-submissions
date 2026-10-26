class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map={}
        if len(s)==len(t):
            for i in range(len(s)):
                if s[i] in s_map:
                    s_map[s[i]]+=1
                else:
                    s_map[s[i]]=1
                
            for j in range(len(s)):
                if t[j] in s_map:
                    s_map[t[j]]-=1
            for val in s_map.values():
                if val!=0:
                    return False
            return True
        else:
            return False