class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        
        for i in range(len(nums)):
            # 1. Skip duplicate values for 'i' to prevent duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            target = 0 - nums[i]
            j = i + 1
            k = len(nums) - 1
            
            while k > j:
                curr = nums[k] + nums[j]

                if target > curr:
                    j += 1
                elif target < curr:
                    k -= 1
                else:
                    # 2. Append the current valid triplet FIRST
                    ans.append([nums[i], nums[j], nums[k]])
                    
                    # THEN move the pointers
                    j += 1
                    k -= 1
                    
                    # 3. Skip duplicate values for 'j' and 'k'
                    while k > j and nums[j] == nums[j - 1]:
                        j += 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
                        
        return ans