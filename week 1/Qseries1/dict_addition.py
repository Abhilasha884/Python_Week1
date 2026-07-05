d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

d3={}

for key,value in d1.items():
    d3[key]=value

for key,value in d2.items():
    if key in d3:
        d3[key]+=value
    else:
        d3[key]=value

print(d3)