def insertion_sort(L):
    length = len(L)

    for index in range(1, length):
        item = L[index]
        j = index-1

        while j>=0 and L[j] > item:
            L[j+1] = L[j]
            j = j - 1
            L[j+1] = item
        print(L)

if __name__ == "__main__":
    L = [6, 1, 4, 9, 2]
    print(f"the list before sorting {L}")
    insertion_sort(L)
    print(f"the list after sorting {L}")