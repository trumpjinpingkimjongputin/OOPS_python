class Item:
	pay_rate=0.8
	all=[] # special class attribute
	def __init__(self,name:str, price:float, quantity=0):
		# Validate arguments
		assert price>=0, f"Price {price} is lesser than 0"
		assert quantity>=0, f"Quantity {quantity} is lesser than 0"

		# assigning self values
		self.name=name
		self.price=price
		self.quantity=quantity

		# actions
		Item.all.append(self) # each instance gets added to the list

	def calc_total_price(self):
		return self.price * self.quantity
	
	def apply_discount(self):
		self.price = self.price*pay_rate

	# a good way to display instances in the all list
	def __repr__(self):
		return f"Item('{self.name}','{self.price}','{self.quantity}')"

item1 = Item("Phone",100,1)
item2 = Item("Laptop",1000,3)
item3 = Item("Cable",10,5)
item4 = Item("Mouse",50,5)
item5 = Item("Keyboard",75,5)

print(Item.all) # get a list with 5 instances
def display_all():
	for instance in Item.all:
		print(instance.name,end=" ")
# display_all()
