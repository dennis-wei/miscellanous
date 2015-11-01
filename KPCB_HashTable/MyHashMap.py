"""
Dennis Wei
Implementation of Hash Map for KPCB Engineering Fellows Program
Uses Separate Chaining through a simple list to handle collisions
"""

class MyHashMap(object):

	# Constructor
	def __init__(self, size):
		self.max_size = size  # User-Specified Hash Table Size
		self.key_arr = []  # Array of Keys
		self.str_arr = []  # Array of Values
		for i in range(0, self.max_size):
			self.key_arr.append([])
			self.str_arr.append([])

	# Adds a new value to the Hash Table
	# Returns true upon successful addition
	# Returns false if key is already in map
	def set(self, key, value):
		map_bin = self.get_hash(key)
		if not key in self.key_arr[map_bin]:
			self.key_arr[map_bin].append(key)
			self.str_arr[map_bin].append(value)
			return True
		# Key already in table
		else:
			print "%s already exists" % (key)
			return False

	# Gets the value at the key
	# Returns the value of the key
	# Returns None if key is not found
	def get(self, key):
		map_bin = self.get_hash(key)
		if key in self.key_arr[map_bin]:
			index = self.key_arr[map_bin].index(key)
			return self.str_arr[map_bin][index]
		else:
			return None

	# Remove the entry with a specified key
	# Returns the value of the removed entry
	# If invalid key, returns None
	def delete(self, key):
		map_bin = self.get_hash(key)
		if key in self.key_arr[map_bin]:
			index = self.key_arr[map_bin].index(key)
			self.key_arr[map_bin].pop(index)
			return self.str_arr[map_bin].pop(index)
		else:
			return None

	# Calculates and returns load factor
	def load(self):
		count = 0
		for key_list in self.key_arr:
			if len(key_list) != 0:
				count += 1
		return count / float(self.max_size)

	# Custom hashing function
	# Takes sum of ASCII values of key and returns the sum modulo the map size
	# Not super effective for very large maps
	def get_hash(self, key):
		sum = 0
		for char in key:
			sum += ord(char)
		return sum % self.max_size

