class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> prevMap;    // num -> index

        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            if (prevMap.contains(diff)) {
                return {prevMap[diff], i};
            }
            prevMap[nums[i]] = i;
            for(auto& p: prevMap) std::cout << "{" << p.first << ":" << p.second << "} "; std::cout << "\n";

        }
    }
};
