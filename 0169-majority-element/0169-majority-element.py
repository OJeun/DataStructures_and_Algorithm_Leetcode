class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 0

        for num in nums:
            if candidate == num:
                count += 1

            else:
                count -= 1
                if count == 0:
                    candidate = num
                    count += 1

        return candidate