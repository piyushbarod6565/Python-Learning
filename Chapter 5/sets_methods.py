s = {1, 2, 3, 4, 5, 6}

s.add(10)
print(s)

s.update([7,8,9,10,5,8])
print(s)

s.remove(5)
print(s)

s.discard(8)
print(s)

s.discard(15)
print(s)

s.pop()
print(s)

s.clear()
print(s)

print(s, type(s))

a = {1,2,3}
b = {4,5,6}

print(a.union(b))
print(a.intersection(b)) 
print(a.intersection(b))
print(a.symmetric_difference(b))
print(a.issubset(b))
print(b.issuperset(a))
c = s.copy()
print(c)