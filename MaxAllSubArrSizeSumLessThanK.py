# Maximum subarray size, such that all subarrays of that size have sum less than k

'''
Given an array of n positive integers and a positive integer k, 
the task is to find the maximum subarray size such that all subarrays of that size 
have the sum of elements less than or equals to k.

Input: arr[] = {1, 2, 3, 4} and k = 8.
Output : 2

Time Complexity: O(n log n)
Auxiliary Space: O(n)
'''

def maxAllSubArrSizeSumLessThanK(nums,n , k): 
    l=0
    ans=0
    not_possible=False
    for r in range(n):
        sumi += nums[r]

        while sumi > k:
            sumi -= nums[l]
            l+=1
        
            ans=max(ans,r-l+1)
            if (sumi == 0):
                not_possible = True
                break
        
        if (not_possible):
            ans = -1
            break
    return ans


