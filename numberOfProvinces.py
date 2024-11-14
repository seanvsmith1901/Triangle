class Solution:

    def findCircleNum(self, isConnected) -> int:

        # first we need to reverse all of the edges
        # then run DFS on our reversed graph
        # then find the SCCS from DSF (G and Post)
        # then we can return that array.
        # i migth still have the code

        # so first I need to create a graph, where we are using a representation array
        # and then I just need to return the total number of SCCs
        # somehow I have to filter the SCCs to make sure they only have edges within teh SCC which
        # is uhh going to be fun to say the least
        currentList = []
        forwardGraph = {}
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i != j:
                    if isConnected[i][j] == 1:
                        if i in forwardGraph:
                            forwardGraph[i].append(j)
                        else:
                            forwardGraph[i] = [j]
        # now we have the graph in a representation that makes sense to me
        # now we have to reverse it
        reverseGraph = makeReverseGraph(forwardGraph)
        forwardGraphNodes = makeNodes(forwardGraph)
        backwardGraphnodes = makeNodes(reverseGraph)
        _, postOrder = DFS(backwardGraphnodes, None)

        SCCs, _ = DFS(forwardGraphNodes, postOrder)

        offsetFactor = 0
        totalNodesInScc = 0
        for i in range(len(SCCs)):
            for j in range(len(SCCs[i])):
                totalNodesInScc += 1
        if totalNodesInScc != len(isConnected) and totalNodesInScc < len(isConnected):
            offsetFactor = len(isConnected) - totalNodesInScc



        # so all of this works solid, I just gotta figure out the rest lol.

        # don't forget at the very end, if an node is not in the graph at all, then it is STRONGLY connected to itself lol
        returnValue = len(SCCs) + offsetFactor
        return returnValue


def makeReverseGraph(forwardGraph):
    reversedDict = {}
    for key, values in forwardGraph.items():
        for value in values:
            reversedDict.setdefault(value, []).append(key)
    return reversedDict



def DFS(graph, tieBreakers):
    if tieBreakers == None: # sets the tiebreakers if we don't have any
        tieBreakers = []
        for node in graph:
            tieBreakers.append(node)




    for node in tieBreakers: # resets the fetchers
        node.unvisit()


    totalSccs = []
    postOrderStuff = []
    for node in tieBreakers: # make sure to use the tiebreakers first
        newList = []
        newSCC = DFS2(node, newList, postOrderStuff, tieBreakers)
        if newSCC is not None:
            totalSccs.append(newSCC)

    postOrderStuff.reverse()
    return totalSccs, postOrderStuff

def DFS2(node, newSCC, postOrderStuff, tieBreakers):
    if not node.check():
        node.visit()
        for child in tieBreakers:
            if node.ID == child.ID:
                tieBreakers.remove(child)
                break
        if node.adjacentNodes != None:
            for adjacentNode in node.adjacentNodes:
                if not adjacentNode.check(): # he is an unchecked fetcher
                    adjacentNode.visit()
                    for child in tieBreakers:
                        if adjacentNode.ID == child.ID:
                            tieBreakers.remove(child)
                            break

                    if (adjacentNode.adjacentNodes) != None:
                        for adjacent in adjacentNode.adjacentNodes:
                            DFS2(adjacent, newSCC, postOrderStuff, tieBreakers)
                    adjacentNode.visit()


                    newSCC.append(adjacentNode)
                    postOrderStuff.append(adjacentNode)
        newSCC.append(node)
        postOrderStuff.append(node)
    return newSCC


def makeNodes(graph):
    newGraph = []
    for i in range(len(graph)):
        nodeList = []
        for node in graph[i]:
            nodeList.append(Node(node))
        newNode = Node(i, nodeList)
        newGraph.append(newNode)
    return newGraph

class Node:
    def __init__(self, ID, newNodesList=None, previsit=None, postVisit=None):
        self.ID = ID
        self.visited = False
        self.adjacentNodes = newNodesList
        self.preVisit = previsit
        self.postVisit = postVisit
    def visit(self):
        self.visited = True
    def unvisit(self):
        self.visited = False
    def check(self):
        return self.visited

# find teh SCCS and return those lol

if __name__ == '__main__':
    Solution().findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])
