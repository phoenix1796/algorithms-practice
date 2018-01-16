def merge(l1,l2):
    ind1 = ind2 = 0
    list = []
    while ind1<len(l1) and ind2<len(l2):
        if l1[ind1]<l2[ind2]:
            list.append(l1[ind1])
            ind1+=1
        else:
            list.append(l2[ind2])
            ind2+=1
    while ind1<len(l1):
        list.append(l1[ind1])
        ind1+=1
    while ind2<len(l2):
        list.append(l2[ind2])
        ind2+=1
    # print(list) # lists when bubbling up
    return list

def mergeSort(list):
    # print(list) # lists when dividing
    if len(list) <= 1:
        return list
    pivot = int((len(list))/2)
    l1=mergeSort(list[:pivot])
    l2=mergeSort(list[pivot:])
    return merge(l1,l2)


test_list = [21,4,1,3,9,20,25]
print(mergeSort(test_list))

# test_list = [0,1,2,3,4]
# print(mergeSort(test_list))