# Problem 1: LRU Cache

I decided to use a dictionary and a list to solve this problem. The dictionary is used for quick retrieval
and to keep the position of that item in the list. The list is used to know which item should be removed
from the cache if the cache is full.

* Worse `get` time case complexity: O(1)
* Worse `set` time case complexity: O(1)
* Space complexity: 0(n)        when n is the size of the cache defined by the user
    
    
## Required Tools
* Python3

## Usage
* clone project
* `cd {folder}` into the repo folder
* `python3 {fine_name}` the file you want to run