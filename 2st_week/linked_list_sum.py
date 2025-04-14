class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def all_sum(self):
        cur = self.head
        sum = ""
        while cur is not None:
            sum += str(cur.data)
            cur = cur.next
        return int(sum)


def get_linked_list_sum(linked_list_1, linked_list_2):
    return linked_list_1.all_sum() + linked_list_2.all_sum()


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

get_linked_list_sum(linked_list_1, linked_list_2)
