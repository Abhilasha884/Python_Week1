'''unordered and key value pair data'''

d1={"name":"Abc","age":22}
'''Accessing using key'''
print(d1["name"])

'''Accessing a missing key with [ ] raises a KeyError, while get() is safer because it returns None (or a default value) instead of an error.
to iterate use key or value'''

for key in d1:
    print(key)


for value in d1.values():
    print(value)


d1 = {"a": 1, "b": 2}
# for key, value in d.items():
#     print(key, value)

d2={"c":3,"d":4}
'''to concat two dictionaries
| Method         | Creates New Dictionary?   | Modifies Original? | Python Version |             |
| -------------- | ------------------------- | ------------------ | -------------- | ----------- |
| `update()`     | ❌ No                      | ✅ Yes              | All versions   |             |
| `              | ` operator                | ✅ Yes              | ❌ No           | Python 3.9+ |
| `{**d1, **d2}` | ✅ Yes                     | ❌ No               | Python 3.5+    |             |
| `for` loop     | ✅ Yes (if using `copy()`) | Optional           | All versions   |             |
Use update() if you want to modify an existing dictionary.
Use {**dict1, **dict2} if you want to create a new merged dictionary (works in Python 3.5+).
Use the | operator if you're using Python 3.9 or later and prefer concise syntax.
Use a for loop if you need custom merging logic (e.g., combining values instead of overwriting).

'''
d3=d1|d2
print(d3)







