class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def findLowest(head):
    minVal = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data < minVal:
            minVal = currentNode.data
        currentNode = currentNode.next
    return minVal


node1 = Node(4)
node2 = Node(16)
node3 = Node(3)

node1.next = node2
node2.next = node3
print(findLowest(node1))
