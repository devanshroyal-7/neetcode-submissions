class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            counter[n] = 1 + counter.get(n, 0)
        
        for n, c in counter.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq), 0, -1):
            res += freq[i-1]
            if len(res) == k:
                return res

        return res
            

            