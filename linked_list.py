#!/usr/bin/python3

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    
class linked_list:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def append_at_beginning(self, data):
        new_node = Node(data)     # crea un nuovo node (es: 0)
        new_node.next = self.head.next # aggiunge il primo node della lista collegata al successivo del nuovo nodo (es: 0 -> 0, 1)
        self.head.next = new_node  # aggiunge il nuovo node modificato (0, 1) alla testa della lista collegata

    def append_at_index(self, index, data):
        new_node = Node(data)
        cur = self.head

        if index >= self.length():
            print("Error: 'Index' out of range")
            return None
        
        cur_index = 0
        while cur_index < index:
            cur = cur.next
            cur_index += 1
        new_node.next = cur.next
        cur.next = new_node


    def update_at_index(self, index, data):
        new_node = Node(data)
        cur = self.head
        if index >= self.length():
            print("Error: 'Index' out of range")
            return None
        
        cur_index = -1
        while cur_index < index:
            cur = cur.next
            cur_index += 1
        cur.data = new_node.data

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def print_list(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next
            print(cur.data)

    def get(self, index):
        if index > self.length():
            print("Error: 'Get' index out of range")
            return None
        cur_index = -1
        cur = self.head
        while cur_index < index:
            cur = cur.next
            cur_index += 1
        return cur.data

    def remove_at_beginning(self):
        if self.head is None:
            return
        else:
            self.head = self.head.next
        
    def remove_at_end(self):
        cur = self.head
        while cur.next.next != None:
            cur = cur.next
        cur.next = None
    
    def remove_at_index(self, index):
        if index >= self.length():
            print("Error: 'Index' out of range")
            return None
        cur_index = 0
        cur = self.head
        while cur_index < index:
            cur = cur.next
            cur_index += 1
        cur.next = cur.next.next

def main():

    # create a linked list
    link = linked_list()
    link.append(1)
    link.append(10)
    link.append(3)
    link.append(4)
    link.append(5)
    link.append_at_beginning(0)
    link.append_at_index(2, 2)
    link.update_at_index(5, 6)
    link.remove_at_beginning()
    link.remove_at_end()
    link.remove_at_index(2)

    # print(f"the {link.length()} elemrnets in the linked list are: ")
    # link.print_list()

    print(f"the index 3 is: {link.get(3)}")

    print(f"length of the linked list is: {link.length()}")

    link.print_list()



if __name__ == "__main__":
    main()