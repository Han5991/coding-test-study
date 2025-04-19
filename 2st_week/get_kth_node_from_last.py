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

    def get_kth_node_from_last(self, k):
        slow = self.head
        fast = self.head
        
        # 먼저 fast를 k만큼 앞으로 이동
        for i in range(k - 1):
            fast = fast.next
            # k가 연결 리스트 길이보다 큰 경우 처리
            if fast is None:
                return None
        
        # 두 포인터를 함께 이동
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        
        return slow


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!