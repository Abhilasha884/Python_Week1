def add_list():
    a=[]
    n=int(input("Enter number of elements: "))
    for i in range(n):
        num=int(input("Enter list elements: "))
        a.append(num)
    try:
        print(a[89])
    except IndexError as e:
        print("error",e)
    print(a)

add_list()
