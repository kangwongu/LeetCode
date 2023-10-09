class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        n = len(nums)

        for i in range(n):
            to_find = target - nums[i]
            if to_find in num_dict:
                return [num_dict[to_find], i]
            num_dict[nums[i]] = i