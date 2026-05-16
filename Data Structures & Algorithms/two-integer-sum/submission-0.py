class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        des_pair = dict()

        for i in range(len(nums)):
            if nums[i] not in des_pair:
                des_pair[target - nums[i]] = i      # dict(des_target:index of the first number)
            else:
                return [des_pair[nums[i]], i]
