arr1 = [1, 2, 3, 5, 7, 8, 9, 10]
arr2 = [1, 2, 4, 8, 9]

res=list(filter(lambda x:x in arr2,arr1))

print(res)