class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique=set(nums)
        starts=[]
        for num in unique:
            if num-1 not in unique:
                starts.append(num)
        max_l=0
        for start in starts:
            head=start
            curr_l=1
            while head+1 in unique:
                curr_l+=1
                head+=1
            max_l=max(curr_l,max_l)

        return max_l