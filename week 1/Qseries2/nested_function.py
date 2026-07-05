l=int(input("Enter length of rectangle"))
b=int(input("Enter breadth of rectangle"))
# res=total=0
def area(l,b):
    res=l*b
    return res

def price():
    unit=15
    rect_area=area(l,b)
    total=unit*rect_area
    return total
print(area(l,b))
print(price())