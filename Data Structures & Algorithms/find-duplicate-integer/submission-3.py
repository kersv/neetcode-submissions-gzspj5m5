class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # phase 1, move slow 1 and fast 2, stop when they meet
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        # phase 2, return when both values match in the fast and slow pointer
        fast = 0
        while slow != fast:
            print(slow, fast)
            slow = nums[slow]
            fast = nums[fast]

        return slow