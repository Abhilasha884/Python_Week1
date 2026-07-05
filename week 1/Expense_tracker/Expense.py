print("---------------Expense Tracker----------------")

class DuplicateExpenseId(Exception):
    pass
class Wallet:

    def __init__(self,initial_balance):

        self.initial_balance=initial_balance
        self.current_balance=initial_balance
    def get_balance(self):
        # self.current_balance=self.initial_balance
        print("The current Balance is: ",self.current_balance)

    def deduct(self,amount):
        if amount>self.current_balance:
            print("Insufficient balance")
        else:
            self.current_balance=self.current_balance-amount

        

class Expense:
    def __init__(self,id,amount,category):
        self.id=id
        self.amount=amount
        self.category=category
    def display(self):
        print("Id ",self.id)
        print("Amount ",self.amount)
        print("Category ",self.category)


class Expense_manager:
    def __init__(self):
        self.expenses=[]

    def add_expense(self,expense):
        
        for i in self.expenses:
            if i.id==expense.id:
                raise DuplicateExpenseId("Id already present")
        self.expenses.append(expense)

    def view_expense(self):
        if not self.expenses:
            print("No expenses")
        for i in self.expenses:
            i.display()

    def delete_expense(self,id):
        for i in self.expenses:
            if i.id==id:
                self.expenses.remove(i)
                print('Expense removed')
            else:
                print("Expense id not found")

    def total_expense(self):
        total=0
        for i in self.expenses:
            total=total+i.amount
        print('Total Expense: ',total)



def main():
    balance=float(input("Enter the initial balance"))
    w=Wallet(balance)
    e1=Expense_manager()
    while True:

        print("\n========= MENU =========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Show Total Expense")
        print("5. Show Balance")
        print("6. Exit")

        ch=int(input("Enter the choice: "))


        match ch:
            case 1:
                
                id=int(input("Enter id for expense: "))
                
                try:
                    amount=float(input("Enter amount to add: "))
                except ValueError as e:
                    print(e)
                category=input("Enter category of expense: ")
                if amount>balance:
                    print('Insufficient balance')
                else:
                    expense=Expense(id,amount,category)
                    e1.add_expense(expense)
                    w.deduct(amount)
            case 2:
                e1.view_expense()
            case 3:
                id=int(input("Enter id to delete expense"))
                e1.delete_expense(id)
            case 4:
                e1.total_expense()
            case 5:
                w.get_balance()
            case 6:
                print("Thank you")
                break
            case _:
                print('Invalid choice')

if __name__=="__main__":
    main()

