class Item:
	#class attributes
	pay_rate=0.8
	def __init__(self,name:str,price:float,quantity=0): # this self is basically the item instance itself - python automatically takes it by default
		# Validating arguments
		assert price>=0, f"Price {price} isnt greater than eq to 0" # put error statements
		assert quantity>=0

		# Assign to self object
		self.name=name # self is basically item1, item 2 etc - get the feel - its the instance itself
		self.price=price
		self.quantity=quantity
	# def calc_total_price(self,x,y):
	# 	return x*y

	def calc_total_price(self):
		return self.price * self.quantity

	def apply_discount(self):
		self.price = self.price * self.pay_rate # we cant directly access a class attribute even inside the class
		#self.price = self.price* Item.pay_rate

item1=Item("Phone",100,5)
# item1.name="Phone"
# item1.price=100
# item1.quantity=5
# print(item1.calc_total_price(item1.price,item1.quantity))

item2=Item("Laptop",1000,3)
# item2.name='Laptop'
# item2.price=1000
# item2.quantity=3
# print(item2.calc_total_price(item2.price,item2.quantity))

item2.has_numpad = False # we can define custom attributes as well, even if some are def in class

item3=Item("Desktop",1000) # quantity is defaul 0
print(item1.name, item2.price)
print(item1.calc_total_price())
#class attributes
# print(Item.pay_rate)
# print(item1.pay_rate)

#magic attribute
# print(Item.__dict__)
# print("*******")
# print(item1.__dict__)

# discount
item1.apply_discount()
print(item1.price)

item2.pay_rate=0.7 #30% discount
item2.apply_discount()
print(item2.price)

