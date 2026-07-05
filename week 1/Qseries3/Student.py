class Student:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def display(self):
        print("ID ",self.id)
        print("Name ",self.name)
s=Student(1,"Abc")
s.display()
s.class_name="B Tech"
print(s.class_name)
        