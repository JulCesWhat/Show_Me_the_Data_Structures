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
        self.real_binary = 0
        self.left_child = None
        self.right_child = None


def transverse_tree(node, dic, binn):
    if node.character is not None:
        dic[node.character].binary_value = binn
        dic[node.character].real_binary = int(binn, base=2)

    if node.left_child is None and node.right_child is None:
        return None

    if node.left_child is not None:
        transverse_tree(node.left_child, dic, binn + "0")

    if node.right_child is not None:
        transverse_tree(node.right_child, dic, binn + "1")

    return None


def huffman_encoding(data):
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
    transverse_tree(tree, letters_dic, "")

    encoded_data = ""
    for letter in data:
        encoded_data += letters_dic[letter].binary_value

    return encoded_data, tree


def huffman_decoding(data, tree):
    tree_head = tree
    decoded_data = ""
    for item in data:
        if item is "0":
            tree_head = tree_head.left_child
            if tree_head.character is not None:
                decoded_data += tree_head.character
                tree_head = tree
        else:
            tree_head = tree_head.right_child
            if tree_head.character is not None:
                decoded_data += tree_head.character
                tree_head = tree

    return decoded_data


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("\nThe size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
