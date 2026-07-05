str=input("Enter a string")
upper=0
lower=0
for ch in str:
    if ch.isupper():
        upper=upper+1
    else:
        lower=lower+1

print("No of uppercase characters: ",upper)
print("No of lowercase characters: ",lower)
