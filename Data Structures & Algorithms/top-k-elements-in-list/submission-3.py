class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency={}
        for n in nums:
            frequency[n]=frequency.get(n,0)+1
        buckets=[set() for _ in range(max(frequency.values()))]
        for n in nums:
            buckets[frequency[n]-1].add(n)
        print(buckets)
        ans=[]

        for _ in range(k):
            if len(buckets[-1])>0:
                ans.append(buckets[-1].pop())
            else:
                while len(buckets[-1])==0:
                    buckets.pop()
                ans.append(buckets[-1].pop())


        return ans