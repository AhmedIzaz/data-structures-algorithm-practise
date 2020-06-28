def selection_sort(L):
    length = len(L)
    for index1 in range(0, length-1):
        mini_index = index1
        for index2 in range(index1+1, length):
            if L[index2] < L[mini_index]:
                mini_index = index2
        if mini_index != index1:
            L[index1], L[mini_index] = L[mini_index], L[index1]   
        print(L)
if __name__ == "__main__":
    L = []
    numbers = int(input("give the number of list you will give: "))
    for number in range(0, numbers):
        print("give the number for list: ")
        number1 = int(input())
        L.append(number1)

    print(f"the list before selection sorting {L}")
    selection_sort(L)
    print(f"the list after selection sort {L}")