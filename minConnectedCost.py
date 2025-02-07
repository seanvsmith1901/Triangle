import heapq  # Use a heap to manage the edges more efficiently
class Solution:
    def minCostConnectPoints(self, points) -> int:

        n = len(points) #
        visited = [False] * n  # Keep track of visited points
        min_heap = []  # use heap to grab smallest cost
        total_cost = 0  # Variable to accumulate the total cost
        edges_count = 0  # total edges in tree

        # returns didstance (access points as well)
        def dist(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        # just start from the first point
        visited[0] = True
        for i in range(1, n):
            heapq.heappush(min_heap, (dist(0, i), 0, i))  # get all the edges on

        # here we get to use prims!
        while min_heap and edges_count < n - 1: # leave conditions
            cost, start, end = heapq.heappop(min_heap) # minimum

            if visited[end]:  # edge leads outside of tree
                continue

            # update our MST
            total_cost += cost
            visited[end] = True
            edges_count += 1

            # access the new point and push him onto the heap.
            for i in range(n):
                if not visited[i]:
                    heapq.heappush(min_heap, (dist(end, i), end, i))

        return total_cost
