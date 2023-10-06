class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = [[n, i] for i, n in enumerate(nums)]
        answer.sort()
        l, r = 0, len(answer)-1

        while l <= r:
            sum = answer[l][0] + answer[r][0]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [answer[l][1], answer[r][1]]