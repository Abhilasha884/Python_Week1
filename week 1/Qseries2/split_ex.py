s=input("Enter a string hyphen separated")

words=s.split('-')
words.sort()
res='-'.join(words)

print(res)