
'''
a=[val for val in range(1,6) if val%2==0 ]
print(a)


Built in functions like len,upper,lower can be used in list comprehension
User defined functions


'''

l1=["Blue","Orange","Red"]

res=[len(word) for word in l1]

print(res)


l1=["Abc","abcd","pqr"]
l2=[34,45,23]


res=list(zip(l1,l2))
print(res)

