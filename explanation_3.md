# Problem 3: Huffman Coding

I decided to use a dictionary to keep track of the letters that are repeated the most. I then used a
priority queue to keep track of the items in order of occurrence to create a tree. I also used a tree
to keep track of the letters that are repeated the most in the sentence so that I can find the encoding
value for each letter and than to be able to decode the encoded value to its original value.

* Worse find user time case complexity: O(5n) => 0(n^2)
* Space complexity for tree: N/A


## Required Tools
* Python3

## Usage
* clone project
* `cd {folder}` into the repo folder
* `python3 {fine_name}` the file you want to run