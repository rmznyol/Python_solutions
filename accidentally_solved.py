#Contains questions that I came up and solved (potentially by accident)

#   Given an sorted array of integers, write a function that finds the length of the  longest_consecutive_subsequence 
#   (i.e., sequence of integers in which each element is one greater than the previous element).
  
# Input: nums = [0,1,2,3,5,9,11,12,13,14,15,16,20]
# Output: 4
# Explanation: The longest contiguous subsequence in the input array is [11,12,13,14,15,16], and its length is 6.
## Solution: (sliding window technique, very similar to problem where you find the longest substring without repetations)
def longest_consecutive_subsequence(nums: list[int]) -> int:
    i = 0
    longest = 1
    for j in range(1,len(nums)):
        if nums[j-1] + 1 == nums[j]:
            length = j - i + 1
            longest = max(length,longest)
        else:
            i = j
    return longest

# Count the number of anagrams of a string:
from collections import Counter
from math import factorial
def anagram_counter(s):
    s_counter = Counter(s)
    count = factorial(len(s))
    for i in s_counter.values():
        count /= factorial(i)
    return count

anagram_counter('okzojaporykbmq')