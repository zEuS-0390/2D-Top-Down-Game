from math import ceil

class PathFinding:

    def find(self, startNode, endNode, nodes, blockSize):

        startNode = startNode
        openNodes = []
        closedNodes = []
        openNodes.append(startNode)
        while len(openNodes) > 0:
            currentNode = openNodes[0]
            for node in openNodes:
                if node.fCost < currentNode.fCost or node.hCost < currentNode.hCost:
                    currentNode = node
            openNodes.remove(currentNode)
            closedNodes.append(currentNode)
            if currentNode.isEnd:
                currentNode.isVisited = False
                break
            neighbors = self.getNeighbors(currentNode, nodes, blockSize)
            for neighbor in neighbors:
                if not neighbor.isTraversable or neighbor.isStart or neighbor in closedNodes:
                    continue
                neighbor.gCost = currentNode.gCost + self.getDistance(currentNode, neighbor)
                neighbor.hCost = self.getDistance(neighbor, endNode)
                neighbor.fCost = neighbor.gCost + neighbor.hCost
                if neighbor in openNodes:
                    if neighbor.gCost > currentNode.gCost:
                        continue
                neighbor.parent = currentNode
                openNodes.append(neighbor)
                neighbor.isVisited = True

    def getNeighbors(self, node, nodes, blockSize):
        neighbors = []
        for y in range(-1, 2):
            for x in range(-1, 2):
                # if x == 0 or y == 0:
                checkX = node.x+(x*blockSize[0])
                checkY = node.y+(y*blockSize[1])
                if checkX >= 0 and checkY >= 0 and \
                ceil(checkY/blockSize[1]) < len(nodes) and ceil(checkX/blockSize[0]) < len(nodes[0]):
                    neighbors.append(nodes[ceil(checkY/blockSize[1])][ceil(checkX/blockSize[0])])
        return neighbors

    def getDistance(self, node1, node2):
        return (node1.x-node2.x)**2 + (node1.y-node2.y)**2

    def retrace(self, endNode):
        path = []
        node = endNode
        node = node.parent
        try:
            while node.parent != None:
                node.isPath = True
                path.append([node.x, node.y])
                node = node.parent
        except:
            node = endNode
        return path
        
