# Maximum subarray size, such that sum less than k

'''
Given an array of n positive integers and a positive integer k, 
the task is to find the maximum subarray size such that 
the sum of elements less than or equals to k.

Input: arr[] = {1, 2, 3, 4} and k = 8.
Output : 3

Time Complexity: O(n)
Auxiliary Space: O(1)
'''

def maxSubArrSizeSumLessThanK(nums,n , k): 
    l=0
    ans=0
    for r in range(n):
        sumi += nums[r]

        while sumi > k:
            sumi -= nums[l]
            l+=1
        
        ans=max(ans,r-l+1)
    
    return ans


