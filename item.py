class Item:
	pay_rate=0.8
	x=2
	all=[] # special class attribute
	def __init__(self,name:str, price:float, quantity=0):
		# Validate arguments
		assert price>=0, f"Price {price} is lesser than 0"
		assert quantity>=0, f"Quantity {quantity} is lesser than 0"

		# assigning self values
		self.__name=name
		self.__price=price
		self.quantity=quantity

		# actions
		Item.all.append(self)

	# HOW TO SET A READ ONLY ATTRIBUTE
	@property
	# Property Decorator = Read Only Attribute
	def name(self):
		return self.__name

	# SETTER - how to set value of read only thing
	@name.setter
	def name(self,value):
		if len(value)>10:
			raise Exception("Length more than 10")
		else:
			self.__name = value


	def apply_discount(self):
		self.__price = self.__price* self.pay_rate

	def apply_increment(self, increment_value):
		self.__price = self.__price + self.__price * increment_value


	# making price attribute read only - ENCAPSULATION
	@property 
	def price(self):
		return self.__price

	def calc_total_price(self):
		return self.__price * self.quantity
	
	

	# a good way to display instances in the all list
	def __repr__(self):
		return f"{self.__class__.__name__}('{self.name}','{self.__price}','{self.quantity}')"

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


	# This is how we create a "Read Only" attribute - cant manually change later - ENcapsulation
	@property
	def read_only_name(self):
		return "AAA"


	# ABSTRACTION
	# below is and example of sample mail sending - we want to access send_mail through a created instance
	# but we dont wanna give access to connect_smtp , generate_body, send etc - not neccessary for the instance
	# only wanna give send_mail() thing
	# do that via __ in front of method name

	def __connect_smtp(self, smtp_server):
		pass
	def __generate_body(self):
		return """
		WEl wel well, we meet again
		just give me the fkin intnshfpis
		"""
	def __send(self):
		pass

	def send_mail(self):
		self.__connect_smtp("1234")
		self.__generate_body()
		self.__send()
		print(f"[*]mail sent from :{self.__name}")






