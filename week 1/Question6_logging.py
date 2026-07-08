import logging

logging.basicConfig(
    filename="user.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class User_fn:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

        logging.info("Name received: %s, Age: %d, Salary: %d",self.name,self.age,self.salary)

        if age<0:
            logging.error("Age cannot be negative")

    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Salary: ",self.salary)
        logging.info("User details displayed for%s ",self.name)

name=input("Enter name: ")
age=int(input("Enter age: "))
salary=int(input("Enter salary: "))
u=User_fn(name,age,salary)
u.display()
