# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for a in range(i+1, len(arr)):
            if arr[smallest_index] > arr[a]:
                smallest_index = a

        # TO-DO: swap
        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swap_occured = True
    while swap_occured:
        swap_occured = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                a = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = a
                swap_occured = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
