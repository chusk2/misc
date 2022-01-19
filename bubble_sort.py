from random import randint


def bubble_sort(lst):
    lst_copy = lst.copy()
    print(f"List to sort:\t {lst}")

    while True:
        # pass the sorting bubble throughout the whole list until penultimate
        for index in range(0,len(lst)-1):
            # if pair of elements are not ordered
            if lst[index] > lst[index+1]:
                    # previous becomes following
                    lst[index+1] = lst_copy[index]
                    # following becomes current
                    lst[index] = lst_copy[index+1]
            # update list
            lst_copy = lst.copy()
        # generate a list of booleans where True if following >= previous
        all_sorted = [lst[i+1] >= lst[i] for i in range(len(lst)-1)]
        if all(all_sorted):
            break

    return lst

lst = [randint(-10,10) for i in range(9)]
print(f'Sorted list:\t {bubble_sort(lst)}')
        