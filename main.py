# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 12:02:43 2021

@author: Darius Bowers
"""

import random, time


def algorithmChoice():
    print("----------Algorithm Time Complexities----------\n")
    print("A: Bubble Sort\n")
    print("B: Merge Sort\n")
    print("C: Selection Sort\n")
    print("D: Quick Sort\n")
    print("F: Quit\n")

    choice = input(
        "Please enter choice of algorithm you would like to view the time complexities for or enter <F> to quit: \n")

    return choice


def quickSort(m):
    elements = len(m)

    # Base case
    if elements < 2:
        return m

    current_position = 0  # Position of the partitioning element

    for i in range(1, elements):  # Partitioning loop
        if m[i] <= m[0]:
            current_position += 1
            temp = m[i]
            m[i] = m[current_position]
            m[current_position] = temp

    temp = m[0]
    m[0] = m[current_position]
    m[current_position] = temp  # Brings pivot to it's appropriate position

    left = quickSort(m[0:current_position])  # Sorts the elements to the left of pivot
    right = quickSort(m[current_position + 1:elements])  # sorts the elements to the right of pivot

    m = left + [m[current_position]] + right  # Merging everything together

    return m


def selectionSort(m):  # selection sort algorithm
    for i in range(len(m)):
        minimum = i

        for j in range(i + 1, len(m)):
            # select smallest value
            if m[j] < m[minimum]:
                minimum = j

        # place at front of sorted end of m
        m[minimum], m[i] = m[i], m[minimum]

    return m


def mergeSort(m):  # merge sort algorithm
    if len(m) <= 1:
        return m
    mid = len(m) // 2

    left, right = mergeSort(m[:mid]), mergeSort(m[mid:])

    # merge each side together
    return merge(left, right, m.copy())


def merge(left, right, merged):  # merge sort algorithm

    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):

        # sort each and place into result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


def bubbleSort(m):  # Bubble Sort Algorithm

    for i in range(len(m) - 1):
        for j in range(len(m) - i - 1):
            if m[j] > m[j + 1]:
                m[j], m[j + 1] = \
                    m[j + 1], m[j]
    return m


def bubbleSortWorst(m):  # worst case bubble sort algorithm

    for i in range(len(m) - 1):
        for j in range(len(m) - i - 1):
            if m[j] > m[j + 1]:
                m[j], m[j + 1] = \
                    m[j + 1], m[j]
    return m


def main(k):
    loop = True

    while loop:
        choice = algorithmChoice()
        k = 10
        intk = int(k)

        if choice == "A" or choice == "a":  # average case for bubble sort
            # for loop nums - 10, 100, 1000, 10000
            a = random.sample(range(10), 10)
            st1 = time.perf_counter()
            bubbleSort(a)
            st2 = time.perf_counter()
            print('Selection sort', 10, 'items costs', round((st2 - st1), 5), 'seconds')
            with open("selectionSortTimes.txt", "a") as selection_sort_times:
                selection_sort_times.write(f"{round((st2 - st1), 8)}\n")

            b = random.sample(range(100), 100)
            st3 = time.perf_counter()
            bubbleSort(b)
            st4 = time.perf_counter()
            print('Selection sort', 10000, 'items costs', round((st4 - st3), 5), 'seconds')
            with open("selectionSortTimes.txt", "a") as selection_sort_times:
                selection_sort_times.write(f"{round((st4 - st3), 8)}\n")

            c = random.sample(range(10 * 100), 1000)
            st5 = time.perf_counter()
            bubbleSort(c)
            st6 = time.perf_counter()
            print('Selection sort', 10000, 'items costs', round((st6 - st5), 5), 'seconds')
            with open("selectionSortTimes.txt", "a") as selection_sort_times:
                selection_sort_times.write(f"{round((st6 - st5), 8)}\n")

            d = random.sample(range(100 * 100), 10000)
            st7 = time.perf_counter()
            bubbleSort(d)
            st8 = time.perf_counter()
            print('Selection sort', 10000, 'items costs', round((st8 - st7), 5), 'seconds')
            with open("selectionSortTimes.txt", "a") as selection_sort_times:
                selection_sort_times.write(f"{round((st8 - st7), 8)}\n")


        # for loop nums - 10, 100, 1000, 10000
        #    for x in range(1, 5):
        #       m = random.sample(range(10*intk), intk)
        #      worsBubbleSortedList = bubbleSort(m)
        #     m.sort(reverse=True)
        #    bt3 = time.perf_counter()
        #    worstBubbleSortedList = bubbleSortWorst(m)
        #    bt4 = time.perf_counter()
        #    print('Bubble sort Worst Case', k, 'items costs', round((bt4-bt3), 8), 'seconds')
        #    with open("worstBubbleTimes.txt", "a") as worst_bubble_times:
        #        worst_bubble_times.write(f"{round((bt4-bt3), 8)}\n")

        #   k *= 10

        elif choice == "B" or choice == "b":  # merge sort
            # for loop nums - 10, 100, 1000, 10000
            for x in range(1, 5):
                m = random.sample(range(10 * intk), intk)
                mt1 = time.perf_counter()
                mergeSortedList = mergeSort(m)
                mt2 = time.perf_counter()
                print('Merge sort', k, 'items costs', round((mt2 - mt1), 5), 'seconds.')
                with open("merge_sort_times.txt", "a") as merge_sort_times:
                    merge_sort_times.write(f"{round((mt2 - mt1), 8)}\n")

                k *= 10
                intk = int(k)

        elif choice == "C" or choice == "c":  # selection sort
            # for loop nums - 10, 100, 1000, 10000
            for x in range(1, 5):
                m = random.sample(range(10 * intk), intk)
                start = time.time()
                selectionSort(m)
                end = time.time()
                print('Selection sort', k, 'items costs', round((end - start), 5), 'seconds')
               # with open("selectionSortTimes.txt", "a") as selection_sort_times:
                    #selection_sort_times.write(f"{round((end - start), 8)}\n")
                start = 0
                end = 0
                k *= 10
                intk = int(k)
            a = random.sample(range(10 * 100), 100)
            st3 = time.perf_counter()
            selectionSort(a)
            st4 = time.perf_counter()
            print('Selection sort', 10000, 'items costs', round((st4 - st3), 5), 'seconds')
            with open("selectionSortTimes.txt", "a") as selection_sort_times:
                selection_sort_times.write(f"{round((st4 - st3), 8)}\n")

        elif choice == "D" or choice == "d":  # quick sort
            # for loop nums - 10, 100, 1000, 10000
            for x in range(1, 5):
                m = random.sample(range(10 * intk), intk)
                qt1 = time.perf_counter()
                quickSortedList = quickSort(m)
                qt2 = time.perf_counter()
                print('Quick sort', k, 'items costs', round((qt2 - qt1), 5), 'seconds')
                with open("quickSortTimes.txt", "a") as quick_sort_times:
                    quick_sort_times.write(f"{round((qt2 - qt1), 8)}\n")

                k *= 10
                intk = int(k)


        elif choice == "F" or choice == "f":  # quits program
            print("Exiting now.(sleep(1)).(sleep(1)).(sleep(1))\n")
            loop = False

        else:  # incorrect value entered
            print("Incorrect option entered. Please try again: \n")


if __name__ == "__main__":
    main(1000)

