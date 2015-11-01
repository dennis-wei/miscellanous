from MyHashMap import MyHashMap

mhm = MyHashMap(13)

print "\nTesting set method"
print ("Adding | Key: John Doe, Value: 12345")
mhm.set("John Doe", 12345)
print ("Adding | Key: Sarah Smith, Value: 23456")
mhm.set("Sarah Smith", 23456)
print ("Adding | Key: Foo Bar, Value: 14916")
mhm.set("Foo Bar", 14916)
print ("Adding | Key: Peter Jackman, Value: 12345")
mhm.set("Peter Jackman", 12345)
print ("Adding | Key: DG, Value: 54321")
mhm.set("DG", 54321)
print ("Trying to readd Foo Bar")
print ("Foo Bar successfully added: %s") % (mhm.set("Foo Bar", 61941))
print ""

print "Testing hashing function"
print ("John Doe hashes to %d") % (mhm.get_hash("John Doe"))
print ("DG also hashes to %d") % (mhm.get_hash("DG"))
print ""

print "Testing get method"
print ("John Doe has value %d") % (mhm.get("John Doe"))
print ("DG has value %d") % (mhm.get("DG"))
print ("Peter Jackman has value %d") % (mhm.get("Peter Jackman"))
print ("Foo Bar has value %d") % (mhm.get("Foo Bar"))
print ("Not Here has not been inserted and thus has value %s") % (mhm.get("Not Here"))
print ("Hash Map has load factor %.4f") % (mhm.load())
print ""

print "Testing delete method"
print ("Deleting Sarah Smith which has value %d") % (mhm.delete("Sarah Smith"))
print ("After deletion, Sarah Smith has value %s") % (mhm.get("Sarah Smith"))
print ("Trying to Delete Not Here, which has value %s") % (mhm.delete("Not Here"))
print ("After deletion, Hash Map has load factor %.4f") % (mhm.load())
