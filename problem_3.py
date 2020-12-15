import sys


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, node):
        self.queue.append(node)

    def is_empty(self):
        return len(self.queue) == 0

    def length(self):
        return len(self.queue)

    def dequeue(self):
        if len(self.queue) < 1:
            return ""

        min = 0
        for i in range(len(self.queue)):
            if self.queue[i].frequency < self.queue[min].frequency:
                min = i
        item = self.queue[min]
        del self.queue[min]
        return item


class Node:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.binary_value = ""
        # self.real_binary = 0
        self.left_child = None
        self.right_child = None


def transverse_tree(node, dic, bin_n):
    if node.character is not None:
        dic[node.character].binary_value = bin_n
        # dic[node.character].real_binary = int(bin_n, base=2)

    if node.left_child is None and node.right_child is None:
        return None

    if node.left_child is not None:
        transverse_tree(node.left_child, dic, bin_n + "0")

    if node.right_child is not None:
        transverse_tree(node.right_child, dic, bin_n + "1")

    return None


def huffman_encoding(data):
    if len(data) < 1:
        return None

    letters_dic = {}

    for letter in data:
        if letter not in letters_dic:
            node = Node(letter, 1)
            letters_dic[letter] = node
        else:
            letters_dic[letter].frequency += 1

    pri_queue = PriorityQueue()

    for key in letters_dic:
        pri_queue.enqueue(letters_dic[key])

    while pri_queue.length() > 1:
        first = pri_queue.dequeue()
        second = pri_queue.dequeue()
        new_node = Node(None, first.frequency + second.frequency)
        if first.frequency > second.frequency:
            new_node.left_child = second
            new_node.right_child = first
        else:
            new_node.left_child = first
            new_node.right_child = second
        pri_queue.enqueue(new_node)

    tree = pri_queue.dequeue()
    if len(letters_dic) < 2:
        new_tree = Node(None, tree.frequency + 1)
        new_tree.left_child = tree
        tree = new_tree
    transverse_tree(tree, letters_dic, "")

    encoded_data = ""
    for letter in data:
        encoded_data += letters_dic[letter].binary_value

    return encoded_data, tree


def huffman_decoding(data, tree):
    if tree is None:
        return ""

    tree_head = tree
    decoded_data = ""
    for item in data:
        if item is "0":
            tree_head = tree_head.left_child
            if tree_head.character is not None:
                decoded_data += tree_head.character
                tree_head = tree
        elif item is "1":
            tree_head = tree_head.right_child
            if tree_head.character is not None:
                decoded_data += tree_head.character
                tree_head = tree
        else:
            decoded_data += tree_head.character

    return decoded_data


if __name__ == "__main__":
    codes = {}

    a_great_sentence_1 = "The bird is the word"

    print("\nThe size of the data is: {}\n".format(sys.getsizeof(a_great_sentence_1)))
    print("The content of the data is: {}\n".format(a_great_sentence_1))

    encoded_data_1, tree_1 = huffman_encoding(a_great_sentence_1)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data_1, base=2))))
    # 0110111011111100111000001010110000100011010011110111111010101011001010
    print("The content of the encoded data is: {}\n".format(encoded_data_1))

    decoded_data_1 = huffman_decoding(encoded_data_1, tree_1)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data_1)))
    print("The content of the encoded data is: {}\n".format(decoded_data_1))
    # The bird is the word

    print("--------------------")

    a_great_sentence_2 = "aabb"

    print("\nThe size of the data is: {}\n".format(sys.getsizeof(a_great_sentence_2)))
    print("The content of the data is: {}\n".format(a_great_sentence_2))

    encoded_data_2, tree_2 = huffman_encoding(a_great_sentence_2)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data_2, base=2))))
    # 0011
    print("The content of the encoded data is: {}\n".format(encoded_data_2))

    decoded_data_2 = huffman_decoding(encoded_data_2, tree_2)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data_2)))
    print("The content of the encoded data is: {}\n".format(decoded_data_2))
    # aabb

    print("--------------------")

    a_great_sentence_3 = "AAAA"

    print("\nThe size of the data is: {}\n".format(sys.getsizeof(a_great_sentence_3)))
    print("The content of the data is: {}\n".format(a_great_sentence_3))

    encoded_data_3, tree_3 = huffman_encoding(a_great_sentence_3)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data_3, base=2))))
    # 0000
    print("The content of the encoded data is: {}\n".format(encoded_data_3))

    decoded_data_3 = huffman_decoding(encoded_data_3, tree_3)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data_3)))
    print("The content of the encoded data is: {}\n".format(decoded_data_3))
    # AAAA