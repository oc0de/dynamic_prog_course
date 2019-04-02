class PartitionSet(object):
    def can_partition(self, nums):
        sum_nums = sum(nums)
        if sum_nums % 2 != 0: return False
        dp = {}
        return self._divider(dp, nums, sum_nums/2, 0)
    
    def _divider(self, dp, nums, cap, currIdx):
        if cap == 0: return True
        if currIdx >= len(nums): return False
        
        if (currIdx, cap) not in dp:
            if nums[currIdx] <= cap:
                if (self._divider(dp, nums, cap - nums[currIdx], currIdx+1)):
                    dp[(currIdx, cap)] = True
                    return True
        
            dp[(currIdx, cap)] = self._divider(dp, nums, cap, currIdx+1)
        
        return dp[(currIdx, cap)]


nums1 = [1,2,3,4]
nums2 = [1,1,3,4,7]
nums3 = [2,3,4,7]
ps = PartitionSet()
if (ps.can_partition(nums1) and ps.can_partition(nums2) and not ps.can_partition(nums3)): print("Success topDown")


