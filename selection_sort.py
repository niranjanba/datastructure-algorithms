# list1 = [56, 3, 2, 78, 6, 0]
#
# for i in range(len(list1)):
#     min_val = min(list1[i:])
#     min_index = list1.index(min_val)
#     list1[i], list1[min_index] = list1[min_index], list1[i]
# print(list1)
#

## With out using min and max

list1 = [56, 3, 2, 78, 6, 0]
for i in range(len(list1)-1):
    m_ind = i
    for j in range(i+1, len(list1)):
        if list1[j] > list1[m_ind]:
            m_ind = j
    if list1[i] != list1[m_ind]:
        list1[i], list1[m_ind] = list1[m_ind], list1[i]
print(list1)
