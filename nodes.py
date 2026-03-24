class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def transverse(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" - > ")
        currentNode = currentNode.next
    print("Null")


def insertNode(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node


node1 = Node(14)
node2 = Node(7)
node3 = Node(34)

node1.next = node2
node2.next = node3
node0 = insertNode(node1, 17)
print(transverse(node0))
