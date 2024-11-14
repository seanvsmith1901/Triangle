from audioop import reverse


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
                            currentList = forwardGraph[i]
                            currentList.append(j)
                            forwardGraph[i] = currentList
                        else:
                            forwardGraph[i] = [j]
        # now we have the graph in a representation that makes sense to me
        # now we have to reverse it

        reverseGraph = makeReverseGraph(forwardGraph)






        # don't forget at the very end, if an node is not in the graph at all, then it is STRONGLY connected to itself lol


def makeReverseGraph(forwardGraph):
    reversedDict = {}
    for key, values in forwardGraph.items():
        for value in values:
            reversedDict.setdefault(value, []).append(key)
    return reversedDict


# find teh SCCS and return those lol

if __name__ == '__main__':
    Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
