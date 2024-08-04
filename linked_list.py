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


    print(f"the {link.length()} elemrnets in the linked list are: ")
    link.print_list()

    print(f"the element at index 2 is: {link.get(2)}")


if __name__ == "__main__":
    main()