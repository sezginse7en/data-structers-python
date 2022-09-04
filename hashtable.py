""" Python Dictionary

– This is a Python data type which is same as what is called “associative array” in other programming languages.
– Data are stored in key-value pairs.
– It’s easy to retrieve data from Python Dictionary.   """

city_disct = {"77":"Yalova","34":"İstanbul"}

city_disct["34"] #Output İstanbul


"""   Pyhton List
    – A list is another data type in Python.
    – Data can be stored as tuples.
    – It’s not as easy as python dictionary to retrieve items.
    – We need to use a loop to search for any item in the list.
    – It’s time-consuming to retrieve data. 
"""
city_code = [("77","Yalova"),("06","Ankara")]

def insert(key,value):
    city_code.append((key,value))

def search(key):
    for item in city_code:
        if item[0] == key:
            return item[1]


insert("34","İstanbul")

found = search("77")

#Hash Function
#The goal is find unique key value.

hash_array = [None] * 5

def hash_key(key):
    return key % len(hash_array)

def insert(key,value):
    hashkey = hash_key(key)
    hash_array[hashkey] = value

def search(key):
     hashkey = hash_key(key)
     return hash_array[hashkey]

insert(10,"sezgin")
insert(10,"seven") # collision

#print(hash_array)

#print(search(10))

#Collision Solution : Chaining

hash_table = [[] for _ in range(10)]

def insert(key,value):
     hashkey = hash_key(key)
     hash_table[hashkey].append(value)

def search(key):
    hashkey = hash_key(key)
    return hash_table[hashkey]
    

insert(1,"sezgin")
insert(2,"seven")
insert(1,"sinem")

search(2)


#Standart implementation is build-in hash function

hash_std = [None] * 10

hash_std[hash(1)] = "sezgin"
hash_std[hash(2)] = "seven"
hash_std[hash(1)] = "sinem"

print(hash_std[2])