class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(l_list_1, l_list_2):
    # Your Solution Here
    dic = {}
    head_1 = l_list_1.head
    while head_1 is not None:
        dic[head_1.value] = 1
        head_1 = head_1.next

    head_2 = l_list_2.head
    while head_2 is not None:
        dic[head_2.value] = 1
        head_2 = head_2.next

    linked_list = LinkedList()
    for key in dic:
        linked_list.append(key)

    return linked_list


def intersection(l_list_1, l_list_2):
    # Your Solution Here
    dic = {}
    dic_2 = {}
    head_1 = l_list_1.head
    while head_1 is not None:
        dic[head_1.value] = 1
        head_1 = head_1.next

    linked_list = LinkedList()
    head_2 = l_list_2.head
    while head_2 is not None:
        if head_2.value in dic and head_2.value not in dic_2:
            dic_2[head_2.value] = 1
            linked_list.append(head_2.value)
        head_2 = head_2.next

    return linked_list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->

print(intersection(linked_list_1, linked_list_2))
# 6 -> 4 -> 21 ->

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_3 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_4 = [1, 7, 8, 9, 11, 21, 1]

for i in element_3:
    linked_list_3.append(i)

for i in element_4:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->

print(intersection(linked_list_3, linked_list_4))
#

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_5 = [0]
element_6 = [0]

for i in element_5:
    linked_list_5.append(i)

for i in element_6:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))
# 0 ->

print(intersection(linked_list_5, linked_list_6))
# 0 ->
