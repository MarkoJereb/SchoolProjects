#!/usr/bin/env python3.8
# Implementation of merge sort as single process, multithreaded process and multiprocess and how they compare to python built-in
# sorted() function.


import math
import multiprocessing
import random
import sys
import threading
import time
import queue


def merge(*args):
    '''
    Support explicit left/right args, as well as a two-item
    tuple which works more cleanly with multiprocessing.
    Merge function of two equal sized lists of integers
    @param: *args
    @return: merged -> list
    '''
    left, right = args[0] if len(args) == 1 else args
    left_length, right_length = len(left), len(right)
    left_index, right_index = 0, 0
    merged = []
    while left_index < left_length and right_index < right_length:
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    if left_index == left_length:
        merged.extend(right[right_index:])
    else:
        merged.extend(left[left_index:])
    return merged




def merge_sort(data):
    '''
    Merge sort algorithm. Recursive implementation.
    @param: data -> list of elements (integers)
    @return: sorted list of same data/elements
    '''
    length = len(data)
    if length <= 1:
        return data
    middle = length // 2 # integer division
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])
    return merge(left, right)


def split_data(data, split):
    '''
    Splits data in {split} segments
    @param: data -> list ; split -> int
    @return: split_data -> list of lists
    '''
    size = int(math.ceil(float(len(data)) / split))
    split_data = [data[i * size:(i + 1) * size] for i in range(split)]

    return split_data



def merge_sort_parallel(data):
    '''
    Creates a pool of 2 worker processes
    We then split the initial data into partitions, sized
    equally per worker, and perform a regular merge sort
    across each partition.
    #processes = multiprocessing.cpu_count()
    @param: list of elements(int)
    @return: sorted list of data
    '''
    processes = 2
    pool = multiprocessing.Pool(processes=processes)    
    data = split_data(data, processes)
    data = pool.map(merge_sort, data)
    # Each partition is now sorted - we now just merge pairs of these
    # together using the worker pool, until the partitions are reduced
    # down to a single sorted result.
    while len(data) > 1:
        # If the number of partitions remaining is odd, we pop off the
        # last one and append it back after one iteration of this loop,
        # since we're only interested in pairs of partitions to merge.
        extra = data.pop() if len(data) % 2 == 1 else None
        data = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]
        data = pool.map(merge, data) + ([extra] if extra else [])
    return data[0]

def merge_sort_threads(data):
    '''
    Multithreaded merge sort with 2 threads. Each thread at the end puts result to a queue,
    which we decue end merge the two lists into single list
    @param: data -> list of integers
    @return sorted list of integers
    '''
    threads = 2
    jobs = list()
    data = split_data(data, threads)
    sorted_data = list()
    que = queue.Queue()

    for i in range(threads):
        thread_data = data[i]
        thread = threading.Thread(target=lambda q, arg1: q.put(merge_sort(arg1)), args=(que, thread_data))
        thread.start()
        jobs.append(thread)

    for t in jobs:
        t.join()

    while not que.empty():
        result = que.get()
        sorted_data.append(result)    

    
    return merge(sorted_data)
        


if __name__ == "__main__":
    for size in [10**3, 10**4, 10**5, 10**6, 10**7]:
        data_unsorted = [random.randint(0, size) for _ in range(size)]
        for sort in merge_sort, merge_sort_threads, merge_sort_parallel, sorted:
            start = time.time()
            data_sorted = sort(data_unsorted)
            deltatime = time.time() - start
            print("For size = {3}, function {0} took {1:.6f} seconds and data is sorted = {2}.".format(sort.__name__,
                                                                                                       deltatime,
                                                                                                       sorted(data_unsorted) == data_sorted,
                                                                                                       size))
            print('-' * 25)
