from cgi import print_environ
from os import link


class ListNode(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    def traverse(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.value)
            curr_node = curr_node.next
    def get_node(self, value):
        curr_node = self.head
        while curr_node:
            if curr_node.value == value:
                return curr_node
            curr_node = curr_node.next
        return None
    def insert_beginning(self, node):
        node.next = self.head
        self.head = node

    def insert_end(self, node):
        last_node = self.head
        # edge case: if head is None
        if last_node is None:
            self.head = last_node
            return
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = node

    def insert_middle(self, middle_node, new_node):
        if not middle_node:
            print("middle not exist")
            return
        new_node.next = middle_node.next
        middle_node.next = new_node


    def remove_node(self, remove_key):
        prev_node = self.head
        if not prev_node:
            print("cannot remove on an empty linkedlist")
        # handle when the target node is the head
        if prev_node.value == remove_key:
            self.head = prev_node.next
            prev_node = None
            return

        while prev_node.next and prev_node.next.value != remove_key:
            prev_node = prev_node.next
        if prev_node.next is None:
            print("remove key not found")
            return
        next_node = prev_node.next.next
        target_node = prev_node.next
        # remove the target node
        prev_node.next = next_node
        target_node =  None


dummyHead = ListNode(0, None)
curr = dummyHead
# insert items in the LinkedList
for i in range(1, 7):
    NewNode = ListNode(i)
    curr.next = NewNode
    curr = NewNode

linked_list = LinkedList(dummyHead.next)

# traversing the linked List
linked_list.traverse()

# insert a newnode at beginning
print("insert a new node at beginning")
new_node = ListNode(0, None)
linked_list.insert_beginning(new_node)
linked_list.traverse()


# insert a newnode at end
print("insert a new node in the end")
new_node = ListNode(7, None)
linked_list.insert_end(new_node)
linked_list.traverse()

# insert a middle node
print("insert a node in the middle")
new_node = ListNode(6.5, None)
middle_node = linked_list.get_node(6)
linked_list.insert_middle(middle_node, new_node)
linked_list.traverse()

# remove a node
print("remove a node")
linked_list.remove_node(7)
linked_list.traverse()
