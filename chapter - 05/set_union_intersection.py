s1 = {2,4,6,77,0}
s2 = {3,2,66,0,5}

print(s1.union(s2))
print(s1.intersection(s2))

print({2,4}.issubset(s1))
print(s1.issuperset({4,77}))
