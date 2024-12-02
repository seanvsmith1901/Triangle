import math

class Solution:
    def minCostConnectPoints(self, points) -> int:
        allEdges = {}
        for edge in points:
            realEdge = tuple(edge)
            allEdges[realEdge] = []

        for edge1 in points:
            for edge2 in points:
                if edge1 != edge2:
                    dist = abs(edge1[0]-edge2[0])+abs(edge1[1]-edge2[1]) # order doesn't matter thanks abs
                    newEdge = dictTuple(dist, edge1, edge2)
                    allEdges[tuple(edge1)].append(newEdge)

            allEdges[tuple(edge1)].sort()


        cost = 0
        tree = [points[0]]
        while len(tree) < len(points): # once the tree conatins all the points
            min_cost = math.inf
            min_edge = None
            for edge in tree:
                for i in (allEdges[tuple(edge)]):
                    if i.cost < min_cost and i.goal not in tree:
                        min_cost = i.cost
                        min_edge = i
            cost += min_edge.cost # updatese the cost

            del allEdges[tuple(min_edge.position)][0] # removes that particualr object, we can't use him again.
            tree.append(min_edge.goal)  # gets the point we have added and adds it to tree



        return cost






class dictTuple:
    def __init__(self, cost, position, goal):
        self.cost = cost
        self.position = position
        self.goal = goal

    def  __lt__(self, other):
        return self.cost < other.cost


if __name__ == '__main__':
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    cost = Solution().minCostConnectPoints(points)
    assert cost == 20