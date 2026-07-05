d = {
    'Science': [88, 89, 62, 95],
    'Language': [77, 78, 84, 80]
}

result = [
    {key: d[key][i] for key in d}
    for i in range(len(d['Science']))
]

print(result)