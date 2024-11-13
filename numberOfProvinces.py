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

        forwardGraph = {}
        for i in range(len(isConnected)):
            if isConnected[i][2] == 0:
                forwardGraph[i] = isConnected[i][1]

        pass


# find teh SCCS and return those lol

if __name__ == '__main__':
    Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
