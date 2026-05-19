class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_hash = dict()
        output = []
        for i in range(len(strs)):
            word = strs[i]
            key = "".join(sorted(word))
            if key not in ana_hash:
                ana_hash[key] = len(ana_hash)
                output.append([word])
            else:
                output[ana_hash[key]].append(word)
                

        return output