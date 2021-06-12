# Pathfinding class
class PathFinding:

    # This is the A* algorithm
    def find(self, startNode, endNode, nodes, blockSize):

        # Declare two empty list
        openNodes = []                  # nodes that will be evaluated will be stored in this list
        closedNodes = []                # nodes that were evaluated will be stored in this list
        openNodes.append(startNode)     # Add start node to openList

        # Check if openlist is still not empty
        while len(openNodes) > 0: 

            # Set the current node with the lowest fcost or hcost in the openList
            currentNode = openNodes[0]
            for node in openNodes:
                if node.fCost < currentNode.fCost or node.hCost < currentNode.hCost:
                    currentNode = node

            openNodes.remove(currentNode)       # Remove the current node in the openlist as it has already been evaluated
            closedNodes.append(currentNode)     # Add the current node in the closedList
            
            # If the current node is the end node, then break the loop
            if currentNode.isEnd:
                currentNode.isVisited = False
                break

            # Get the neighbors of the current node
            neighbors = self.getNeighbors(currentNode, nodes, blockSize)

            for neighbor in neighbors:

                # If neighbor is not walkable (wall) or it is in the closedList,
                # then ignore this neighbor using "continue"
                if not neighbor.isTraversable or neighbor in closedNodes:
                    continue

                # Compute the distance between currentNode and neighbor
                # Also, add the existing current node's gcost to get the sum
                neighbor.gCost = currentNode.gCost + self.getDistance(currentNode, neighbor)
                
                # If neighbor is not in the openList, then compute the heuristic costs
                if neighbor.gCost < currentNode.gCost or not neighbor in openNodes:

                    # Compute the distance between neighbor and endNode
                    neighbor.hCost = self.getDistance(neighbor, endNode)

                    # Compute the sum of neighbor's gcost and hcost
                    neighbor.fCost = neighbor.gCost + neighbor.hCost

                    # Set currentNode as neighbor's parent
                    neighbor.parent = currentNode

                    # Add neighbor to openList for evaluation
                    openNodes.append(neighbor)

    # Get neighbors of the given node
    def getNeighbors(self, node, nodes, blockSize):
        neighbors = []
        for y in range(-1, 2):
            for x in range(-1, 2):
                if x == 0 or y == 0:
                    checkX = node.x+(x*blockSize[0])
                    checkY = node.y+(y*blockSize[1])
                    if checkX >= 0 and checkY >= 0 and \
                    round(checkY/blockSize[1]) < len(nodes) and round(checkX/blockSize[0]) < len(nodes[0]):
                        neighbors.append(nodes[round(checkY/blockSize[1])][round(checkX/blockSize[0])])
        return neighbors

    # Get the distance between two given nodes using the given formula
    def getDistance(self, node1, node2):
        return (node1.x-node2.x)**2 + (node1.y-node2.y)**2

    # Retrace the path from linked list
    def retrace(self, endNode):
        path = []
        node = endNode
        while node.parent != None:
            path.append([node.x, node.y])
            node = node.parent
        path.reverse()
        return path