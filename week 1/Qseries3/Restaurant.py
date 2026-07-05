class restaurant:
    def __init__(self):
        self.menu_item={}
        self.book_table=[]
        self.customer_orders=[]
    def add_item_to_menu(self,item,price):
        self.menu_item[item]=price
    def book_tables(self,table_id):
        self.book_table.append(table_id)
    def customer_order(self,customer_name,item):
        order={"customer":customer_name,"item":item }
        self.customer_orders.append(order)

    def display_menu(self):
        print("\nMenu")
        for item,price in self.menu_item:
            print(item," + ",price)
    def display_tables(self):
        print("Booked tables")
        print(self.book_table)
    def display_order(self):
        print("orders")
        for i in self.customer_orders:
            print(i)

r=restaurant()
n=int(input("Enter total number of items"))
for i in range(n):
    item=input("Enter item name")
    price=int(input("Enter price"))
    r.add_item_to_menu(item,price)
m=int(input("Enter number of tables"))

for i in range(m):
    table = int(input("Enter table number: "))
    r.book_tables(table)

k = int(input("\nEnter number of customer orders: "))

for i in range(k):
    name = input("Enter customer name: ")
    item = input("Enter ordered item: ")
    r.customer_order(name, item)

r.display_menu()
r.display_order()
r.display_tables(2)