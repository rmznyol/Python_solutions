# 933. Number of Recent Calls

from collections import deque
class RecentCounter:

    def __init__(self):
        self.queue = deque()
    def ping(self, t: int) -> int:
        self.queue.append(t)
        while len(self.queue) > 0 and self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)
#################################################
# 649. Dota2 Senate

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r, d = collections.deque(), collections.deque()
        for seat, member in enumerate(senate):
            match member:
                case 'D': d.append(seat)
                case 'R': r.append(seat)
        last_vote = len(senate)
        while r and d:
            rad = r.popleft()
            dr = d.popleft()
            if rad > dr:
                d.append(last_vote + dr)
            else:
                r.append(last_vote + rad)
        return "Radiant" if r else 'Dire'