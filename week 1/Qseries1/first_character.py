sample="restart"
symbol='$'
res=""
first=sample[0]
for i in range(len(sample)):
    if i==0:
        res=res+sample[i]
    elif sample[i]==first:
        res=res+symbol
    else:
        res=res+sample[i]

print(res)
