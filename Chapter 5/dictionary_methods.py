alphabet = {
    "A":1,
    "B":2,
    "C":3
}

print(alphabet["A"])

print(alphabet.keys()) # Key 
print(alphabet.values()) # Values
print(alphabet.items()) # items
print(alphabet.get("C")) # get

alphabet.update({"D":4}) # update
print(alphabet)

alphabet.pop("D") #pop
print(alphabet)

alphabet.popitem() #popitem
print(alphabet)

alphabet.clear() # clear
print(alphabet)

alphabet2 = alphabet.copy() #copy
print(alphabet2)

alphabet.setdefault("A",1) # setdefault
print(alphabet)