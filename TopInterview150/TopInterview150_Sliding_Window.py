# 209. Minimum Size Subarray Sum
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        slow = 0
        sum_until = 0
        longest = 0 
        for fast,num in enumerate(nums):
            sum_until += num
            if sum_until >= target:
                while slow < fast and sum_until - nums[slow] >= target:
                    sum_until -= nums[slow]
                    slow += 1
                longest = min(fast - slow + 1,longest) if longest >0 else fast-slow + 1
        return longest 
                

# 76. Minimum Window Substring
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # keep track of next slow with a que ? 
        # keep a count track to see if it is done
        res = '' #?
        count = 0
        l = len(t)
        t_tracker = {}
        for char in t:
            if char in t_tracker:
                t_tracker[char][0] += 1
            else:
                # counter, queue
                t_tracker[char] = [1, collections.deque()]

        for fast_index,fast in enumerate(s):
            if fast in t_tracker:
                t_tracker[fast][1].append(fast_index)
                if t_tracker[fast][0] == 0:
                    t_tracker[fast][1].popleft()
                if t_tracker[fast][0]:
                    t_tracker[fast][0] -= 1 
                    count += 1
                if count >= l:
                    slow = min(t_tracker.values(),key= lambda x: x[1][0])[1][0]
                    if res:
                        res = s[slow:fast_index+1] if len(res) > (fast_index - slow) else res
                    else:
                        res = s[slow:fast_index+1]
        return res
                    