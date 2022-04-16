class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printll(self):
        if self.head is None:
            print('List is empty')
        else:
            n = self.head
            while n:
                print(n.data, '---->',end=' ')
                n = n.ref

    def add_begin(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node

    def add_end(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            n = self.head
            while n.ref:
                n = n.ref
            n.ref = Node(data)

    def add_befor(self, data, x):
        n = self.head
        new_node = Node(data)
        while n:
            if n.data == x:
                break
            n = n.ref
        if n.ref is None:
            n.ref = new_node
        else:
            new_node.ref = n.ref
            n.ref = new_node

    def add_after(self, data, x):
        n = self.head
        while n:
            if n.ref.data == x:
                break
            n = n.ref
        if n is None:
            print('data not found in list')
        new_node = Node(data)
        new_node.ref = n.ref
        n.ref = new_node
    def delete_begin(self):
        if self.head is None:
            print('list is empty can\'t delete')
            return
        self.head = self.head.ref
    def delete_end(self):
        if self.head is None:
            print('list is empty can\'t delete')
            return
        n = self.head
        while n.ref.ref:
            n = n.ref
        n.ref = None
////.filter(










    
)
    def reverse(self):
        current = self.head
        pre = None
        while current:
            nxt = current.ref
            current.ref = pre
            pre = current
            current = nxt
        self.head = pre

# 1 -> 2 -> -> 7 ->
# 3 -> 4 ->

def sorts(n, m):
    temp = dummy = Node(0)
    if n is None:
        return m
    if m is None:
        return n
    while (n and m):
        if n.data < m.data:
            temp.ref = n
            n = n.ref
        else:
            temp.ref = m
            m = m.ref
        temp = temp.ref
    if n:
        temp.ref = n
    if m:
        temp.ref = m

    # temp = dummy = Node(0)
    # if not n:
    #     return m
    # if not m:
    #     return n
    # while n and m:
    #     if n.data < m.data:
    #         temp.ref = n
    #         n = n.ref
    #     else:
    #         temp.ref = m
    #         m = m.ref
    #     temp = temp.ref
    # if n:
    #     temp.ref = n
    # if m:
    #     temp.ref = m
    # return dummy.ref



l = LinkedList()
l2 = LinkedList()
l.add_end(1)
l.add_end(3)
l.add_end(7)
l2.add_end(3)
l2.add_end(4)
l.printll()
l2.printll()
print('\n')
sorts(l.head, l2.head)
l.printll()
l.reverse()
l.printll()