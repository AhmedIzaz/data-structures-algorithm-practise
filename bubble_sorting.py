def sorting_list(L):
    n = len(L)
    fnc_terminated = True

    while (fnc_terminated):
        fnc_terminated = False
        for index in range(0, n-1):
            if L[index] > L[index+1]:
                L[index], L[index+1] = L[index+1], L[index]
                fnc_terminated = True
        if fnc_terminated == False:
            break
        else:
            print(L)
        

if __name__ == "__main__":
    numberList = []
    n = int(input("Enter the list size : "))

    for index in range(0, n):
        print("Enter number at location of", index, ":")
        item = int(input())
        numberList.append(item)

    print("User List is ", numberList)
    print(f"list before bubble sorted {numberList}")
    sorting_list(numberList)
    print(f"list after bubble sorted {numberList}")