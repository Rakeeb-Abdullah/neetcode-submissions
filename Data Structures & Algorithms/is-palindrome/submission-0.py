class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_=[c.lower() for c in s if c.isalnum()]
        print(s_)
        for i in range(len(s_)//2):
            if s_[i]!=s_[len(s_)-1-i]:
                return False
        
        return True