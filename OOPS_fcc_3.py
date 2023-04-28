import csv

# when to use staticmethod vs classmethod
# classmethod - when we want to pass in the class iteself - to instantiate something - like from csv file
# staticmethod - the moethod has nothing to do with the instrance - we could define it outside the class as special function but
# we put it inside the class - coz it might have some relation to the features of the class
# static method dont pass in object reference as the first paramenter as argument

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

	# instantiate from CSV file 

	@classmethod
	def instantiate_from_csv(cls):
		with open('items.csv','r') as f:
			reader = csv.DictReader(f)
			items = list(reader)

		for item in items:
			# print(item['name'])
			# Item(name=item.get('name'),price=int(item.get('price')), quantity= int(item.get('quantity')))
			# Item(item.get('name'),int(item.get('price')),int(item.get('quantity')))
			Item(item['name'],float(item['price']),float(item['quantity']))

	@staticmethod
	def is_integer(num):
		# isinstance checks if eg num is float or int etc
		if isinstance(num, float):
			# this method rules out the floats which have .0 at the entd : basically integers
			return num.is_integer()  # this would return False in case we input a decimal
		elif isinstance(num, int):
			return True
		else:
			return False

Item.instantiate_from_csv()
# print(Item.all)

# Static methods
print(Item.is_integer(7.5))

