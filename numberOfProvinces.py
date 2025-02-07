class Solution:
    def findCircleNum(self, isConnected) -> int:
        # build the graph
        forwardGraph = {}
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    if i not in forwardGraph:
                        forwardGraph[i] = [j]
                    else:
                        forwardGraph[i].append(j)

        reverseGraph = makeReverseGraph(forwardGraph)

        # first DFS function returns the postORder
        postOrder = DFS(reverseGraph)


        visited = [False] * len(isConnected)
        totalSccs = 0 #
        for node in postOrder:
            if not visited[node]:
                totalSccs += 1
                DFS2(forwardGraph, node, visited)

        return totalSccs

def makeReverseGraph(forwardGraph):
    reversedDict = {}
    for key, values in forwardGraph.items():
        for value in values:
            reversedDict.setdefault(value, []).append(key)
    return reversedDict

def DFS(graph):
    # Standard iterative DFS for post-order traversal
    visited = set()
    postOrder = []
    stack = []

    # Initialize the stack with all nodes
    for node in graph:
        if node not in visited:
            stack.append(node)
            while stack:
                node = stack[-1]
                if node not in visited:
                    visited.add(node)
                    for neighbor in graph.get(node, []):
                        if neighbor not in visited:
                            stack.append(neighbor)
                else:
                    stack.pop()
                    postOrder.append(node)

    postOrder.reverse()  # reverse the post order
    return postOrder

def DFS2(graph, node, visited):
    stack = [node] # create a stack with just our node on it
    while stack:
        curr = stack.pop() # get the first one off
        if not visited[curr]: # if he has not been visited
            visited[curr] = True # mark him as visited
            for neighbor in graph.get(curr, []):
                if not visited[neighbor]:
                    stack.append(neighbor) # throw them on top

# Test case
if __name__ == '__main__':
    Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
