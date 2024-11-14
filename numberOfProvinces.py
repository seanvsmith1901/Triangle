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

        reverseGraph = makeReverseGraph(forwardGraph) # make the reverse graph

        # first DFS function returns the postORder
        postOrder = DFS(reverseGraph)



        # the way we keep track of which ones we have visited is kinda wierd
        visited = [False] * len(isConnected) # make a new array of visited (where every node corresponds to its spot in the dict
        totalSccs = 0 # just so we know what they are
        for node in postOrder: # make sure we are using hte post order version to sort these things
            if not visited[node]:
                totalSccs += 1 # we have found a new one, now figure out what he is connected to
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
                    for neighbor in graph.get(node, []): # null handling
                        if neighbor not in visited: # if we haven't seen him yet
                            stack.append(neighbor) # throw him on top
                else:
                    stack.pop() # he has been visited we don't need him no more
                    postOrder.append(node) # but we do want to throw him in the post order lsit

    postOrder.reverse()  # reverse the post order to get it from greatest to least
    return postOrder

def DFS2(graph, node, visited):
    stack = [node] # create a stack with just our node on it
    while stack:
        curr = stack.pop() # get the first one off (we want DFS, not BFS)
        if not visited[curr]: # if he has not been visited
            visited[curr] = True # mark him as visited
            for neighbor in graph.get(curr, []): # get all of his freinds
                if not visited[neighbor]: # if they are not in the visited dict yet
                    stack.append(neighbor) # throw them on top

# Test case
if __name__ == '__main__':
    Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
