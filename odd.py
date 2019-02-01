new_list =[]
for a in range(100,500):
    for b in str(a):
        if int(b) % 2 == 0:
            break
    else:
        new_list.append(a)
print(new_list)
print(len(new_list))







