# Problem 3: Huffman Coding

I decided to use a dictionary to keep track of the letters that are repeated the most. I then used a
priority queue to keep track of the items in order of occurrence to create a tree. I also used a tree
to keep track of the letters that are repeated the most in the sentence so that I can find the encoding
value for each letter and than to be able to decode the encoded value to its original value.

* Worse `huffman_encoding` time case complexity: 0(2n + m + j) => 0(n)  Where n is the size of the data string and m is the size of the dictionary and
                                                                            j is the size of the priority queque
* Worse `huffman_decoding` time case complexity: 0(n)                   Where n is the size of the encoded data string
* Worse `huffman_encoding` space case complexity: 0(n + m) => 0(n)      Where n is the size of the dictionary and m the size of the priority queue
* Worse `huffman_decoding` space case complexity: N/A                   Not using an local data structure


## Required Tools
* Python3

## Usage
* clone project
* `cd {folder}` into the repo folder
* `python3 {fine_name}` the file you want to run