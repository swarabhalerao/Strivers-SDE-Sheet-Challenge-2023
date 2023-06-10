class Solution:
    def interchange(self, numbers: List[int], x, y) -> List[int]:
        k = numbers[x]
        numbers[x] = numbers[y]
        numbers[y] = k
        return numbers
    
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # bubble sort
        for i in range(len(nums)):
            for j in range(0, len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    self.interchange(nums, j, j+1)
