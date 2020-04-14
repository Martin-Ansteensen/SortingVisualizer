import random
import copy
import time


data_size = 3000
#unsorted_array = random.sample(range(0, data_size), data_size)
unsorted_array = [4, 7, 6, 8, 0, 2, 3, 9, 5, 1]
#print(unsorted_array)

def bubbleSort(arr):
    start_time = time.time()
    for j in range(len(arr)):
        for i in range(len(arr)-1-j):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    print(arr) 
    print("--- %s seconds ---" % (time.time() - start_time))    
            

def insertionSort(arr):
    start_time = time.time()
    for org_pos in range(1, len(arr)):
        curr_pos = org_pos
        org_val = arr[org_pos]
        while org_val > arr[curr_pos-1] and curr_pos > 0:
            arr[curr_pos] = arr[curr_pos-1]
            curr_pos -=1
        arr[curr_pos] = org_val
    print("--- %s seconds ---" % (time.time() - start_time))
    # print(arr)



#bubbleSort(unsorted_array)
#insertionSort(unsorted_array)



