string1="listep"
string2="silent"
len1=len(string1)
len2=len(string2)
if len1!=len2:
    print("Not a Anagram")
else:
    isAnagram=False;
    for ch in string1:
        if string1.count(ch)!=string2.count(ch):
            isAnagram=False
            break
    if isAnagram:
        print("Anagram")
    else:
        print("Not a anagram")