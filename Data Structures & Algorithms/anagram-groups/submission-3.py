class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        alphabet=list(map(chr, range(97, 123)))
        def hashify(s):
            hashmap={}
            hash_=[]
            for c in s:
                hashmap[c]=hashmap.get(c,0)+1
        
            for c in alphabet:
                hash_.append(f"{c}{hashmap.get(c,0)}")

            return "".join(hash_)
           

        for s in strs:
            hash_=hashify(s)
            if hash_ not in res:
                res[hash_] = []
            res[hash_].append(s)
        return list(res.values())