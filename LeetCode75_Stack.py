# 2390. Removing Stars From a String

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char != '*':
                stack.append(char)
            else:
                stack.pop()
        return ''.join(stack)
###############################################################    
# 735. Asteroid Collision

class Solution:
    def gonna_clash(self,left,right):
        if left >= 0 and right <= 0:
            return True
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and self.gonna_clash(stack[-1],asteroid) and stack[-1] < -asteroid:
                stack.pop()
            if stack and self.gonna_clash(stack[-1],asteroid) and stack[-1] >= -asteroid:
                if stack[-1] == -asteroid:
                    stack.pop()
                continue         
            stack.append(asteroid)
        return stack
###############################################################
# 394. Decode String

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                substring = ''
                while stack[-1] != '[':
                    substring = stack.pop() + substring
                stack.pop()
                coefficient = ''
                while len(stack) > 0 and stack[-1].isdigit():
                    coefficient = stack.pop() + coefficient
                stack.append(int(coefficient)*substring)
        return ''.join(stack)