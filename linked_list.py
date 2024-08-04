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
        new_node.next = self.head.next # aggiunge il primo nodo della lista collegata al successivo del nuovo nodo (es: 0 -> 0, 1)
        self.head.next = new_node  # aggiunge il nuovo nodo modificato (0, 1) alla testa della lista collegata


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
        if index >= self.length():
            print("Error: 'Get' index out of range")
            return None
        cur_index = 0
        cur = self.head
        while cur_index < index:
            cur = cur.next
            cur_index += 1
        return cur.data
        

def main():

    # create a linked list
    link = linked_list()
    link.append(1)
    link.append(10)
    link.append(3)
    link.append(4)
    link.append(5)
    link.append_at_beginning(0)

    # print(f"the {link.length()} elemrnets in the linked list are: ")
    # link.print_list()

    print(f"the element at index 2 is: {link.get(2)}")

    link.print_list()


if __name__ == "__main__":
    main()