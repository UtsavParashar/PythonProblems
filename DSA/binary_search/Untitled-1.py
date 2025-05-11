class MountainArray:
    def __init__(self, nums):
        self.nums = nums
        
    def get(self, index: int) -> int:
        return self.nums[index]
    def length(self) -> int:
        return len(self.nums)

class Solution:
    def find_in_mountain_array(self, target: int, mountain_arr: MountainArray) -> int:
        def binary_search(l, r, asc=True):
            while l <= r:
                m = l + (r-l) //2
                mid_val = mountain_arr.get(m)
                if mid_val == target:
                    return m
                if asc:
                    if mid_val < target:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    if mid_val > target:
                        l = m + 1
                    else:
                        r = m - 1
                
            return -1


        length = mountain_arr.length()
        l, r = 0, length-1 # as the 0th index and last index value can't be peak else it won't be a mountain
        # find peak
        while l < r:
            m = (l+r)//2
            if mountain_arr.get(m) < mountain_arr.get(m+1):
                l = m + 1
            else:
                r = m
        peak = l # left and right both will be pointing to the peak


        # find target in the increasing subarray
        index = binary_search(0, peak, True)
        if index != -1:
            return index

        # find target in the decreasing subarray
        return binary_search(peak, length-1, False)
    
ma = MountainArray([1,2,3,4,5,3,1])
print(Solution().find_in_mountain_array(2, ma))