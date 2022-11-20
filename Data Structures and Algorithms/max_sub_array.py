#kadanes algorithm to find the subArray with maximum sum

import math

def maxSubArray(nums) -> int:

        # initializing the variables to minus inf
        curr_sum = 0
        max_sum = -math.inf

        for i in nums:

            #checking whether can we add the prefix sum to the current num 
            curr_sum = max(curr_sum + i, i)

            #max so far -> max sub array sum up to the current element 
            max_sum = max(curr_sum, max_sum)
        return max_sum
    

print(maxSubArray([-2, -3, 4, -1, -2, 1, 5, -3]))