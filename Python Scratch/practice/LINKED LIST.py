class Node:
    data = None
    next = None

newn = Node()
newn.data = "Fridel "
head = newn

newn = Node()
newn.data = "Ian "
newn.next = head
head = newn

newn = Node()
newn.data = "Gamez "
newn.next = head
head = newn

ptr = head
while (ptr != None):
    print(ptr.data)
    ptr = ptr.next