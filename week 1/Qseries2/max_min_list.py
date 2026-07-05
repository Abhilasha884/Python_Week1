l1=[('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]

maximum=max(l1,key=lambda x:x[1])
minimum=min(l1,key=lambda x:x[1])

print(maximum,minimum)

