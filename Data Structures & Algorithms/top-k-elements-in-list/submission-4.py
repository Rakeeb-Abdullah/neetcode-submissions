from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        frequency = {}
        for n in nums:
            frequency[n] = frequency.get(n, 0) + 1
            
        # Step 2: Create buckets where the index is the frequency.
        # The maximum possible frequency is len(nums), so we need len(nums) + 1 buckets.
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # Step 3: Group numbers by their frequency
        # Iterating over the dictionary is much faster than iterating over `nums` again
        for num, freq in frequency.items():
            buckets[freq].append(num)
            
        ans = []
        
        # Step 4: Iterate backward from the highest frequency bucket
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                ans.append(num)
                # Return immediately once we have k elements
                if len(ans) == k:
                    return ans
                    
        return ans