from itertools import count


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

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        cur_index = 0
        while cur_index != index:
            cur = cur.next
            cur_index += 1
        return cur

    def add_node(self, index, value):
        if index == 0:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            return

        prev = self.get_node(index - 1)
        new_node = Node(value)
        new_node.next = prev.next
        prev.next = new_node
        return

    def delete_node(self, index):
        if index == 0:
            if self.head is None:
                raise IndexError("Index out of range")
            self.head = self.head.next
            return

        prev_node = self.get_node(index - 1)
        if prev_node is None or prev_node.next is None:
            raise IndexError("Index out of range")

        # 삭제할 노드를 저장
        node_to_delete = prev_node.next

        # prev_node의 next를 삭제할 노드의 next로 변경
        prev_node.next = node_to_delete.next

    def replace_node(self, index, value):
        if index == 0:
            # 인덱스가 0인 경우 첫 번째 노드를 교체
            new_node = Node(value)
            if self.head is not None:
                new_node.next = self.head.next
            self.head = new_node
            return

        prev_node = self.get_node(index - 1)
        cur_node = Node(value)

        if prev_node.next is None:
            # 인덱스가 범위를 벗어난 경우
            raise IndexError("Index out of range")

        next_node = prev_node.next.next  # 기존 노드의 다음 노드
        prev_node.next = cur_node
        cur_node.next = next_node

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def not_none_size(self):
        count = 0
        current = self.head
        while current:
            if current.data is not None:
                count += 1
            current = current.next
        return count


# linked_list = LinkedList(5)
# linked_list.append(12)
# linked_list.add_node(0, 3)
# linked_list.delete_node(1)
# linked_list.replace_node(0, None)
# linked_list.print_all()

def josephus_problem(n, k):
    if n == 0:
        return []
    people_list = [i for i in range(n)]
    remove_list = []
    index = 0
    # 모든 사람이 제거될 때까지 반복
    while people_list:
        # k번째 사람의 위치 계산 (원형이므로 나머지 연산 사용)
        index = (index + k - 1) % len(people_list)

        # k번째 사람 제거하고 제거 리스트에 추가
        removed_person = people_list.pop(index)
        remove_list.append(removed_person + 1)

    print("<", ", ".join(map(str, remove_list)), ">", sep='')


n, k = map(int, input().split())
josephus_problem(n, k)
