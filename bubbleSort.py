def bubbleSort(list):
    flag = False # flag to check if there was no change in the curr Iteration & break loop
    for i in range(0,len(list)):
        flag = False
        for j in range(0,len(list)-i-1):
            if list[j]>list[j+1]:
                list[j] += list[j+1]
                list[j+1] = list[j] - list[j+1]
                list[j] -= list[j+1]
                flag = True
        # print("Iter#",i+1)
        # print(list)
        if not flag:
            break
    return list

test_list = [21,4,1,3,9,20,25,6,21,14]
print(bubbleSort(test_list))

test_list = [0,1,2,3,4]
print(bubbleSort(test_list))