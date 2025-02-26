from math import inf

class Solution:
    def minimumTotal(self, triangle) -> int:
        num_rows = len(triangle)
        max_cols = len(triangle[num_rows-1])

        cost_array = [[Point(i,j) for j in range(i+1)] for i in range(num_rows)]
        # now we need to set baseCases
        cost_array[0][0] = Point(0, 0, triangle[0][0], None)
        for i in range(num_rows-1):
            cost_array[i+1][0].cost = triangle[i+1][0] + cost_array[i][0].return_cost()

        while cost_array[num_rows-1][max_cols-1].cost == inf:
            for i in range(1, num_rows):
                for j in range(1, i+1):
                    cell_cost = triangle[i][j]
                    # cost1 is coming down, cost2 is coming left

                    if j != i:
                        cost1 = cell_cost + cost_array[i-1][j].cost
                    else:
                        cost1 = inf

                    cost2 = cell_cost + cost_array[i-1][j-1].cost

                    if cost2 < cost1:
                        prev = cost_array[i][j-1]
                        cost =  cost2
                    else:
                        prev = cost_array[i-1][j]
                        cost = cost1

                    cost_array[i][j] = Point(i, j, cost, prev)

        min = inf
        minPoint = Point(0,0,inf,None)
        for element in cost_array[num_rows-1]:
            if element.cost < min:
                min = element.cost

        return min

class Point:
    def __init__(self, i=0, j=0, cost=inf, previous=None):
        self.i = i
        self.j = j
        self.cost = cost

if __name__ == "__main__":
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    Solution().minimumTotal(triangle)