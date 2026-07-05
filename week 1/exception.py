'''
zero Division error 
n1=int(input("Enter number to be divided"))
n2=int(input("Enter number to divide"))

try:
    res=n1/n2
except ZeroDivisionError:
    print("Divide by zero error")
else:
    print(res)

finally:
    print("Division file")
'''

'''Multiple Exceptions

l1=[2,"Hello",50]

try:
    res=l1[0]+l1[6]
except (TypeError,IndexError) as e:
    print("Error",e)
except IndexError as e:
    print("Error",e)
finally:
    pass
'''

'''Raising exception

def age(n):
    if n<0:
        raise ValueError("Age cannot be negative")
    print("Age is ",n)

try:
    age(3)
except ValueError as e:
    print("Error",e)
    
'''

'''raising custom exception

class InvalidAgeError(Exception):
    pass

try:
    n=int(input("Enter the age"))
    if n<0:
        raise InvalidAgeError("Age should not be negative")
    else:
        print("Age entered is ",n)
    
except InvalidAgeError as e:
    print(e)

'''

