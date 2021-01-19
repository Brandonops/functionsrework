list1 = [30, 50, 2, 5, 9, 11, 200, 14]
list2 = []
def only_evens(list):
    for i in list:
        if i % 2 == 0:
            list2.append(i)    
    list2.sort()  
    return print(list2)

only_evens([55, 52, 90, 4, 9, 11, 15, 21])


