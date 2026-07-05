t1=(1,2,3)
t2=("Blue","Red","Black")
t3=t1+t2
print(t3)


print(t3[:5])
'''to delete the tuple use del once deletion you cannot access and single characters of tuple cannot be deleted'''
del t1

print(t3)

'''extended tuple unpacking'''

t1=(7,8,9,0)

a, *b=t1

print(a)
print(b)
'''Set

'''
s1=set(t1)
print(s1)