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


def findHighest(head):
    maxVal = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data > maxVal:
            maxVal = currentNode.data
        currentNode = currentNode.next
    return maxVal


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


node1 = Node(1)
node2 = Node(16)
node3 = Node(3)


node1.next = node2
node2.next = node3
node0 = insertNode(node1, 2)
node5 = insertNode(node0, 20)
node5 = insertNode(node5, 70)
node6 = delete_value(node5, node1)

print(transverse(node5))
print(findLowest(node0))
print(findHighest(node5))
