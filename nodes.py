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


node1 = Node(14)
node2 = Node(7)
node3 = Node(34)

node1.next = node2
node2.next = node3
node0 = insertNode(node1, 17)
node4 = insertatend(node0, 22)
print(transverse(node0))
