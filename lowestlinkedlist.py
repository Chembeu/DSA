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


def transverse(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" ->")
        currentNode = currentNode.next
    print("Null")


def insertNode(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node


def delete_value(head, value):
    if head and head.data == value:
        return head.next

    current = head
    while current.next:
        if current.next.data == value:
            current.next = current.next.next
            return head
        current = current.next

    return head


node1 = Node(4)
node2 = Node(16)
node3 = Node(3)


node1.next = node2
node2.next = node3
node0 = insertNode(node1, 2)
node0 = delete_value(node0, 4)
print(transverse(node0))
print(findLowest(node0))
