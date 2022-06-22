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
#%%
"""
Heap notes:

- Heaps are widely used tree-like data structures in which the parent nodes satisfy any one of the criteria given below.

    The value of the parent node in each level is less than or equal to its children’s values – min-heap.
    The value of the parent node in each level higher than or equal to its children’s values – max-heap.

- The purpose of a min-heap is to store objects that have a partial order on them. It has a fast (O(log n)) method for removing the minimum object from the heap.
- Same idea for max heap when you want to find max item quickly

- That being said the usefulness of heaps is to get min/max quickly and in python even if we 
    heapify an object it's still just a list so we get min using min(list)

- In other programming languages a heap is an object that contains multiple other data objects,
    typically a key:value object, where we heapify (min/max) the key and use the extract_min/max function
    to obtain the key and then get the value quickly

- Use case of heap is repetitive: You use one when you have to do repeated minimum (or maximum) extractions

"""


#%%

# Heaps and Queues


