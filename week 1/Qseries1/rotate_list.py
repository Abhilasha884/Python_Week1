'''right rotation'''
# l1=[6,5,3,2,1]
# # 1 6 5 3 2
# # 2 1 6 5 3
# # 3 2 1 6 5
# step=3
# for i in l1:
#     res=l1[-step::]+l1[:-step]

# print(res)


#or

l1=[5,3,9,8,7]
step=3

for i in range(step):
    last=l1[-1]
    l1.pop()
    l1.insert(0,last)

print(l1)

