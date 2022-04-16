class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_dll(self):
        if not self.head:
            print('Doubly LinkedList is empty')
        else:
            n = self.head
            while n:
                print(n.data, '-->', end=' ')
                n = n.nref
            print('\n')

    def print_reverse_dll(self):
        if not self.head:
            print('List is empty')
        else:
            n = self.head
            while n.nref:
                n = n.nref
            while n:
                print(n.data, '-->', end=' ')
                n = n.pref

    def add_begin(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            n = self.head
            while n.nref:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def add_after(self, data, x):
        n = self.head
        if n:
            while n:
                if n.data == x:
                    break
                else:
                    n = n.nref
            if n is None:
                print('no data found')
                return
            else:
                new_node = Node(data)
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node

    def add_before(self, data, x):
        n = self.head
        if n:
            while n:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print('Data not found')
                return
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node

    def delete_begin(self):
        if self.head.nref:
            self.head.nref.pref = None
            self.head = self.head.nref
        else:
            print('List is empty has only one element')

    def delete_end(self):
        n = self.head
        if n:
            while n.nref:
                n = n.nref
            n.pref.nref = None
        else:
            print('List is empty')

    def delete_data(self, x):
        n = self.head
        if n:
            while n:
                if n.data == x:
                    break
                else:
                    n = n.nref
            if n is None:
                print('Element not found')
                return
            if n.pref is None:
                n.nref.pref = None
                self.head = n.nref
            elif n.nref is None:
                n.pref.nref = None
            else:
                n.nref.pref = n.pref


dll = DoublyLinkedList()

dll.add_end(20)
dll.add_end(10)
dll.add_after(30, 10)
dll.add_before(40, 20)
# dll.delete_begin()
# dll.delete_end()
dll.delete_data(40)
dll.print_dll()
dll.print_reverse_dll()
