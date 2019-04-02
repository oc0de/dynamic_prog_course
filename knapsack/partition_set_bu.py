class PartitionSet(object):
    def can_partition(self, nums):
        sum_nums, n = sum(nums), len(nums)
        if sum_nums % 2: return False
        sum_nums //= 2

        dp = [[None] * (sum_nums+1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        
        
        for c in range(1, sum_nums+1):
            dp[0][c] = True if nums[0] == sum_nums else False
        
        for i in range(1, n):
            for s in range(1, sum_nums+1):
                if dp[i-1][s]:
                    dp[i][s] = dp[i-1][s]
                elif s >= nums[i]:
                    dp[i][s] = dp[i-1][s-nums[i]]
        
        return dp[n-1][sum_nums]

nums1 = [1,2,3,4]
nums2 = [1,1,3,4,7]
nums3 = [2,3,4,7]
ps = PartitionSet()
if (ps.can_partition(nums1) and ps.can_partition(nums2) and not ps.can_partition(nums3)): print("Success bottomUp")

# ps.can_partition(nums1)
        
