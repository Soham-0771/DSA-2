class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k

        def quickselect(left, right):
            if left == right:
                return nums[left]

            pivot = nums[random.randint(left, right)]

            lt = left
            i = left
            gt = right

            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[gt], nums[i] = nums[i], nums[gt]
                    gt -= 1
                else:
                    i += 1

            if target < lt:
                return quickselect(left, lt - 1)
            elif target > gt:
                return quickselect(gt + 1, right)
            else:
                return nums[target]

        return quickselect(0, len(nums) - 1)