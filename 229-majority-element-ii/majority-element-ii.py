class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = {}

        for num in nums:

            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        result = []
        for num in count:

            if count[num] > len(nums) // 3:
                result.append(num)
        return result
                