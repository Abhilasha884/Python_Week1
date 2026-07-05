class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        

    def display(self):
        print("Name ",self.name)
        print("Id ",self.id)
class Manager(Employee):
    def __init__(self, id, name, dept):
        super().__init__(id, name)
        self.dept=dept
    def display(self):
        super().display()
        print("Department ",self.dept)

m=Manager(1,"Abc","Sales")
m.display()
    

        