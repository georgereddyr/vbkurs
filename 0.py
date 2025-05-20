list = [1, 2, 3, 4, 5, 6, 6, 6, 7, 8, 9]

for i in list:
    try:
        list.remove(6)
    except:
        break
    
print(list)    
