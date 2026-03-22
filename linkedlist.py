class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def transverse(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" ->")
        currentNode = currentNode.next
    print("null")


node1 = Node(7)
node2 = Node(6)
node3 = Node(9)

node1.next = node2
node2.next = node3

transverse(node2)
