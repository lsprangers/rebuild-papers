#%%
import weakref
import numpy as np
import heapq
import random


fibs = [0, 1]
for i in range(2, 100):
    fibs.append(fibs[-1] + fibs[-2])

# %%

print(f"first 10 fibs before shuffle {fibs[:10]} \n\n")
fibs_copy = fibs.copy()

random.shuffle(fibs_copy)
heap_fibs = fibs_copy.copy()

print(f"first 10 fibs after shuffle {fibs_copy[:10]} \n\n")

heapq.heapify(heap_fibs)

print(f"first 25 fibs after heapq::heapify {heap_fibs[:25]} \n\n")

print(f"type of fibs, fibs shuffled, and heaped fibs: {type(fibs)}, {type(fibs_copy)}, {type(heap_fibs)},")

"""
heapq notes specifically:
implementation of heap queue algorithm (priority queue algorithm) in which the property of min-heap is preserved. The module takes up a list of items and rearranges it such that they satisfy the following criteria of min-heap:
    The parent node in index ‘i’ is less than or equal to its children (VALUE AT 0 IS MIN)
    Parent of node 'i' is in index 'i//2'
    The left child of a node in index ‘i’ is in index ‘(2*i) + 1’.
    The right child of a node in index ‘i’ is in index ‘(2*i) + 2’.
"""


#%%
"""
Heap notes:

- Heaps are widely used tree-like data structures in which the parent nodes satisfy any one of the criteria given below.

    The value of the parent node in each level is less than or equal to its children’s values – min-heap.
    The value of the parent node in each level higher than or equal to its children’s values – max-heap.

- The value at root of min heap is minimum of all values, and for each tree below it the same
    idea is true...therefore a value like 23 coudl be placed where it is below
    and the min-heap is still valid
       9
     /   \ 
   13     22
  / \     / \
 19  23  25 29

- The purpose of a min-heap is to store objects that have a partial order on them. It has a fast (O(log n)) method for removing the minimum object from the heap.
- Same idea for max heap when you want to find max item quickly

- That being said the usefulness of heaps is to get min/max quickly and in python even if we 
    heapify an object it's still just a list so we get min using min(list)

- In other programming languages a heap is an object that contains multiple other data objects,
    typically a key:value object, where we heapify (min/max) the key and use the extract_min/max function
    to obtain the key and then get the value quickly

- Use case of heap is repetitive: You use one when you have to do repeated minimum (or maximum) extractions

- If we extract the min/max then you replace it with one of the leaves at random
    and then run the shift down operation until it's a valid heap again
    - For min the swap down swaps it with the smaller child, and for max it's the larger

        We take out 9 as the min and put 25 randomly there and then shift_down() 
       9         -->        25       -->        13                 
     /   \       -->      /   \      -->       /   \                
   13     22     -->    13     22    -->     25     22              
  / \     / \    -->   / \      \    -->    / \      \                     
 19  23  25 29   -->  19  23     29  -->   19  23     29                        
"""

#%%

# Heaps to Queues

"""
- Heaps can turn into priority queueus fairly easily 

- Priority queues are abstract data types and are a special form of queues

- Heap to queue we just start at root, take left and then right, and then recursively
    do the same for all the trees below starting with left tree then right

       9      
     /   \    
   13     22  
  / \     / \ 
 19  23  25 29

Turns into [9, 13, 22, 19, 23, 25, 29]
"""
heap_to_priority_from_example = [
    (9, 'X'), 
    (13, 'X'), 
    (22, 'X'), 
    (19, 'X'), 
    (23, 'X'), 
    (25, 'X'), 
    (29, 'X')
]


random.shuffle(heap_to_priority_from_example)
print(heap_to_priority_from_example)

heapq.heapify(heap_to_priority_from_example)    # Doesn't produce exact same result as above
print(heap_to_priority_from_example)


