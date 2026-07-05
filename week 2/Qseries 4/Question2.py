
def fun():
    try:
         n=int(input("Enter a number: "))
    except ValueError:
        raise ValueError("Input not a valid integer")
    
fun()





