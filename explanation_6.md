# Problem 6: Union and Intersection

I am using a dictionary to find the union of two linked lists so that I don't have duplicate values in the
result. I am using two dictionaries to find the intersection of two linked lists because it will allow me
to find the items that are in both linked list pretty quickly.

* Worse `union` time case complexity: O(n + m + j) => 0(n)  where n and m are the size of the two linked lists
                                                                passed to the functions and j is the new
                                                                dictionary size
* Worse `intersection` time case complexity: O(n + m)       where n and m are the size of the linked list passed
                                                                to the intersection function
* Space `union` complexity: 0(n + m) => 0(n)                where n is  the dictionary and m the new linked
                                                                list size
* Space `intersection` complexity: 0(n + m + j) => 0(n)     where n is the fist dictionary and m is
                                                                the second dictionary and j is the new linked
                                                                list
                                                


## Required Tools
* Python3

## Usage
* clone project
* `cd {folder}` into the repo folder
* `python3 {fine_name}` the file you want to run