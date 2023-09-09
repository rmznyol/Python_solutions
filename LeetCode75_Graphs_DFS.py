#841. Keys and Rooms

from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False for _ in rooms]
        visited[0] = True
        keys = deque([key for key in rooms[0] if not visited[key]])
        while keys:
            current_key = keys.popleft()
            visited[current_key] = True
            for key in rooms[current_key]:
                if not visited[key]:
                    keys.append(key)
        return all(visited)
############################################################
# 547. Number of Provinces

from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        grouped = [False for _ in range(n)]
        province_count = 0
        # finds all the cities in a province starting from a city in the province.
        # marks every city as grouped 
        # def province_finder(i):
        #     province = set()
        #     queue = deque([i])
        #     while queue:
        #         curr = queue.popleft()
        #         province.add(curr)
        #         grouped[curr] = True
        #         for connection in range(n):
        #             if isConnected[curr][connection] and not grouped[connection]:
        #                 queue.append(connection)
            # return province
        # take a city, find all connection ones. Mark all those as 'grouped' 
        # the next not grouped one will be in a new province, thus increase the count by 1
        for i in range(n):
            if not grouped[i]:
                # province_finder(i)
                province_count += 1
                queue = deque([i])
                while queue:
                    curr = queue.popleft()
                    # province.add(curr)
                    grouped[curr] = True
                    for connection in range(n):
                        if isConnected[curr][connection] and not grouped[connection]:
                            queue.append(connection)
        return province_count
############################################################
# 1466. Reorder Routes to Make All Paths Lead to the City Zero

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        connection_dict = collections.defaultdict(list)
        for connection in connections:
            connection_dict[connection[0]].append(connection)
            connection_dict[connection[1]].append(connection)
        
        visited = [False if i != 0 else True for i in range(n)]
        stack = [0]
        count = 0
        while stack:
            print(stack)
            curr = stack.pop()
            for connection in connection_dict[curr]:
                if curr == connection[0] and not visited[connection[1]]:
                    count += 1
                    visited[connection[1]] = True
                    stack.append(connection[1])
                elif curr == connection[1] and not visited[connection[0]]:
                    visited[connection[0]] = True
                    stack.append(connection[0])
        return count
    
############################################################
    
