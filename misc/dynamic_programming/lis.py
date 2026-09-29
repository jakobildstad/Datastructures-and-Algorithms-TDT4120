"""
Longest Increasing Subsequence

Given an array of integers, find the length of the longest subsequence whose elements 
are in strictly increasing order. A subsequence keeps the original order but may skip 
elements.

For example, in [10, 9, 2, 5, 3, 7, 101, 18], one longest increasing subsequence is 
[2, 3, 7, 18], so the answer is 4.
"""

def longest_increasing_subsequence(arr):
    if not arr:
        return
    
    n = len(arr)
    dp = [0] * n
    dp[0] = 1

    for i in range(1, n):
        candidates = [dp[j] for j in range(0, i) if arr[j] < arr[i]]
        dp[i] = max(candidates) + 1

    return max(dp)
