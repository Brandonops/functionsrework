list2 = []
def only_odds(list):
    for i in list:
        if i % 2 != 0:
            list2.append(i)
    list2.sort()        
    return print(list2)

only_odds([22, 75, 84, 5, 2, 10, 11, 13])
