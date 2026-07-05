l1=['Abc','pqr','ipr']

res=list(filter(lambda x:x[0].lower() in 'aeiou',l1 ))

print(res)