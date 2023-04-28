# INHERITENCE
# what is inheritence in python oops ? 
# using features  n methods of one class in another class

# we use super function to inherit all methods from the class we're inheriting from
# THING LEARNT IN INHERITENCE
# 1. class Phone(Item):
# 2. {self.__class__.__name__}
# 3. super().__init__(name,price, quantity)
# 4. inheriting functions like => Phone.calc_total_price

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
		return f"{self.__class__.__name__}('{self.name}','{self.price}','{self.quantity}')"

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

class Phone(Item):
	def __init__(self,name:str,price:float,quantity=0,broken_phones=0):
		# call super function
		super().__init__(name,price,quantity)

		assert broken_phones>=0, f"broken phones cant be negative"

		# assigning to self object
		self.broken_phones=broken_phones

# now we can inherit the features of Item in Phone so we dont need to assign name rpice etc seprately, we can even directly use the functions
phone1=Phone("Pixel",500,20,1)
item1 = Item("Laptop",200,10)
# print(phone1.calc_total_price())

# stuff
print(Item.all)
print(Phone.all)

# more sstuff related to above stuff


