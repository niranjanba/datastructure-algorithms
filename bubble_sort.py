list1 = [10, 15, 4, 23, 0]

for j in range(len(list1)-1):
    for i in range(len(list1)-1-j):
        if list1[i] > list1[i+1]: #for decending change to <
            list1[i], list1[i+1] = list1[i+1], list1[i]
#
print(list1)

# size = len(list1)-1
# sort = False
#
# while not sort:
#     sort = True
#     for i in range(size):
#         if list1[i] < list1[i+1]:
#             sort = False
#             list1[i], list1[i+1] = list1[i+1], list1[i]

print(list1)