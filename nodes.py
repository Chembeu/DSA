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


def insertatend(head, data):
    new_end = Node(data)
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_end


def insertanypos(pos, data, head):
    np = Node(data)
    temp = head
    for i in range(pos - 1):
        temp = temp.next
    np.data = data
    np.next = temp.next
    temp.next = np


node1 = Node(14)
node2 = Node(7)
node3 = Node(34)

node1.next = node2
node2.next = node3
node0 = insertNode(node1, 17)
node4 = insertatend(node0, 22)
node7 = insertanypos(2, 66, node0)
print(transverse(node0))
