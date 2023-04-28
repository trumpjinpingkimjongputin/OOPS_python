#OOPS principles
# 1. Encapsulation
# 2. Abstraction - show only neccessary attributes
# 3. Inheritence
# 4. Polymorphism - use of single type entity to be represent different types in different scenarios 
from keyboard import Keyboard
from item import Item
# 1. Encapsulation

item1= Item("myItem",100)
print(item1.price)

item1.apply_increment(0.2) # direct access not allowed - only through pre def methods
print(item1.price)

# 2. Abstraction 
item1.send_mail()
	# we cant call item1.__connect_smtp etc

# 3. Inheritence
from phone import Phone
	# done that
item2=Phone("iPhone 6s",100,3)
item2.send_mail() # we are able to use method defined in Item class - through an instance of Phone class

# 4. Polymorphism
# eg - len function 
keyboard1 = Keyboard("keyb1",200,3)
keyboard1.apply_discount()
print(Item.all)

