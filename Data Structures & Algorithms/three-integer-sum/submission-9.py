class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # return ans
        ans = []
        # sort array
        nums.sort()
        print(nums)
        # fixed pointer
        for i in range(len(nums)-2):
            # check duplicates at start of fixed pointer from prev pointer
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # edge case check if fixed is greater than zero, return ans if true
            elif nums[i] > 0:
                return ans
            # initialize double pointers
            left, right = i+1, len(nums)-1
            while left < right:
                # grab sum of three pointers
                sumThree = nums[i] + nums[left] + nums[right]
                # check if sum is greater than 0, move right pointer left
                if sumThree > 0:
                    right-=1
                # check if sum is less than 0, move left pointer right
                elif sumThree < 0:
                    left+=1
                # if it equals to 0, store value in ans and move left pointer to the right 1
                else:
                    ans.append([nums[i],nums[left],nums[right]])
                    left+=1
                    # check if left pointer is same value as the prev left pointer, keep incrementing left if true
                    while nums[left] == nums[left-1] and left < right:
                        left+=1

        # return ans
        return ans
