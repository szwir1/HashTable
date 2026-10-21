import pdb

class HashTable:
    def __init__(self):
        collection = {}
        self.collection = collection

    def hash(self, key):
        value = 0
        for x in key:
            value += ord(x)
        return value

    def add(self, key, value):
        hashed_key = self.hash(key)
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}
        self.collection[hashed_key][key] = value

    def lookup(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection:
            if key in self.collection[hashed_key]:
                return self.collection[hashed_key][key]
        else:
            return None

    def remove(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection:
            if key in self.collection[hashed_key]:
                del self.collection[hashed_key][key]
            return

            
        
table = HashTable()

table.add("fcc", "coding")
table.add("cfc", "chemical")

table.remove("fcc")

print(table.collection)
print(table.lookup("fcc"))
print(table.lookup("cfc"))

table.remove("nieistniejacy")  # Powinno zakończyć się bez błędu