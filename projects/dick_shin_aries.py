#some dick_shin_aries fun
numbers = [1,48,20]
print(numbers[0] + numbers[1] + numbers[2])

animals = ["sloth", "virgin", "zebra", "leonard"]
print(animals)
animals[3]= "picachu"
print(animals)
print("my favorite numbers are, %s, and my favorite animals are %s!" % (numbers, animals))
print("my favoritest number is %s and my most favorite animal is %s" % (numbers[1], animals[3]))

inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] = inventory['gold'] + 50