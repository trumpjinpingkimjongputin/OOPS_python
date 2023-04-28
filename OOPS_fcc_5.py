from item import Item

item1=Item("test",100,2)
# print(Item.all)

print(item1.name)
# print(item1.__name) # __ represents private attributes for class - so we cant access
# item1.name="teting" #doesnt work

#implemented setter
item1.name="testin"
print(item1.name)